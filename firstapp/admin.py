from django.contrib import admin
#from firstapp.models import account
from firstapp.models import solofftournament

# Register your models here.
#custom model for user account registration
##class accounts(admin.ModelAdmin):
##    list_display = ('name','mail','pass5')
##admin.site.register(account,accounts)
class tournament(admin.ModelAdmin):
    list_display = ('tittle','totalplayer','prize','time')
admin.site.register(solofftournament ,tournament)