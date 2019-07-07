from django.urls import path
from . import views
urlpatterns = [
    path('<name>/', views.add_to_wish, name='add_to_wish'),
    path('wishPage/<userName>/', views.showWishPage, name='showWishPage'),
    path('<userName>/<pk>/delete/', views.deleteWish, name='deleteWish'),
]
