from django.urls import path
from user.views import IndexView


urlpatterns = [
    path('',IndexView.as_view(),name="index" ),

]



