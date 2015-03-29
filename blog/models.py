from django.db import models


class Article(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ARCHIVED = 'archived'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Disabled'),
        (ARCHIVED, 'Archived'),
        (DELETED, 'Deleted'),
    )

    title = models.CharField(max_length=100)
    lead = models.CharField(max_length=255)
    body = models.CharField(max_length=512)
    author = models.CharField(max_length=50, default="Anonymous", blank=True)
    img = models.CharField('Image URL', max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=ACTIVE)

    def __unicode__(self):
        return str(self.title)
