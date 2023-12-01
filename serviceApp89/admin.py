from django.contrib import admin

# Register your models here.

from .models import Doc,DocImg


class DocImgInline(admin.StackedInline):
    model = DocImg
    extra = 1


class DocAdmin(admin.ModelAdmin):
    inlines = [DocImgInline,]



admin.site.register(Doc,DocAdmin)
#admin.site.register(DocImg)
