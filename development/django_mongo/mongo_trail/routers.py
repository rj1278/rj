from rest_framework import routers
from . import viewset

router=routers.DefaultRouter()
router.register(r'member',viewset.MemberViewset)
