from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#DJ Model
class Dj(models.Model):
    dj_id=models.AutoField(primary_key=True)
    dj_name=models.CharField(max_length=100)
    dj_email=models.EmailField(max_length=100)
    dj_website=models.URLField(max_length=100,default=None, null=True, blank=True)
    dj_image=models.FileField(upload_to='images',blank=True)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.dj_name
    class Meta:
        verbose_name_plural = 'DJS'

#Mixtape Model
class DjMixTape(models.Model):
    mix_tape_id=models.AutoField(primary_key=True)
    dj_id=models.ForeignKey(Dj,on_delete=models.CASCADE)
    mix_tape_title=models.CharField(unique=True,max_length=200)
    mix_tape_media_link=models.FileField(upload_to='videos',blank=True)
    mix_tape_tot_likes=models.IntegerField(default=0, null=True, blank=True)
    mix_tape_tot_views=models.IntegerField(default=0, null=True, blank=True)
    slug = AutoSlugField(populate_from='created_on,mix_tape_title', max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mix_tape_title
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'DJ Mix Tapes'

        def __unicode__(self):
            return self.mix_tape_title
