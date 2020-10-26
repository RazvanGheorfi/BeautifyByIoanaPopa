from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class hyaluronGalleryClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    alt_field = models.CharField(max_length=50)
    images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class hyaluronDetailsClass(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title

class makeupGalleryClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    alt_field = models.CharField(max_length=50)
    images = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


class makeupDetailsClass(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


class laminareGalleryClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    alt_field = models.CharField(max_length=50)
    images = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


class laminareDetailsClass(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


class geneGalleryClass(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    alt_field = models.CharField(max_length=50)
    images = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title


class geneDetailsClass(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title

class aboutPage(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title

class contactPage(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    
    def __str__(self):
        return self.title