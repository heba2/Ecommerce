from django.contrib import admin
from django.urls import path, include
from accounts import views
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('home/', views.index, name='index'),
    path('products/', include('products.urls', namespace='product')),
    path('cart/', include('cart.urls')),
    path('contact/', include('contact.urls')),
    path('about/', views.about, name='about'),
    path('search/', include('search.urls')),
    path('checkout/', views.checkout, name='checkout'),
    path('wish/', views.add_wish, name='wish'),
    path('orderComplete/', views.order_complete, name='orderComplete'),
    path('review/', include('review.urls')),
    path('wish/', include('wishlist.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

