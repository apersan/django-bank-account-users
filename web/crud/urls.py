from django.urls import path
from .views import *


urlpatterns = [
    path('', view_user_list, name="view_user_list"),
    path('view_user_list/', view_user_list, name="view_user_list"),
]
