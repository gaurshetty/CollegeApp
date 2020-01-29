from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('book/', views.home_book),
    path('book/save/', views.save_update_book),
    path('book/edit/<int:id>', views.edit_book),
    path('book/delete/<int:id>', views.delete_book),

    path('author/', views.home_author),
    path('author/save/', views.save_update_author),
    path('author/edit/<int:id>', views.edit_author),
    path('author/delete/<int:id>', views.delete_author),

    path('publication/', views.home_publication),
    path('publication/save/', views.save_update_publication),
    path('publication/edit/<int:id>', views.edit_publication),
    path('publication/delete/<int:id>', views.delete_publication),

    path('address/', views.home_address),
    path('address/save/', views.save_update_address),
    path('address/edit/<int:id>', views.edit_address),
    path('address/delete/<int:id>', views.delete_address),
]
