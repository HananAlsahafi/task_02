
from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='hanan'),

]
