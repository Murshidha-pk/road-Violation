"""
URL configuration for roadviolation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from road import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/',views.SignUpView.as_view(),name="signup"),

    path('signin/',views.SignInView.as_view(),name="signin"),

    path('violation/add/',views.RoadViolationAddView.as_view(),name='violation-add'),

    path('violation/list/',views.ViolationListView.as_view(),name="violation-list"),

    path('violation/<int:pk>/remove',views.ViolationDeleteView.as_view(),name='delete'),

    path("violation/<int:pk>/change/",views.ViolationUpdateView.as_view(),name="update"),

    path("signout/",views.SignOutView.as_view(),name="signout"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
