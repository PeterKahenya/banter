from django.shortcuts import render,redirect
from django.views import View,generic
from django.contrib.auth.models import User
from .models import Message
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist


 
class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("/chats/")
        else:
            all_users_except_me=User.objects.exclude(username=request.user.username)
            return render(request,"home.html",{'users_list':all_users_except_me})

class ChatBox(View):
    def get(self,request,receiver=None):
        if request.user.is_authenticated:
            me=request.user
            if receiver is None:
                all_users_except_me=User.objects.exclude(username=me.username)
                return render(request,"chatbox.html",{'users_list':all_users_except_me})
            else:
                try:
                    to=User.objects.get(username=receiver)
                    query = Q(Q(sender=me)&Q(receiver=to))|Q(Q(sender=to)&Q(receiver=me))    
                    all_users_except_me=User.objects.exclude(username=me.username)   
                    messages = Message.objects.filter(query).order_by('timestamp')
                    return render(request,"chatbox.html",{'messages':messages,'receiver':to,'users_list':all_users_except_me})
                except ObjectDoesNotExist:
                    return redirect("/chats/")
        else:                    
            return redirect("/accounts/login/")

   
    def post(self,request,receiver):
            me=request.user
            to=User.objects.get(username=receiver)
            msg=request.POST.get("msg")
            msg_obj=Message.objects.create(sender=me,receiver=to,msg=msg)
            msg_obj.save()
            return redirect("/chats/"+receiver+"/")















class LiveChats(View):
    def get(self,request,receiver):
        to=User.objects.get(username=receiver)
        me=request.user
        query = Q(Q(sender=me)&Q(receiver=to))|Q(Q(sender=to)&Q(receiver=me))
        #messages = Message.objects.filter(query).order_by('-timestamp')
        messages =list(Message.objects.filter(query).order_by('timestamp'))
        qs_json = serializers.serialize('json', messages)
        return HttpResponse(qs_json, content_type='application/json')