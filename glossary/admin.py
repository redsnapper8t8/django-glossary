from django.contrib import admin
from glossary.models import Term, Synonym

class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title']}

class SynonymAdmin(admin.ModelAdmin):
    pass

admin.site.register(Term, TermAdmin)
admin.site.register(Synonym, SynonymAdmin)