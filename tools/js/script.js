document.getElementById('notToDoForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const input = document.getElementById('taskInput');
    const newTask = input.value;

    if (newTask) {
        const li = document.createElement('li');
        li.className = 'permanent';
        li.textContent = newTask;
        
        // Efecto visual de "alerta" al agregar
        li.style.borderColor = '#38bdf8'; 
        
        document.getElementById('taskList').prepend(li);
        input.value = '';
    }
});

