from django.urls import path
from . import views

urlpatterns = [

    path('view/', views.course_view, name="view"),
    path('create/', views.course_create, name="create"),
    path('delete/<int:id>', views.course_delete, name="delete"),
    path('edit/<int:id>', views.course_edit, name="edit"),
    path('status/<int:id>', views.change_status, name="status")

]
