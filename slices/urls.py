
from django.urls import path, include
from slices import views

from slices.views import MemberListAPI, home

#TODO: list view
urlpatterns = [
  path('home/', views.home, name="home"), 
  path('pay_now/<int:pk>', views.payment_view, name="pay"),
  path('api/articles/list/', MemberListAPI.as_view(), name='api_Member_list'),


  
]
