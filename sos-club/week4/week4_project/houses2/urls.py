from django.urls import path
from . import views

# urlpatterns=[
#     path("", views.Houses.as_view()),
# 	path("<int:pk>", views.HouseDetail.as_view()),
# ]

urlpatterns = [
    path("", views.HouseViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path("<int:pk>", views.HouseViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]