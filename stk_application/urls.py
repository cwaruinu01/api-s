from django.contrib import admin
from django.urls import path
from stk_application import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('application/', views.application_list),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
