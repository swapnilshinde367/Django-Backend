from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from . forms import NewUserForm


# Create your views here.
# def homepage( request ) :
# 	return render( request=request, template_name = 'main/homepage.html', \
# 					context = {"tutorials" : Tutorial.objects.all} )

def homepage( request ) :
	return render( request = request, template_name = "main/categories.html", \
		context = { "categories" : TutorialCategory.objects.all})

def single_slug( request, single_slug ) :
	categorie_slugs = [c.slugs for c in TutorialCategory.objects.all()]
	if single_slug in categorie_slugs :

		matching_series = TutorialSeries.objects.filter( category__slugs = single_slug )
		series_urls = {}
		for m in matching_series.all() :
			part_one = Tutorial.objects.filter(tutorial_series__series = m.series).earliest("tutorial_published")
			series_urls[m] = part_one.slug

		return render( request = request, template_name = "main/category.html", context = { 'part_ones' : series_urls } )

	tutorial_slugs = [t.slug for t in Tutorial.objects.all()]
	if single_slug in tutorial_slugs :
		tutorial = Tutorial.objects.get( slug = single_slug )
		tutorials_from_same_series = Tutorial.objects.filter(tutorial_series__series = tutorial.tutorial_series).order_by("tutorial_published")
		active_tutorial_id = list(tutorials_from_same_series).index(tutorial)
		return render( request = request,
						template_name = "main/tutorial.html",
						context = { 'tutorial' : tutorial,
									'tutorials_from_same_series' : tutorials_from_same_series,
									'active_tutorial_id' : active_tutorial_id } )

	return HttpResponse( f"{single_slug} was nowhere to be found!!" )

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