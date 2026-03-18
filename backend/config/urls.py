"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.http import HttpResponse  # api endpoint __debug__/

def home(request):
    return JsonResponse({"message": "API is running"})

def test_view(request):
    return HttpResponse("Debug test page")


urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),

    path("api/auth/", include("apps.users.urls")),
    

    path("api/menu/", include("apps.menu.urls")),
    path("api/rooms/", include("apps.rooms.urls")),
    path("api/activities/", include("apps.activities.urls")),
    path("api/bookings/", include("apps.bookings.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/payments/", include("apps.payments.urls")),

    # Django debug tool
    path("__debug__/", include(debug_toolbar.urls)),

    # http://127.0.0.1:8000/test/
    path("test/", test_view),
]
