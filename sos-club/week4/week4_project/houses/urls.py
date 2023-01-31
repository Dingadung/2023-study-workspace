from django.urls import path
from . import views
urlpatterns=[
    # path("", views.Houses.as_view()),
    path("", views.houses),
    path("<int:pk>", views.house),
]