from django.contrib import admin

# Register your models here.
from .forms import CreateAccountForm
from .models import CreateAccount

class CreateAccountAdmin(admin.ModelAdmin):
	list_display=["__str__", "organization"]
	form = CreateAccountForm
	#class Meta:
	#	model=CreateAccount


admin.site.register(CreateAccount, CreateAccountAdmin)