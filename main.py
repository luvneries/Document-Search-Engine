#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:30:08 2018

@author: Pankaj Sharma
"""

from flask import Flask, render_template, request, jsonify, redirect, session, flash
from urlRetrieval_Tfidf import sentence_similarity
from flask_mysqldb import MySQL
import webbrowser
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "This is my secret key"
#app.debug=True

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'documentFinder'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

url_opera=""
url_dal=""
url_cfodl=""

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    flash(a,b)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/<string:application_name>/")
def applicationPage(application_name):
    session['app']=application_name
    flash(urlList(application_name))
    return render_template("home.html")

@app.route('/', methods=['GET', 'POST'])
def executeProcess():
    UserInput = request.form['msg']
    processed_text = sentence_similarity_query(UserInput.lower())

    #Open connection
    cur = mysql.connection.cursor()
    #key to update user feedback
    #result = cur.execute("SELECT max(feedback_id)+1 FROM user_search_history")
    #session['feedback_id'] = result.fetchone()

    #Inset search text into Database
    cur.execute("INSERT INTO user_search_history(search_text, url_provided, application_id) VALUES(%s, %s, %s)", (UserInput, processed_text, session['app']))
    mysql.connection.commit()
    cur.close()
    #session['output']=processed_text
    #flash(session['feedback_id'])
    return redirect(processed_text, code=302)

def update_user_feedback():
    userFeedback = request.form['feedback']

    if userFeedback:
    #Open connection
        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_search_history SET user_feedback=%s WHERE id=%s",(userFeedback, session['feedback_id']))

def urlList(app_name):
        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by application name
        result = cur.execute("SELECT distinct url_name, url_title FROM url_details WHERE url_application = %s", [app_name])
        urls = cur.fetchall()
        cur.close()

        url_name = []
        url_title = []
        for i in urls:
            url_name.append(i['url_name'])
            url_title.append(i['url_title'])

        return url_name, url_title

def sentence_similarity_query(userInput):
    userInput = " ".join(re.compile('\w+').findall(userInput.lower()))
    print(userInput)
    score_list=[]
    urls_List, urls_Title = urlList(session['app'])
    for url in urls_List:
        url = " ".join(re.compile('\w+').findall(url.lower()))
        score_list.append(sentence_similarity(userInput,url))
    best_match = urls_List[score_list.index(max(score_list))]
    return best_match

@app.errorhandler(404)
def page_not_found(e):
     return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
