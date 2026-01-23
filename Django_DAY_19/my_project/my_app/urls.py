from django.urls import path
from .views import home, edit_contact, delete_contact

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:id>/', edit_contact, name='edit'),
    path('delete/<int:id>/', delete_contact, name='delete'),
]
