from django.contrib import admin
from django.urls import path
from hijab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form/', views.form),
]
