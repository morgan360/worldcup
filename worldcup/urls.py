from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("stats.urls")),
    path("films/", include("films.urls")),
    path("student/", include("student.urls")),
]
