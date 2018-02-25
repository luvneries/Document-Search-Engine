var background1 = 'black';
var background2 = 'firebrick';

var color = true;

setInterval(function () {
    document.body.style.backgroundColor = (color ? background1 : background2)
    color = !color;
}, 1000);