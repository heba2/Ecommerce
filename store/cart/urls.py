from django.urls import path
from . import views
urlpatterns = [
    path('<name>/', views.add_to_cart, name='add_to_cart'),
    path('cartPage/<userName>/', views.showCartPage, name='showCartPage'),
    path('<userName>/<pk>/delete/', views.deleteCart, name='deleteCart')
]
