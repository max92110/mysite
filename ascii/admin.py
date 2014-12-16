from django.contrib import admin
from ascii.models import Input, Type, Output

class OutputInline(admin.TabularInline):
	model = Output
	extra = 1

class InputAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,     {'fields': ['Input_text']})
	]
	inlines = [OutputInline]

admin.site.register(Input, InputAdmin)
#admin.site.register(Output)
#admin.site.register(Type)

