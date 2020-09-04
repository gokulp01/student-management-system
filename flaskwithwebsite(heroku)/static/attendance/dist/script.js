"use strict";
var body = document.body;
var tilted = false;
var toggleTilt = function () {
    tilted = !tilted;
    if (tilted)
        body.classList.add('details');
    else
        body.classList.remove('details');
};
body.addEventListener('click', toggleTilt);
body.addEventListener('touchstart', toggleTilt);
if (location.pathname.match(/fullcpgrid/i))
    setTimeout(toggleTilt, 1000);