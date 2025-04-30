from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views

urlpatterns = [

    path('student/', StudentAPI.as_view()),
    # path('', home),
    # path('student/', post_student),
    # path('update-student/<id>/', update_student),
    path('get-book/', get_book),
    path('api-token-auth/', views.obtain_auth_token),
]
