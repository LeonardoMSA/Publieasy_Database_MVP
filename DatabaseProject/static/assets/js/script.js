"use strict"

function screenChanges(screenWidth)
{
    const sloganTitle = document.querySelector('.slogan-title');
    const sloganSubTitle = document.querySelector('.sub-slogan');


    if (screenWidth.matches) 
        sloganTitle.innerHTML = sloganTitle.textContent.replace('<br>', '');
    
    if (screenWidth.matches) 
        sloganSubTitle.innerHTML = sloganSubTitle.textContent.replace('<br>', '');
    
}

screenChanges(window.matchMedia("(max-width: 600px)"));
window.matchMedia("(max-width: 600px)").addListener(screenChanges);
