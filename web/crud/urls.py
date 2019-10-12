from django.urls import path
from .views import *


urlpatterns = [
    path('', view_user_list, name="view_user_list"),
    path('view_user_list/', view_user_list, name="view_user_list"),
    path('add_user/', add_user, name="add_user"),
    path('edit_user/<int:pk>', edit_user, name="edit_user"),
    path('delete_user/<int:pk>', delete_user, name="delete_user"),
]
