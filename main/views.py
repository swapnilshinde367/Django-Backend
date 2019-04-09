from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Tutorial
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from . forms import NewUserForm

# Create your views here.
def homepage( request ) :
	return render( request=request, template_name = 'main/homepage.html', \
					context = {"tutorials" : Tutorial.objects.all} )

def register( request ) :

	if request.method == "POST" :
		form = NewUserForm(request.POST)

		if form.is_valid() :
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success( request, f"Account created for :  {username}" )
			login(request, user )
			messages.info( request, f"Logged in as : {username}" )
			return redirect("main:homepage")
		else :
			for error in form.error_messages :
				messages.error(request, f"{error} : {form.error_messages[error]}")

	form = NewUserForm()
	return render( request = request, template_name = "main/register.html", \
					context = { "form" : form } )

def logout_request( request ) :
	logout(request)
	messages.info( request, "Logged Out" )
	return redirect("main:homepage")

def login_request( request ) :

	if request.method == 'POST' :
		form = AuthenticationForm( request, data = request.POST )
		if form.is_valid() :
			username = form.cleaned_data.get( 'username' )
			password = form.cleaned_data.get( 'password' )
			user = authenticate( username=username, password=password)
			if user != None :
				login(request, user)
				messages.success( request, f"Welcome back {username}!" )
				return redirect( "main:homepage" )
		else :
			for error in form.error_messages :
				messages.error( request, f"{error} : {form.error_messages[error]}" )

	form = AuthenticationForm()
	return render( request = request, template_name = "main/login.html", \
					context = { 'form' : form } )