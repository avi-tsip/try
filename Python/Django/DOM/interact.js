alert("We are about to change the text of the paragraph");

var par = document.querySelector('p');

par.textContent = 'This text has been changed';

alert("Now, I am about to make the text bold");

par.innerHTML = "<strong>This text has been changed</strong>";

alert("Lets mess with the facebook link");

var special = document.querySelector('#special');

var specialA = special.querySelector('a')

specialA.getAttribute('href');

specialA.setAttribute('href', 'https://www.amazon.com')