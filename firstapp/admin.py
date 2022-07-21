from django.contrib import admin
#from firstapp.models import account
from firstapp.models import solofftournament, freefiredata, pubggdata, coddata, duofftournament, squadfftournament, paymentdata


# Register your models here.
#custom model for user account registration
##class accounts(admin.ModelAdmin):
##    list_display = ('name','mail','pass5')
##admin.site.register(account,accounts)
class tournament(admin.ModelAdmin):
    list_display = ('tittle','totalplayer','prize','time')
admin.site.register(solofftournament ,tournament)

class tournament(admin.ModelAdmin):
    list_display = ('tittle','totalplayer','prize','time')
admin.site.register(duofftournament ,tournament)

class tournament(admin.ModelAdmin):
    list_display = ('tittle','totalplayer','prize','time')
admin.site.register(squadfftournament ,tournament)

class ffdata(admin.ModelAdmin):
    admin.site.register(freefiredata)

class pubdata(admin.ModelAdmin):
    admin.site.register(pubggdata)

class coddata(admin.ModelAdmin):
    admin.site.register(coddata)

class paymentdata(admin.ModelAdmin):
    list_display = ('user','status','orderid','date')
    admin.site.register(paymentdata)