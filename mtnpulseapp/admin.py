from django.contrib import admin
from .models import Dj,DjMixTape,LiveLink,Archives

#Display the DJ Data in a Tabular Format at the Admin End
class DJAdmin(admin.ModelAdmin):
    list_display= ('dj_name', 'dj_email', 'dj_website','dj_image')#Display Data in A List
    search_fields = ('dj_name', 'dj_email')#Add A search Field
class DJMixtapeAdmin(admin.ModelAdmin):
    list_display= ('mix_tape_title', 'mix_tape_media_link','mix_tape_tot_likes','mix_tape_tot_views','slug','created_on')#Display Data in A List
    search_fields = ('mix_tape_title','slug')#Add A search Field
class LiveLinkAdmin(admin.ModelAdmin):
    list_display= ('live_link_title', 'live_link_url', 'created_on')#Display Data in A List
    search_fields = ('live_link_title', 'live_link_url')#Add A search Field
class ArchivesAdmin(admin.ModelAdmin):
    list_display= ('archive_id', 'archive_title','archive_url', 'created_on')#Display Data in A List
    search_fields = ('archive_title', 'archive_url')#Add A search Field
# Register DJ Model and Display the Data in a Tabular Format.
admin.site.register(Dj,DJAdmin)
admin.site.register(DjMixTape,DJMixtapeAdmin)
admin.site.register(LiveLink,LiveLinkAdmin)
admin.site.register(Archives,ArchivesAdmin)


