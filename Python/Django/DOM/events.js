var headHover = document.querySelector('#hover');
var headClick = document.querySelector('#click');
var headDouble = document.querySelector('#double');

headHover.addEventListener("mouseover", function(){
    headHover.textContent = "I hovered over the  text!";
    headHover.style.backgroundColor = "azure";
})

headHover.addEventListener("mouseout", function() {
    headHover.textContent = "Hover Over Me!";
    headHover.style.backgroundColor = "white";
})

headClick.addEventListener("click", function(){
    headClick.textContent = "I've been clicked!";
    headClick.style.color = 'blue';
})

headDouble.addEventListener("dblclick", function(){
    headDouble.textContent = "I've been dooped!";
    window.scrollTo(0, 0);
})