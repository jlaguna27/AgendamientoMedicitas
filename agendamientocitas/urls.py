"""medicitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from agendamientocitas import settings

from django.views.generic import TemplateView
from citas.views import Viewcitamedica, Addcitamedica, Editcitamedica, Deletcitamedica, Vieweps, Addeps, Editeps, \
    Deleteps, Viewmedico, Addmedico, Editmedico, Deletmedico, Viewpaciente, Addpaciente, Editpaciente, Deletpaciente, \
    Viewprofile, Addprofile, Editprofile, Deletprofile, Viewuser, Deletuser, Edituser
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewcita/', Viewcitamedica.as_view(), name='viewcita'),
    path('addcita/', Addcitamedica.as_view()),
    path('editcita/<int:pk>/', Editcitamedica.as_view()),
    path('deletcita/<int:pk>/', Deletcitamedica.as_view()),
    path('vieweps/', Vieweps.as_view(), name='vieweps'),
    path('addeps/', Addeps.as_view()),
    path('editeps/<int:pk>/', Editeps.as_view()),
    path('deleteps/<int:pk>', Deleteps.as_view()),
    path('viewmedico/', Viewmedico.as_view(), name='viewmedico'),
    path('addmedico/', Addmedico.as_view()),
    path('editmedico/<int:pk>', Editmedico.as_view()),
    path('deletmedico/<int:pk>/', Deletmedico.as_view()),
    path('viewpaciente/', Viewpaciente.as_view(), name='viewpaciente'),
    path('addpaciente/', Addpaciente.as_view()),
    path('editpaciente/<int:pk>/', Editpaciente.as_view()),
    path('deletepaciente/<int:pk>', Deletpaciente.as_view()),
    path('viewprofile/', Viewprofile.as_view(), name='viewprofile'),
    path('addprofile/', Addprofile.as_view()),
    path('editprofile/<int:pk>/', Editprofile.as_view()),
    path('deletprofile/<int:pk>', Deletprofile.as_view()),
    path('viewuser/', Viewuser.as_view(), name='viewuser'),
    path('edituser/<int:pk>', Edituser.as_view()),
    path('deletuser/<int:pk>', Deletuser.as_view()),

    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
