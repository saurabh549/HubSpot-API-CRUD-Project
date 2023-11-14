// contacts/static/contacts/script.js
let afterId = null;

function createNextPageButton() {
    const nextPageButton = document.createElement('button');
    nextPageButton.id = 'nextPageBtn';
    nextPageButton.textContent = 'Next Page';
    nextPageButton.addEventListener('click', function () {
        fetchContacts(`/contacts/${afterId}`);
    });

    document.body.appendChild(nextPageButton);
}

document.addEventListener('DOMContentLoaded', function() {
    // Your function to be executed on page load
    fetchContacts('/contacts/');
});

// document.getElementById('fetchContactsBtn').addEventListener('click', function () {
//     fetchContacts('/contacts/');
// });

document.getElementById('searchContactBtn').addEventListener('click', function () {
    const contactId = document.getElementById('contactIdInput').value;
    if (contactId) {
        fetchContacts(`/contacts/details/${contactId}`);
    }
});

function fetchContacts(apiUrl) {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            displayContacts(data.contacts);
            afterId = data.next_page_id;
            if (!document.getElementById('nextPageBtn') && afterId) {
                createNextPageButton();
            }
        })
        .catch(error => console.error('Error fetching contacts', error));
}

function displayContacts(contacts) {
    let contactsTable = document.getElementById('contactsTable');

    if (!contactsTable) {
        contactsTable = document.createElement('table');
        contactsTable.id = 'contactsTable';
        contactsTable.className = 'table table-bordered';
        document.body.appendChild(contactsTable);
    }

    contactsTable.innerHTML = '';

    const tableHeader = document.createElement('thead');
    tableHeader.innerHTML = `
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
    `;
    contactsTable.appendChild(tableHeader);

    const contactsBody = document.createElement('tbody');
    contacts.forEach(contact => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${contact.id}</td>
            <td>${contact.properties.firstname}</td>
            <td>${contact.properties.lastname}</td>
            <td>${contact.properties.email}</td>
            <td><button class="update-btn" onclick="updateContact(${contact.id})">Update</button></td>
            <td><button class="delete-btn" onclick="deleteContact(${contact.id})">Delete</button></td>
        `;
        contactsBody.appendChild(row);
    });
    contactsTable.appendChild(contactsBody);
}

function updateContact(contactId) {
    // Redirect to the update page with the contact ID
    window.location.href = `/update_contact/${contactId}/`;
}

function deleteContact(contactId){
    // Redirect to the update page with the contact ID
    window.location.href = `/delete_contact_api/${contactId}/`;
}