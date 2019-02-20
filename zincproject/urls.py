"""zincproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from events import views
from django.conf import settings
from django.conf.urls.static import static
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.event_list, name='homepage'),
    path('events/<int:event_id>/',
         views.event_detail, name='event-detail'),
    path('dashboard/', views.event_dashboard, name='event-dashboard'),
    path('events/<int:event_id>/booked/', views.booking, name='booked-event'),
   

    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('signup/', views.user_register, name='user-register'),
    path('events/create/', views.event_create, name='event-create'),
    path('events/<int:event_id>/delete/',
         views.event_delete, name='event-delete'),
    path('events/<int:event_id>/update/',views.event_update, name='event-update'),

    path('accounts/', include('allauth.urls')),

    path('noaccess/',views.noaccess ,name='no-access'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
