"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from cmath import log
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from items import views
from django.conf.urls import include
from items.views import register_request, login_request, logout_request, MoreItemViews, MoreUserViews


router = routers.DefaultRouter()
router.register(r'items', views.ItemView, 'item')
router.register(r'users', views.UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path(r'^users/', include('items.urls')),
    path('register/', register_request),
    path('login/', login_request),
    path('', login_request),
    path('logout/', logout_request),
    # path('api/item-manipulations/<int:id>', MoreItemViews.as_view()),
    # path('api/user-manipulations/<int:id>', MoreUserViews.as_view()),
    # path('api/items/', MoreItemViews.as_view()),
    # path('api/items/<int:id>', views.ItemView)
    path('api/v1/items/', views.item_list),
    path('api/v1/items/<int:pk>', views.item_details),
    path('api/v1/match/<int:pk>', views.item_match),
    path('api/v1/match/', views.match),
    path('api/v1/match1/', views.match1),
    path('api/v1/User/<int:pk>',views.matchUUser)
]
