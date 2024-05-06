from django.urls import path
from .import views


urlpatterns = [
    path('mpesa/', views.mpesa, name='mpesa'),
    path('application/', views.application_list, name='application_list'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
