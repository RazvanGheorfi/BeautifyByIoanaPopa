from django.contrib import admin

from .models import hyaluronGalleryClass, hyaluronDetailsClass, makeupDetailsClass, makeupGalleryClass, geneDetailsClass, geneGalleryClass, laminareDetailsClass, laminareGalleryClass, contactPage, aboutPage
# Register your models here.

class hyaluronGalleryClassAdmin(admin.ModelAdmin):
    list_display = ("title", "date_published")


class makeupGalleryClassAdmin(admin.ModelAdmin):
    list_display = ("title", "date_published")


class geneGalleryClassAdmin(admin.ModelAdmin):
    list_display = ("title", "date_published")


class laminareGalleryClassAdmin(admin.ModelAdmin):
    list_display = ("title", "date_published")

    
admin.site.register(hyaluronGalleryClass,hyaluronGalleryClassAdmin)
admin.site.register(hyaluronDetailsClass)
admin.site.register(makeupDetailsClass)
admin.site.register(makeupGalleryClass, makeupGalleryClassAdmin)
admin.site.register(geneDetailsClass)
admin.site.register(geneGalleryClass, geneGalleryClassAdmin)
admin.site.register(laminareDetailsClass)
admin.site.register(laminareGalleryClass, laminareGalleryClassAdmin)
admin.site.register(aboutPage)
admin.site.register(contactPage)
