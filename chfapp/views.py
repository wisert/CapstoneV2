#All views for the project are created in this page

from django.shortcuts import render
from .forms import UserLoginForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	# title = "Welcome"
	# if request.user.is_authenticated():
	title = "Welcome, %s" % (request.user)

	context = {
		"title": title,
	}

	return render(request,"home.html", context)

def userLogin(request):
	title = "Please sign in:"
	form = UserLoginForm(request.POST or None)

	#video 14/42 has alternate validation methods
	if form.is_valid():
		# print (request.POST['username'])
		instance = form.save(commit=False)
		instance.save()
		context = {
			"title":"Thank you." #does not yet take you to the user's dashboard
		}

	#parens create instance
	context = {
		"title": title,
		"form": form,
	}

	return render(request,"userLogin.html", context)



#test form from tutorials; email sending doesn't work yet
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print (key)
		# 	print (form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_first_name = form.cleaned_data.get("first_name")
		print (form_email)
		
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'courtney.llera@ymail.com']
		contact_message = "%s: %s via %s"%(
			form_first_name, 
			form_message, 
			form_email
			)
		send_mail (
			subject, 
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False
			)
		#have fail silently if you're doing it in prod

	context = {
		"form":form,
	}
	
	return render(request, "forms.html", context)

