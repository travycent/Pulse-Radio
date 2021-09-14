from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
#class Live link
class LiveLink(models.Model):
    live_link_id=models.AutoField(primary_key=True)
    live_link_title=models.CharField(max_length=100)
    live_link_url=models.URLField(max_length=100)
    live_link_show_name=models.CharField(max_length=100, null=True, blank=True)
    live_link_host=models.CharField(max_length=100,null=True, blank=True)
    live_link_tot_likes=models.IntegerField(default=0, null=True, blank=True)
    live_link_tot_views=models.IntegerField(default=0, null=True, blank=True)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.live_link_title
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Live Links'

        def __unicode__(self):
            return self.live_link_title
#model Archives
class Archives(models.Model):
    archive_id=models.AutoField(primary_key=True)
    archive_title=models.CharField(unique=True,max_length=100)
    archive_url=models.FileField(upload_to='archives')
    archive_description=models.TextField( null=True, blank=True)
    archive_presenter=models.CharField( max_length=100,null=True, blank=True)
    archive_tot_likes=models.IntegerField(default=0, null=True, blank=True)
    archive_tot_views=models.IntegerField(default=0, null=True, blank=True)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.archive_title
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Archives'

        def __unicode__(self):
            return self.archive_title
#model Archives
class NewsBeats(models.Model):
    news_beat_id=models.AutoField(primary_key=True)
    news_beat_title=models.CharField(unique=True,max_length=100)
    news_beat_url=models.FileField(upload_to='videos',blank=True)
    news_beat_tot_likes=models.IntegerField(default=0, null=True, blank=True)
    news_beat_tot_views=models.IntegerField(default=0, null=True, blank=True)
    slug = AutoSlugField(populate_from='created_on,news_beat_title', unique=True,max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.news_beat_title
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'News Beats'

        def __unicode__(self):
            return self.news_beat_title
    
