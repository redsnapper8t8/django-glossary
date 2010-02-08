from django.db import models

class Term(models.Model):
    PERSON_TYPE = 1
    STYLE_TYPE = 2
    PHILOSOPHY_TYPE = 3
    TYPE_CHOICES = (
        (PERSON_TYPE, 'Person'),
        (STYLE_TYPE, 'Style'),
        (PHILOSOPHY_TYPE, 'Philosopy'),
    )
    title = models.CharField(max_length=250, unique=True)
    ipa = models.CharField(max_length=250, unique=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, blank=True)

    class Meta:
        ordering = ['title']

    @models.permalink
    #def get_absolute_url(self):
    #   return ('glossary_detail', (), {'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term  = models.ForeignKey(Term, related_name="synonyms")

    def __unicode__(self):
        return u"%s (synonym for %s)" % (self.title, self.term.title)
