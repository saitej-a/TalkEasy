from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.home,name='home'),
    path('messages/<str:pk>/',views.home,name='messages'),
    path('getMessages/<str:pk>/',views.getMessages,name="getmessages"),
    path('send',views.send,name='send'),
    path('search/',views.search,name='search'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('new-chat/<str:pk>/',views.new_chat,name="newchat"),
    path('signup/',views.reg,name='reg'),
    path('signin/',views.signin,name='login'),
    path('logout/',views.logOut,name='logout'),

]
urlpatterns+=staticfiles_urlpatterns()