from django.contrib import admin
from .models import Form

# this class inherits from the method 'admin' of the class 'ModelAdmin
class FormAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'email') # display this information for in candidate
    search_fields = ('first_name', 'last_name', 'email') # apply a search field bar to search for candidates
    list_filter = ('date', 'occupation') # apply a filter to the admin site
    ordering = ('first_name', ) # display names in alphabetical order
    readonly_fields = ('occupation', ) # let this field be read only, make it uneditable


admin.site.register(Form, FormAdmin)
