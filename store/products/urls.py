from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products, name='products'),
    path('<name>/', views.single_product, name='product_Detail'),
    path('categoryFilter/<name>/', views.categoryFilter, name='categoryFilter'),
    ]
