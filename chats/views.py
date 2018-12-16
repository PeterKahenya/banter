from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User


class UsersList(View):
    def get(self,request):
        all_users=User.objects.exclude(username=request.user.username)
        return render(request,"home.html",{'users_list':all_users})

class MessageCreate(View):
    def get(self,request):
        pass
    
