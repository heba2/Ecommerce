from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactPage, name='contactPage'),
    path('<userName>/', views.contact, name='contact'),
    path('admin/messages/', views.showMessages, name='showMessages')
]
