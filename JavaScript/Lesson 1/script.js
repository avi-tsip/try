const button = document.getElementById('button');
const text = document.getElementById('text');

button.addEventListener('click', function()
{
    if (text.classList.contains('d-none')) 
    {
        text.classList.remove('d-none');
        text.textContent = 'Someone just clicked the button!';
        button.textContent = 'Close me!'
    }
    else
    {
        text.classList.add('d-none');
        text.textContent = '';
        button.textContent = 'Click me!';
    }
});