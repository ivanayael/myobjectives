const form = document.getElementById('notToDoForm');
const taskInput = document.getElementById('taskInput');
const taskList = document.getElementById('taskList');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const taskText = taskInput.value.trim();
    if (taskText === '') return;

    const li = document.createElement('li');
    li.textContent = taskText;

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'X';
    deleteButton.className = 'delete';
    deleteButton.onclick = () => li.remove();

    li.appendChild(deleteButton);
    taskList.appendChild(li);

    taskInput.value = '';
});