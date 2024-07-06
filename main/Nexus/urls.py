from django.urls import path
from . import views

app_name = 'Nexus'
urlpatterns = [
    path('',views.Nexus_list,name='nexus_list'),
    path('create/',views.Nexus_create,name='nexus_create'),
    path('<int:nex_id>/edit/',views.Nexus_edit,name='nexus_edit'),
    path('<int:nex_id>/delete/',views.Nexus_delete,name='nexus_delete'),
    path('register/',views.register,name='register'),
    # path('register/',views.register,name='register'),


]