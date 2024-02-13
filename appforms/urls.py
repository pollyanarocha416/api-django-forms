from django.urls import path, include
# from tarefa.views import
from rest_framework import routers
# from tarefa.serializer import


router = routers.DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
]
