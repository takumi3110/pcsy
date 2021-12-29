from django.contrib import admin
from django.urls import path, include

from phoneplat.urls import router as phoneplat_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/phoneplat/', include(phoneplat_router.urls))
]
