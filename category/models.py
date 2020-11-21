import os
import uuid

from django.db import models



from django.utils.translation import ugettext_lazy as _
from .utils import get_unique_slug


class Category(models.Model):

    a='Active'
    i='Inactive'

    STATUS_CHOICES = (
        (a, _("Active")),
        (i, _("Inactive")),
    )

    parent = models.ForeignKey('self',blank=True, null=True, related_name='children',on_delete=models.CASCADE)  # on_delete=DO_NOTHING
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True,null=True)
    # image = models.ImageField(upload_to='upload/category/')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default=a)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('parent',)    #enforcing that there can not be two
    #     verbose_name_plural = "categories"       #categories under a parent with same slug


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)


    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of       # __str__ if you are using python 2
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])










