from django.urls import path,include

from . import routers
from . import views

urlpatterns=[
    path('',include(routers.router.urls))
]