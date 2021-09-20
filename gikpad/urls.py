from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/register/', views.registration, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('about',views.about,name = 'about'),
    path('services',views.services,name = 'services'),
    path('contacts',views.contacts,name = 'contacts'),
    path('advance',views.advance,name = 'advance'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)