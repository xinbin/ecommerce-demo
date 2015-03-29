from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    carousel = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.name)


class Product(models.Model):
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

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    small_image = models.CharField(max_length=255)
    large_image = models.CharField(max_length=255)
    special = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=ACTIVE)

    def __unicode__(self):
        return str(self.name)
