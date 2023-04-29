from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='Main.html'), name='home'),
    path('users/', include('films.urls')),
    path('about', views.about),
    path('sign', views.sign),
    path('login', views.login),

]
