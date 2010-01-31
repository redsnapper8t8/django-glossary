from django.conf.urls.defaults import *
from glossary.models import Term

terms = Term.objects.all()

urlpatterns = patterns('',
    url(r'^$', 'glossary.views.term_list', {"paginate_by": 20}),
    url(r'^(?P<slug>[-\w]+)/$','django.views.generic.list_detail.object_detail',
        {"queryset": terms, 'template_object_name': 'term'}),
)