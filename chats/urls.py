from django.urls import path,include
from .views import UsersList,ChatList,LiveChats
urlpatterns=[
    path("",UsersList.as_view()),
    path("chats/<slug:receiver>/",ChatList.as_view(),name="message_list"),
    path("livechats/<slug:receiver>/",LiveChats.as_view(),name="livechat"),
]