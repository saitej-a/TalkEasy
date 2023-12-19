from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Messages,Chat
from django.db.models import Q
from django.http import HttpResponse,JsonResponse

# Create your views here.
q=""
def home(request,pk=None):
    
    if request.user.is_authenticated :
        
            
        
        users=Chat.objects.filter(Q(sender=request.user)|Q(host=request.user))
        name=[]
        for i in users:
            if str(i.sender.username)==str(request.user):
                name.append({"naam":i.host.username,"id":i.id})
            else :
                name.append({'naam':i.sender.username,'id':i.id})
        # if str(chat.sender)==str(request.user):
        #     name=str(chat.host)
        # else:
        #     name=chat.sender
        print(name)
        user='TalkEasy'


        
        if pk!=None:
            
            chat=Chat.objects.get(id=pk)
            
            body=chat.messages_set.all()
            count=len(body)
            chat=chat.id
            return render(request,"home.html",{'msgs':body,'chat':chat,'users':users,'count':count,'name':name})
            
        
        return render(request,'home.html',{'users':users,'user_msg':user,'name':name})
    else :
        
        return redirect('login')
page='reg'
def reg(request):
    
    page='reg'
    form=UserCreationForm()
    if request.method=='POST':
        try:
            username1=request.POST.get('username')
        except:
            username1=None
        if username1!=None:
            
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        
    return render(request,'registration.html',{'form':form,'page':page})
def signin(request):
    page='login'
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            print("doesn't exists")
        user=authenticate(request,username=username,password=password)
        try:
            login(request,user=user)
            return redirect('home')
        except:
            print("something went wrong")
    return render(request,'registration.html',{'page':page})
def logOut(request):
    logout(request)
    return redirect('home')

def messages(request,pk):
    chat=Chat.objects.get(id=pk)
    
    
def search(request):
    searched=None
    q=request.GET.get('q') if request.GET.get('q')!=None else ""
    searched=User.objects.filter(
        Q(username__icontains=q)
    )
    if request.method=='POST':
        q=request.GET.get('q') if request.GET.get('q')!=None else ""
        searched=User.objects.filter(
            Q(username__icontains=q)
        )
    return render(request,'searched.html',{'searched':searched})
def send(request):
    body=request.POST["body"]
    chat_id=request.POST["chat"]
    receiver=''
    con=Chat.objects.get(id=chat_id)
    if str(con.sender.username)==str(request.user):
        receiver=User.objects.get(username=con.host.username)
    elif str(con.host.username)==str(request.user):
        receiver=User.objects.get(username=con.sender.username)
    
    
    new_msg=Messages.objects.create(
        body=body,
        chat=con,
        sender=request.user,
        reciever=receiver
        
        
        )
    
    new_msg.save()
    return HttpResponse("message sent")

def getMessages(request,pk):
    chat=Chat.objects.get(id=pk)
    
    body=Messages.objects.filter(chat=chat).order_by('updated','created')
    user_id=User.objects.get(username=request.user)
    username=""
    user_id=user_id.id
    if chat.sender.id==user_id:
        username=chat.host.username
    else:
        username=chat.sender.username
    # chat=Chat.objects.filter(id=pk)
    
    return JsonResponse({"messages":list(body.values()),'user_id':user_id,'username':username})
def profile(request,pk):
    q=request.GET.get('q') if request.GET.get('q')!=None else ""
    prof=User.objects.get(id=pk)
    return render(request,'profile.html',{'prof':prof})
def new_chat(request,pk):
    
    # if :
    #     print(chat)
    #     return redirect('home')

    
    # else:
    up,created=Chat.objects.get_or_create(host=request.user,sender=User.objects.get(username=pk))
    
    if created:
        return redirect('home')
    else:
        return redirect('messages',pk=up.id)
    
        
        