var users = [];
function displayUsers() {
    var tableBody = document.getElementById('userTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';

    users.forEach(function(user){
        var row = tableBody.insertRow();
        row.insertCell(0).textContent = user.id;
        row.insertCell(1).textContent = user.name;
        row.insertCell(2).textContent = user.age;
        row.insertCell(3).textContent = user.phone;

        var updateCell = row.insertCell(4);
        var updateButton = document.createElement('button');
        updateButton.textContent = 'Update';
        updateButton.onclick = function() { updateUser(user); };
        updateCell.appendChild(updateButton);

        var deleteCell = row.insertCell(5);
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function() { deleteUser(user); };
        deleteCell.appendChild(deleteButton);
    });
}

function updateUser(user) {
    document.getElementById('userId').value = user.id;
    document.getElementById('userName').value = user.name;
    document.getElementById('userAge').value = user.age;
    document.getElementById('userPhone').value = user.phone;

    document.getElementById('saveButton').style.display = 'inline-block';
    document.getElementById('addButton').style.display = 'none';
}

function saveUser() {
    var userId = document.getElementById('userId').value;
    var userName = document.getElementById('userName').value;
    var userAge = document.getElementById('userAge').value;
    var userPhone = document.getElementById('userPhone').value;

    document.getElementById('saveButton').style.display = 'none';
    document.getElementById('addButton').style.display = 'inline-block';

    var userIndex = users.findIndex(function(user) {
        return user.id == userId;
    });

    if (userIndex !== -1) {
        users[userIndex].name = userName;
        users[userIndex].age = userAge;
        users[userIndex].phone = userPhone;

        fetch(`http://localhost:3011/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(users[userIndex]),
        })

        .then(response => response.json())
        .then(data => {
            console.log('Useri u be update:', data);
            document.getElementById('userForm').reset();
            displayUsers();
        })
    }
}

function deleteUser(user) {
    var confirmation = confirm('A je i sigurt qe don me fshi zotni a jo?');
    if (confirmation) {
        users = users.filter(function(u) {
            return u.id !== user.id;
        });

        fetch(`http://localhost:3011/users/${user.id}`, {
            method: 'DELETE',
        })

        .then(response => response.json())
        .then(data => {
            console.log('Useri u fshi:', data);
            displayUsers();
        })
    }
}

function addUser() {
    var userName = document.getElementById('userName').value;
    var userAge = document.getElementById('userAge').value;
    var userPhone = document.getElementById('userPhone').value;

    var maxId = Math.max(...users.map(user => user.id));
    var newUserId = maxId + 1;

    var newUser = {
        id: newUserId,
        name: userName,
        age: userAge,
        phone: userPhone
    };

    fetch('http://localhost:3011/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newUser),
    })

    .then(response => response.json())
    .then(data => {
        console.log('Useri u shtu:', data);
        document.getElementById('userForm').reset();
        displayUsers();
        window.location.reload();
    })
}


fetch('http://localhost:3010/users')
.then(response => response.json())
.then(data => {
    users = data;
    displayUsers();
})