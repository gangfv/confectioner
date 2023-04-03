from django.urls import path
from home.views import HomeListView, NumberCreteApi

urlpatterns = [
    path('', HomeListView.as_view()),
    path('feedback/', NumberCreteApi.as_view())
]
