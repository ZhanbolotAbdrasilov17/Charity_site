from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Props)
admin.site.register(Gallery)


@admin.register(About_page_text)
class About_page_textAdminList(admin.ModelAdmin):
    pass

@admin.register(About_us_mainpaig)
class About_us_mainpaigAdminList(admin.ModelAdmin):
    pass

@admin.register(HelpCase)
class HelpCaseAdminList(admin.ModelAdmin):
    pass

