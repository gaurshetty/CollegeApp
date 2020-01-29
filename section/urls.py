from django.conf.urls import url
from django.urls import path
from .views import Studentops
from . import views

urlpatterns = [
    # path('', views.home),
    # path('save/', views.save_update),
    # path('edit/<int:id>', views.edit),
    # path('delete/<int:id>', views.delete),
    url('', Studentops.as_view(), name='stud-ops'),
]
