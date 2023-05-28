
from django.contrib import admin
from django.urls import path, include
from Menu import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('booklist/', include('Menu.urls')),
    path('admin/', admin.site.urls, name="admin"),
]

