
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('board/', include('Bullboard.urls')),
    #path('ckeditor/', include('ckeditor_uploader.urls')),

]
