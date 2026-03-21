from django.urls import path
from . import views

urlpatterns = [
    # Train URLs
    path("", views.train_list, name="train_list"),
    path("train/<int:pk>/", views.train_detail, name="train_detail"),
    path("train/create/", views.create_train, name="create_train"),
    path("train/<int:pk>/update/", views.update_train, name="update_train"),
    path("train/<int:pk>/delete/", views.delete_train, name="delete_train"),
    # Carriage URLs
    path("carriages/", views.carriage_list, name="carriage_list"),
    path("carriage/<int:pk>/", views.carriage_detail, name="carriage_detail"),
    path("carriage/create/", views.create_carriage, name="create_carriage"),
    path("carriage/<int:pk>/update/", views.update_carriage, name="update_carriage"),
    path("carriage/<int:pk>/delete/", views.delete_carriage, name="delete_carriage"),
]