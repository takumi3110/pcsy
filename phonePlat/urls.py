from django.urls import path

from rest_framework import routers

from . import views

app_name = 'phonePlat'

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

urlpatterns = [
	path('', views.index, name='index'),
	path('service_list/', views.ServiceListView.as_view(), name='service_list'),
	path('service_detail/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
	path('service_update/<int:pk>', views.ServiceUpdateView.as_view(), name='service_update'),
	path('scenario_list/', views.ScenarioListView.as_view(), name='scenario_list'),
	path('scenario_detail/<int:pk>', views.ScenarioDetailView.as_view(), name='scenario_detail'),
	path('scenario_update/<int:pk>', views.ScenarioUpdateView.as_view(), name='scenario_update'),
	path('phone_number_list/', views.PhoneNumberListView.as_view(), name='phone_number_list'),
	path('phone_number_detail/<int:pk>', views.PhoneNumberDetailView.as_view(), name='phone_number_detail'),
	path('phone_number_update/<int:pk>', views.PhoneNumberUpdateView.as_view(), name='phone_number_update'),
	path('access_line_list/', views.AccessLineListView.as_view(), name='access_line_list'),
	path('access_line_detail/<int:pk>', views.AccessLineDetailView.as_view(), name='access_line_detail'),
	path('access_line_update/<int:pk>', views.AccessLineUpdateView.as_view(), name='access_line_update'),
	path('incoming_number_list/', views.IncomingNumberListView.as_view(), name='incoming_number_list'),
	path('incoming_number_detail/<int:pk>', views.IncomingNumberDetailView.as_view(), name='incoming_number_detail'),
	path('incoming_number_update/<int:pk>', views.IncomingNumberUpdateView.as_view(), name='incoming_number_update'),
	path('paying_code_list/', views.PayingCodeListView.as_view(), name='paying_code_list'),
	path('paying_code_detail/<int:pk>', views.PayingCodeDetailView.as_view(), name='paying_code_detail'),
	path('paying_code_update/<int:pk>', views.PayingCodeUpdateView.as_view(), name='paying_code_update')
]
