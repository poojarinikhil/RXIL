document.addEventListener('DOMContentLoaded', function () {
    const userForm = document.getElementById('userForm');
    const entityForm = document.getElementById('entityForm');
    const usersList = document.getElementById('usersList');
    const entitiesList = document.getElementById('entitiesList');

    if (userForm) {
        userForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            const formData = new FormData(userForm);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch('/users/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                loadUsers();
            }
        });

        loadUsers();
    }

    if (entityForm) {
        entityForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            const formData = new FormData(entityForm);
            const data = Object.fromEntries(formData.entries());

            const response = await fetch('/entities/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                loadEntities();
            }
        });

        loadEntities();
    }

    async function loadUsers() {
        const response = await fetch('/users/');
        const users = await response.json();
        usersList.innerHTML = users.map(user => `
            <div>
                <h3>${user.name} (${user.email})</h3>
                <button onclick="deleteUser(${user.id})">Delete</button>
            </div>
        `).join('');
    }

    async function loadEntities() {
        const response = await fetch('/entities/');
        const entities = await response.json();
        entitiesList.innerHTML = entities.map(entity => `
            <div>
                <h3>${entity.name}</h3>
                <p>${entity.description}</p>
                <p>User ID: ${entity.user_id}</p>
                <button onclick="deleteEntity(${entity.id})">Delete</button>
            </div>
        `).join('');
    }

    window.deleteUser = async function (id) {
        const response = await fetch(`/users/${id}`, { method: 'DELETE' });
        if (response.ok) {
            loadUsers();
        }
    }

    window.deleteEntity = async function (id) {
        const response = await fetch(`/entities/${id}`, { method: 'DELETE' });
        if (response.ok) {
            loadEntities();
        }
    }
});
