from django.urls import path
from . import views


urlpatterns = [
    path('', views.home), # home
    path('recipes/<int:id>/', views.recipe),


]