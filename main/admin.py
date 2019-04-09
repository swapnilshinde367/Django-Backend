from django.contrib import admin
from . models import Tutorial, TutorialCategory, TutorialSeries
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class TutorialAdmin( admin.ModelAdmin ) :
	# fields = ["tutorial_title", "tutorial_published", "tutorial_content" ]
# Not necessary, but recommendedto have different sections
	fieldsets = [
		("Title/Date", {"fields":["tutorial_title","tutorial_published"]}),
		("URL" , {"fields" : ["slug"] }),
		("Series", {"fields" : ["tutorial_series"]}),
		("Content", {"fields":["tutorial_content"]}),
	]
	formfield_overrides = {
		models.TextField : { 'widget' : TinyMCE() }
	}

admin.site.register( TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)