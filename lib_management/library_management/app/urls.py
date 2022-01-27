from django import urls
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import viewsets

router=DefaultRouter()
router.register('admin',viewsets.LoginViewset)
router.register('book',viewsets.BookViewset)
router.register('book',viewsets.UpdateViewset)
router.register('signup',viewsets.RegisterViewset)

urlpatterns=[
    # path('signup/',viewsets.RegisterViewset.as_view()),
    # path('register',viewsets.RegisterView.as_view()),
    path('',include(router.urls))

]