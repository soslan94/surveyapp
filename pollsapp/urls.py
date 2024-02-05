from django.urls import path
from .views import SurveyList, result, vote


app_name = 'pollsapp'

urlpatterns = [
    path('', SurveyList.as_view(), name='index'),
    path('vote/<str:pk>', vote, name='vote'),
    path('result/<str:pk>', result, name='result')
]