// Selectors
const todoInput = document.querySelector('.todo-input');
const todoButton = document.querySelector('.todo-button');
const todoList = document.querySelector('.todo-list');
const filterOption = document.querySelector('.filter-todo');



//Event Listeners
todoButton.addEventListener('click', addTodo);
todoList.addEventListener('click', deleteAndCheck);
filterOption.addEventListener('click', filterTodo);

//Functions
function addTodo(event) {
    //prevents from the submit button to refresh the browser
    event.preventDefault();
    //Check that the field is not empty
    if (todoInput.value != '') {
        //Create a todo div
        const todoDiv = document.createElement('div');
        todoDiv.classList.add('todo');
        //Create li
        const todoLi = document.createElement('li');
        todoLi.innerText = todoInput.value;
        todoLi.classList.add('todo-item');
        todoDiv.appendChild(todoLi);
        //Create a completed button
        const completedButton = document.createElement('button');
        completedButton.innerHTML = '<i class="fa fa-check"></i>';
        completedButton.classList.add('complete-btn');
        todoDiv.appendChild(completedButton);
        //Create a trash button
        const trashButton = document.createElement('button');
        trashButton.innerHTML = '<i class="fa fa-trash"></i>';
        trashButton.classList.add('trash-btn');
        todoDiv.appendChild(trashButton);
        //Append to list
        todoList.appendChild(todoDiv);
        //Clear todo field
        todoInput.value = '';
    }
    else {
        window.alert('Input cannot be empty!')
    }
}

function deleteAndCheck(event) {
    const item  = event.target;
    if (item.classList[0] === 'trash-btn') {
        const todo = item.parentElement;
        todo.classList.add('fall');
        todo.addEventListener('transitionend', function() {
            todo.remove();
        });
    }
    if (item.classList[0] === 'complete-btn') {
        const todo = item.parentElement;
        todo.classList.toggle('completed');
    }

}

function filterTodo(event) {
    const todos = todoList.childNodes;
    todos.forEach(function(todo) {
        switch(event.target.value){
            case "all":
                todo.style.display = 'flex';
                break;
            case "completed":
                if (todo.classList.contains('completed')) {
                    todo.style.display = 'flex';
                } else {
                    todo.style.display = 'none';
                }
                break;
            case "notComp":
                if (!todo.classList.contains('completed')) {
                    todo.style.display = 'flex';
                } else {
                    todo.style.display = 'none';
                }
                break;
        }
    });
}