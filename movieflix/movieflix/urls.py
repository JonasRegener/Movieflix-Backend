"""movieflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from movies.views import MovieViewSet
from movies.views import show_movie
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from user import views
router = routers.DefaultRouter()
router.register(r'movieAPI', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('movieST/<str:title>/', show_movie),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
   
    
    # path('login/', views.login),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

 # path('api-auth/', include('rest_framework.urls')),
 #"""  path('api-user-login/', UserLogIn.as_view()),
 #path('sign-up/', SignUp.as_view()), """
#""" re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)), """
#"""  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), """