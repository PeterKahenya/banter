from django.urls import path,include
from .views import ChatBox,LiveChats,HomeView
urlpatterns=[
    path("",HomeView.as_view()),
    path("chats/",ChatBox.as_view()),
    path("chats/<slug:receiver>/",ChatBox.as_view(),name="message_list"),
    path("livechats/<slug:receiver>/",LiveChats.as_view(),name="livechat"),
]