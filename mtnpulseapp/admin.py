from django.contrib import admin
from .models import LiveLink,Archives,NewsBeats
#Register all Models
class LiveLinkAdmin(admin.ModelAdmin):
    list_display= ('live_link_title', 'live_link_url', 'created_on')#Display Data in A List
    search_fields = ('live_link_title', 'live_link_url')#Add A search Field
class ArchivesAdmin(admin.ModelAdmin):
    list_display= ('archive_id', 'archive_title','archive_url', 'created_on')#Display Data in A List
    search_fields = ('archive_title', 'archive_url')#Add A search Field
class NewsBeatsAdmin(admin.ModelAdmin):
    list_display= ('news_beat_id', 'news_beat_title','news_beat_url', 'created_on')#Display Data in A List
    search_fields = ('news_beat_title', 'news_beat_url')#Add A search Field
#Register Models
admin.site.register(LiveLink,LiveLinkAdmin)
admin.site.register(Archives,ArchivesAdmin)
admin.site.register(NewsBeats,NewsBeatsAdmin)


