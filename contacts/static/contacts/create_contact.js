function submitForm() {
    const form = document.getElementById('createContactForm');
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Update the page content to show the contact_id
        document.getElementById('contactId').textContent = data.contact_id;
        document.getElementById('contactIdResult').style.display = 'block';
    })
    .catch(error => console.error('Error creating contact', error));
}