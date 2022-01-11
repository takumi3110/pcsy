from django.urls import path

from rest_framework import routers

from . import views

app_name = 'line'

router = routers.DefaultRouter()
router.register(r'career', views.CareerViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'contractNumber', views.ContractNumberViewSet)
router.register(r'parentNumber', views.ParentNumberViewSet)

urlpatterns = []
