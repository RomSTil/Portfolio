from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuView.as_view(), name='home'),  # Пример маршрута для главной страницы
]