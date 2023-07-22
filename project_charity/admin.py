from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Props)
admin.site.register(Gallery_1)
admin.site.register(Gallery_2)
admin.site.register(Gallery_3)
admin.site.register(Gallery_4)
admin.site.register(Gallery_5)
admin.site.register(Gallery_6)
admin.site.register(Gallery_7)
admin.site.register(Gallery_8)
admin.site.register(Gallery_9)
admin.site.register(Gallery_10)
admin.site.register(Gallery_11)
admin.site.register(Gallery_12)



@admin.register(About_page_text)
class About_page_textAdminList(admin.ModelAdmin):
    pass

@admin.register(About_us_mainpaig)
class About_us_mainpaigAdminList(admin.ModelAdmin):
    pass

@admin.register(HelpCase)
class HelpCaseAdminList(admin.ModelAdmin):
    pass

