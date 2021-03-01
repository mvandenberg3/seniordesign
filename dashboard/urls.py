from django.urls import path, include
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, {'pagename': ''}, name='home'),
    path('<str:pagename>', views.index, name='index'),
]
