from rest_framework import routers
from namelist.viewsets import NamelistViewSet

router = routers.DefaultRouter()

router.register(r'namelist', NamelistViewSet)