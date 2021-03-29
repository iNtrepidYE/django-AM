from django.urls import include, path
from django.contrib import admin
from AMapp.views import homepage,showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),

]
