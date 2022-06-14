from email.message import Message
from venv import create
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render 
from firstapp.models import freefiredata
from  django.http import  HttpResponse ,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from firstapp.models import solofftournament


# Create your views here.
def home(request):
    
    #return HttpResponse("this is homepage")
    return render(request, 'home.html')
def signup(request):
    #return HttpResponse("this is homepage")
    if request.method=="POST":
        name=request.POST['name'] 
        mail=request.POST['mail']
        pass1=request.POST['pass1']
        pass5=request.POST['pass5']

        #form validation
        #userdata=User.objects.all()
        #for usermail in userdata:
        #    if mail != usermail:
        #        messages.error(request, "email already exist")
        try:
            #temp= account.objects.get(name=name)
            temp= User.objects.get(username=name)
            messages.success(request, "username already exist")
        except Exception:
            pass
        try:
            #temp= account.objects.get(name=name)
            temp= User.objects.get(mail=mail)
            return HttpResponse("username already exist")
        except Exception:
            pass 
        if pass1 != pass5:
            messages.error(request, 'password does not match')
        else:
            print(name ,mail ,pass5 )
            #createuseraccount.save()
            user=User.object.create_user(name, mail , pass5)
            user.save()
            return HttpResponseRedirect('thankyoupage') 
    return render(request, 'createaccount.html' )

   
def thank(request):
    return render(request, 'thankyoupage.html')

def tournament(request):
    #anonymous user
    #if request.user.is_anonymous:
    #    return HttpResponseRedirect('createaccount')
    #else:
    solo=solofftournament.objects.all()
    solodata={
        'solo':solo
    }
    return render(request, 'tournamentpage.html',solodata)

def aboutus(request):
    return render(request, 'aboutus.html')

def loginn(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        #userlogin=account.objects.all()
        #for logindata in userlogin:
            #      print(logindata.mail)
        User= authenticate(request, username = name, password = password)
        if User is not None:
            login (request, User)  
            print("yess") 
            return HttpResponseRedirect('profile')
        else:
            print("shii se likh n")
                #createuseraccount=authenticate(mail = logindata.mail, password = logindata.pass5)
                #if createuseraccount is not None:
                #accountt=authenticate(mail=logindata.mail, password=logindata.pass5)
                #login(request, accountt)
                #return HttpResponseRedirect('profile')
            #else:
                #print("nooooo")
                    #messages.error(request, "Please Enter Correct Details")
    return render(request, 'login.html')

def profile(request):
    if request.method =="POST":
        logout(request)
        messages.success(request,"your account sucessfully logout")
        return HttpResponseRedirect('login')
    return render(request, 'profile.html')


def ffdata(request):
    if request.method =="POST":
        ffname=request.POST["ffname"]
        ffid=request.POST["ffid"]
        ffdata=freefiredata(ffname=ffname,ffid=ffid)
        ffdata.save()
        if ffdata.save:
          print("yes")
    return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')

#def loggout(request):
#    if request.method =="POST":
#        logout(request)
#        messages.success(request,"your account sucessfully logout")
#        return HttpResponseRedirect('contact')
#    return render(request, 'logout.html')
        