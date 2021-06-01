from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.StudentView)

app_name = 'student'

urlpatterns = [
    path('', include(router.urls)),
]