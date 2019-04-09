from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory( models.Model ) :
	category = models.CharField( max_length = 200 )
	summary = models.CharField( max_length = 200 )
	slugs = models.CharField( max_length = 200 )

	class Meta  :
		verbose_name_plural = 'Categories'

	def __str__( self ) :
		return self.category

class TutorialSeries( models.Model ) :

	class Meta :
		verbose_name_plural = 'Tutorial Series'

	series = models.CharField( max_length = 200 )
	category = models.ForeignKey(TutorialCategory, default = 1, verbose_name = "Category", on_delete = models.SET_DEFAULT)
	summary = models.CharField( max_length = 200 )

	def __str__(self) :
		return self.series

class Tutorial( models.Model ) :
	tutorial_title = models.CharField( max_length = 50)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())
	tutorial_series = models.ForeignKey( TutorialSeries, default = 1, verbose_name = "Series", on_delete = models.SET_DEFAULT)
	slug = models.CharField( max_length = 200, default =  1 )

	def __str__(self) :
		return self.tutorial_title