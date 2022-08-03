
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render 
from firstapp.models import freefiredata ,pubggdata ,coddata
from  django.http import  HttpResponse ,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
from firstapp.models import solofftournament, duofftournament, squadfftournament, paymentdata
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
                'CALLBACK_URL':'http://127.0.0.1:8000/roomid',

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
            messages.sucess(request, "your payment was sucessfull")
            return HttpResponseRedirect('roomid')
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
            temp= User.objects.get(username = name)
            return HttpResponseRedirect('createaccount', messages.error(request, "username already exist"))  
        except Exception:
            pass
        #try:
        #    temp= User.objects.get(email = mail)
        #    messages.error(request, "mail already exist")
        #except Exception:
        #    pass 
        userlogin=User.objects.all()
        for userdata in userlogin:
            pass
            #print("yes")
        if userdata.email == mail : 
            messages.error(request, 'mail already exists')
        else:
            if pass1 != pass5 : 
                messages.error(request, 'password does not match')
            else:
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
        for ff in freefire:
            pass
        userlogin=User.objects.all()
        for userdata in userlogin:
            pass
        #payment = paymentdata.objects.all()
        #for paymentdataa in payment:
        #    print(paymentdataa.user)
        #    pass
        #if userdata.username == paymentdataa.user:
        #        messages.error(request, "You are already register this tournament")
        #else:
        if userdata.username == ff.ffid:
            print(ff.ffid)
            return HttpResponseRedirect('payment')
        else:
            messages.error(request, "First you need to register your ingame username with us")
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
            messages.error(request, "Email id and Password do not match.Please try again")
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

      #real code  
    freefireuserdata=freefiredata.objects.all()
    userlogin=User.objects.all()
    ffdata={
        'freefiredata':freefireuserdata,
        'userlogin':userlogin
    }
    if request.method =="POST":
        logout(request)
        return HttpResponseRedirect('home')
    return render(request, 'profile.html',ffdata)


def ffdata(request):
    if request.method =="POST":
        fname=request.POST["fname"]
        ffid=request.POST["ffid"]
        if request.user.is_authenticated:
           # print(request.user.username)
           pass
    freefire=freefiredata.objects.all()
    ffuserdata={
        'freefire':freefire
    }
    for abc in freefire:
        pass
    if abc.ffname == fname:
        messages.error(request, "This user data already registerd with us")
    else:
        if request.user.username == fname :
            fdata=freefiredata(ffname=fname, ffid=ffid)
            fdata.save()
        else: 
            messages.error(request, "username doesnot match") 

    return render(request, 'profile.html', ffuserdata)

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
        

def roomid(request):
    return render(request, 'roomid.html')