from django.urls import path
from .views import create_user,getstate,home,updatetask

urlpatterns = [

path('',home,name='home'),
path('create_users/',create_user,name='create_user'),
path('state/<task_id>/',getstate,name='get_state'),
path('state/<task_id>/<status>/',updatetask,name='update_task'),
]
