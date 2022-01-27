from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter,SimpleRouter

router=DefaultRouter()
router.register('fileUpload',views.FileuploadViewset)
router.register('download',views.ExampleViewSet)
urlpatterns = [
    path('assest', views.StudentList.as_view()),
    path('assest/<int:pk>/', views.StudentDetail.as_view()),
    path('file',include(router.urls))
    
]
