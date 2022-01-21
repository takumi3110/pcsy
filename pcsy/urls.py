from django.contrib import admin
from django.urls import path, include

from phonePlat.urls import router as phoneplat_router
from teamInfo.urls import router as teaminfo_router
from line.urls import router as line_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/phonePlat/', include(phoneplat_router.urls)),
    path('api/v1/teamInfo/', include(teaminfo_router.urls)),
    path('api/v1/line/', include(line_router.urls)),
    path('', include('phonePlat.urls'))
]
