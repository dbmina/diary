from django.urls import path
from diary import views

app_name='diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), 
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit', views.edit, name='edit'), 
    path('<int:id>/update/', views.update, name='update'), 
    path('<int:id>/delete/', views.delete, name='delete'), # add this line
]