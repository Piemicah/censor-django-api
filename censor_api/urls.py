from django.urls import path
from . import views

urlpatterns = [
    path("persons/", views.PersonListCreate.as_view(), name="person_list"),
    path("persons/<int:pk>/", views.PersonRUD.as_view(), name="person_detail"),
    path("manage_tokens/", views.SaveApi.as_view()),
    path("logout/", views.Logout.as_view()),
    # path("persons/edit/<int:pk>/", views.UpdatePersonView.as_view(), name="update"),
    # path("persons/delete/<int:pk>/", views.DeletePersonView.as_view(), name="delete"),
]
