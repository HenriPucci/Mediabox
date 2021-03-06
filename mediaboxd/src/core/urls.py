from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reviews/', include('reviews.urls')),
]