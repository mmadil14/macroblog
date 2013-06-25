from django.db import models

class Biodata(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    heading = models.CharField('Heading', max_length=255)
    content = models.TextField('Biodata ( Markdown Supported )', max_length=500, blank=True, default='')
    order = models.IntegerField('Ordering', unique=True)
    published = models.BooleanField('Do we publish it ?', default=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.heading

