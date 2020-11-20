"""deliverApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
#from deliverApp.views import home
app_name = (
    'food_area',
    'food_order',
    'food_items',
    'food_delivery',
    'food_providers',
    'food_newsletters',
    'food_user_profiles',
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),

    path('area/', include('food_area.urls')),
    path('order/',include('food_order.urls')),
    path('items/',include('food_items.urls')),
    path('delivery/',include('food_delivery.urls')),
    path('providers/',include('food_providers.urls')),
    path('users/', include('food_user_profiles.urls')),
    path('newsletter/',include('food_newsletters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__',include(debug_toolbar.urls)),
    ]+urlpatterns
    #]+urlpatterns


