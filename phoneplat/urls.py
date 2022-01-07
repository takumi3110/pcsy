from django.urls import path

from rest_framework import routers

from . import views

app_name = 'phoneplat'

router = routers.DefaultRouter()
router.register(r'system', views.SystemViewSet)
router.register(r'phoneNumber', views.PhoneNumberViewSet)
router.register(r'surplusNumber', views.SurplusNumberViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'accessLine', views.AccessLineViewSet)
router.register(r'trank', views.TrankViewSet)
router.register(r'trankInfo', views.TrankInfoViewSet)
router.register(r'scenario', views.ScenarioViewSet)
router.register(r'payingService', views.PayingServiceViewSet)
router.register(r'incomingNumber', views.IncomingNumberViewSet)
router.register(r'payingCode', views.PayingCodeViewSet)
router.register(r'notification', views.NotificationViewSet)

urlpatterns = []
