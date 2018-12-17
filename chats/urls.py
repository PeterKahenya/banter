from django.urls import path,include
from .views import UsersList,ChatList
urlpatterns=[
    path("",UsersList.as_view()),
    path("chats/<slug:receiver>/",ChatList.as_view(),name="message_list"),
]