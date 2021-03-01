from django.contrib import admin
from .models import page
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','update_date')
	ordering = ('title',)
	search_fields = ('title',)
#Add this in to make content easier to write!
class GraphAdmin(admin.ModelAdmin):
	fields = ["title",
			  "permalink",
			  "update_date",
			  "bodytext"]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(page, GraphAdmin)