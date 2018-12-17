from django.shortcuts import render,redirect
from django.views import View,generic
from django.contrib.auth.models import User
from .models import Message
from django.http import HttpResponse
from django.db.models import Q

 
 

class UsersList(View):
    def get(self,request):
        all_users_except_me=User.objects.exclude(username=request.user.username)
        return render(request,"home.html",{'users_list':all_users_except_me})


class ChatList(View):
    def get(self,request,receiver):
        to=User.objects.get(username=receiver)
        me=request.user
        query = Q(Q(sender=me)&Q(receiver=to))|Q(Q(sender=to)&Q(receiver=me))
        #messages = Message.objects.filter(query).order_by('-timestamp')
        messages = Message.objects.filter(query).order_by('timestamp')
        return render(request,"chatbox.html",{'messages':messages,'receiver':to})

    def post(self,request,receiver):
        me=request.user
        to=User.objects.get(username=receiver)
        msg=request.POST.get("msg")
        msg_obj=Message.objects.create(sender=me,receiver=to,msg=msg)
        msg_obj.save()
        return redirect("/chats/"+receiver+"/")
