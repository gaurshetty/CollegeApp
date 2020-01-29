
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('section.urls')),
    path('', include('allORM.urls')),
]
