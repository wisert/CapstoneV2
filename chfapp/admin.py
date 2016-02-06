from django.contrib import admin

# Register your models here.
from .forms import UserLoginForm
from .models import UserForm, AdminForm

# class CreateAccountAdmin(admin.ModelAdmin):
# 	list_display=["__str__", "organization"]
# 	form = CreateAccountForm
	#class Meta:
	#	model=CreateAccount

class UserLoginAdmin(admin.ModelAdmin):
	list_distplay=["__str__", "username"]
	form = UserLoginForm


#admin.site.register(CreateAccount, CreateAccountAdmin)
admin.site.register(UserForm, UserLoginAdmin)