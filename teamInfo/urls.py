from django.urls import path

from rest_framework import routers

from . import views

app_name = 'teamInfo'

router = routers.DefaultRouter()
router.register(r'site', views.SiteViewSet)
router.register(r'tenant', views.TenantViewSet)
router.register(r'team', views.TeamViewSet)
router.register(r'dept', views.DeptViewSet)

urlpatterns = []
