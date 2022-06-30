from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render 
from firstapp.models import freefiredata ,pubggdata ,coddata
from  django.http import  HttpResponse ,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from firstapp.models import solofftournament, duofftournament, squadfftournament
from firstapp.paytm import Checksum
import random
from django.views.decorators.csrf import csrf_exempt



MERCHANT_KEY='FQvE9GodDFIW5vIT'
MERCHANT_ID='aRRQGx94100136444263'

# Create your views here.
def landingpage(request):
    return render(request, 'landpage.html')


def payment(request):
    if request.method=="POST":
        param_dict = {

                'MID': MERCHANT_ID,
                'ORDER_ID': str(random.randint(9999,99999)),
                'TXN_AMOUNT': str(10),
                'CUST_ID' : "balisc04@gmail.com",
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/order',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY, )
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'payment.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
          #  return HttpResponseRedirect('order')
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'order.html', {'response': response_dict})


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
            return HttpResponse("username exists")
            messages.success(request, "username already exist")
        except Exception:
            pass
        try:
            #temp= account.objects.get(name=name)
            temp= User.objects.get(email=mail)
            return HttpResponse("mail already exist")
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
                return HttpResponseRedirect('payment')
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
        