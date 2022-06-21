
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render 
from firstapp.models import freefiredata ,pubggdata ,coddata
from  django.http import  HttpResponse ,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from firstapp.models import solofftournament, duofftournament, squadfftournament


# Create your views here.
def landingpage(request):
    return render(request, 'landpage.html')


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
            user=User.objects.create_user(name, mail , pass5,)
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
    duo=duofftournament.objects.all()
    squad=squadfftournament.objects.all()
    solodata={
        'solo':solo,
        'duo':duo,
        'squad':squad
    }
    if request.method == "POST":
        freefire=freefiredata.objects.all()
        ff={
            'freefire':freefire
        }
        for fff in freefire:
            print(fff.ffid)
            if fff.ffid is not None:
                return HttpResponse("hogya")
        else:
            return HttpResponseRedirect('profile')
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
    freefire=freefiredata.objects.all()
    ffdata={
        'freefire':freefire
    }
    if request.method =="POST":
        logout(request)
        messages.success(request,"your account sucessfully logout")
        return HttpResponseRedirect('login')
    return render(request, 'profile.html',ffdata)


def ffdata(request):
    if request.method =="POST":
        ffnamee=request.POST["fname"]
        ffid=request.POST["ffid"]
        if request.user.is_authenticated:
            print(request.user.username)
            if request.user.username == ffnamee:
                print(ffnamee)
                fdata=freefiredata(ffname=ffnamee, ffid=ffid)
                fdata.save()
            else:
                return HttpResponse("chl n")
    freefire=freefiredata.objects.all()
    ff={
        'freefire':freefire
    }
    return render(request, 'profile.html',ff)

def pubgdata(request):
    if request.method =="POST":
        pubgnamee=request.POST["pubgname"]
        pubgidd=request.POST["pubgid"]
        if request.user.is_authenticated:
            print(request.user.username)
            if request.user.username == pubgnamee:
                print(pubgnamee)
                pubgdataa=pubggdata(pubgname=pubgnamee,pubgid=pubgidd)
                pubgdataa.save()
            else:
                return HttpResponse("chl n")
    return render(request, 'profile.html')

def callofdutydata(request):
    if request.method =="POST":
        codnamee=request.POST["codname"]
        codid=request.POST["codid"]
        if request.user.is_authenticated:
            print(request.user.username)
            if request.user.username == codnamee:
                print(codnamee)
                coddataa=coddata(codname=codnamee, codid=codid)
                coddataa.save()
            else:
                return HttpResponse("chl n")
    return render(request, 'profile.html')


def contact(request):
    return render(request, 'contact.html')

#def loggout(request):
#    if request.method =="POST":
#        logout(request)
#        messages.success(request,"your account sucessfully logout")
#        return HttpResponseRedirect('contact')
#    return render(request, 'logout.html')
        