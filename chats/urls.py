from django.urls import path,include
from .views import UsersList,MessageCreate
urlpatterns=[
    path("",UsersList.as_view()),
    path("chats/",MessageCreate.as_view(),name="message_create")
]