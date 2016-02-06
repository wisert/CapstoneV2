from django.shortcuts import render
from .forms import CreateAccountForm

# Create your views here.
def home(request):
	# title = "Welcome"
	# if request.user.is_authenticated():
	title = "Welcome, %s" % (request.user)
	form = CreateAccountForm(request.POST or None)

	#parens create instance
	context = {
		"title": title,
		"form": form,
	}

	#video 14/42 has alternate validation methods
	if form.is_valid():
		# print (request.POST['email'])
		instance = form.save(commit=False)
		instance.save()
		context = {
			"title":"Thank you."
		}

	return render(request,"home.html", context)