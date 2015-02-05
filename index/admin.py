from django.contrib import admin
from index.models import Pages


# Register your models here.

class OutputInline(admin.TabularInline):
	model = Pages
	extra = 1

class InputAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,     {'fields': ['Input_text']})
	]
	inlines = [OutputInline]

admin.site.register(Pages)

	