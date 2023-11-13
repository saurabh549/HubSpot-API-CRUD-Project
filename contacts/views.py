# contacts/views.py
from django.shortcuts import render,HttpResponse
import requests
import json
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    return render(request, 'contacts/contact_list.html')

def contact_list(request,after_id=None):
    api_url = f'https://api.hubapi.com/crm/v3/objects/contacts?after={after_id}' if after_id else 'https://api.hubapi.com/crm/v3/objects/contacts?after=0'
    payload = {}
    headers = {
    'Authorization': 'Bearer pat-na1-c4752074-664d-4967-9e49-92e1e5277f67'
    }

    try:
        response = requests.request("GET", api_url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx responses

        data = response.json()
        contacts = data.get('results', [])
        next_page = data.get('paging',{})
        next_page_details = next_page.get('next',{})
        next_page_id = next_page_details.get('after',{})
        return JsonResponse({'contacts': contacts,'next_page_id':next_page_id})
        #return render(request, 'contacts/contact_list.html', {'contacts': contacts})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def contact_details(request, contact_id):
    api_url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}'
    payload = {}
    headers = {
        'Authorization': 'Bearer pat-na1-c4752074-664d-4967-9e49-92e1e5277f67'
    }

    try:
        response = requests.get(api_url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx responses

        contacts = response.json()
        return JsonResponse({'contacts': [contacts]})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def create_contact(request):
    return render(request, 'contacts/create_contact.html')



def create_contact_api(request):
    url = "https://api.hubapi.com/crm/v3/objects/contacts"

    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')

    payload = json.dumps({
            "properties": {
                "firstname": firstname,
                "lastname": lastname,
                "email": email
            }
        })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer pat-na1-c4752074-664d-4967-9e49-92e1e5277f67'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        print(data)
        contact_id = data.get('id')
        return JsonResponse({'contact_id': contact_id})
    except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)



def update_contact(request,contact_id):
    return render(request, 'contacts/update_contact.html',{'contact_id':contact_id})

def update_contact_api(request,contact_id):
    api_url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}'

    firstname = ""
    if 'firstname' in request.POST:
        firstname = request.POST.get('firstname')

    lastname = ""
    if 'lastname' in request.POST:
        lastname = request.POST.get('lastname')
    
    email = ""
    if 'email' in request.POST:
        email = request.POST.get('email')

    payload = {"properties":{}}

    if firstname != "":
        payload['properties']['firstname'] = firstname
    
    if lastname != "":
        payload['properties']['lastname'] = lastname

    if email != "":
        payload['properties']['email'] = email

    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer pat-na1-c4752074-664d-4967-9e49-92e1e5277f67'
    }
    try:
        response = requests.request("PATCH", api_url, headers=headers, data=payload)
        data = response.json()
        print(data)
        contact_id = data.get('id')
        return JsonResponse({'contact_id': contact_id})
    except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)


def delete_contact_api(request,contact_id):
    api_url = f'https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}'
    payload = {}
    headers = {
        'Authorization': 'Bearer pat-na1-c4752074-664d-4967-9e49-92e1e5277f67'
    }

    try:
        response = requests.request("DELETE", api_url, headers=headers, data=payload)
        #response.raise_for_status()  # Raise an exception for 4xx and 5xx responses
        if response.status_code == 204:
            return render(request, 'contacts/contact_list.html')
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)