from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_review, name='add_view'),
    #path('deleteReview/<userName>/<productName>/', views.deleteReview, name='deleteReview'),
]
