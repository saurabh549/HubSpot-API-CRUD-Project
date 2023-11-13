# contacts/urls.py
from django.urls import path
from .views import contact_list,index, contact_details, create_contact, create_contact_api, update_contact,update_contact_api, delete_contact_api

urlpatterns = [
    #Read Contacts
    path('', index),
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<str:after_id>/', contact_list, name='contact_list_with_id'),
    path('contacts/details/<int:contact_id>/', contact_details, name='contact_details'),
    #Create Contacts
    path('create_contact/',create_contact),
    path('create_contact_api/',create_contact_api),
    #Update Contacts
    path('update_contact/<int:contact_id>/',update_contact),
    path('update_contact_api/<int:contact_id>/',update_contact_api),
    #Delete Contacts
    path('delete_contact_api/<int:contact_id>/',delete_contact_api),
]
