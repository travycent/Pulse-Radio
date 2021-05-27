from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
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
    def __str__(self):
        return self.dj_name

#Mixtape Model
class DjMixTape(models.Model):
    mix_tape_id=models.AutoField(primary_key=True)
    dj_id=models.ForeignKey(Dj,on_delete=models.CASCADE)
    mix_tape_title=models.CharField(max_length=200)
    mix_tape_media_link=models.FileField(upload_to='videos',blank=True)
    mix_tape_tot_likes=models.IntegerField(default=None, null=True, blank=True)
    mix_tape_tot_views=models.IntegerField(default=None, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.mix_tape_title
    def get_absolute_url(self):
        return reverse('mix_tape_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.mix_tape_title)
        super(DjMixTape, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.mix_tape_title
#class Live link
class LiveLink(models.Model):
    live_link_id=models.AutoField(primary_key=True)
    live_link_title=models.CharField(max_length=100)
    live_link_url=models.URLField(max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.live_link_title
    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.live_link_title
#model Archives
class Archives(models.Model):
    archive_id=models.AutoField(primary_key=True)
    archive_title=models.CharField(max_length=100)
    archive_url=models.FileField(upload_to='archives')
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.archive_title
    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.archive_title
    
