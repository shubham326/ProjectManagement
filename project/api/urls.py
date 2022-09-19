from project.api import views
from django.urls import path

urlpatterns = [
    path('get/', views.api_project_view, name="get_list"),
    path('get/<int:pk>/', views.api_detail_project_view, name="detail"),
    path('delete/<int:pk>', views.api_delete_project_view, name="delete"),
    path('update/<int:pk>', views.api_update_project_view, name="update"),
    path('project', views.api_post_project_view, name="create"),

]