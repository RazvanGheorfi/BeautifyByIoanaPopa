from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hyaluron-gallery', views.hyaluronGallery, name='hyaluron-gallery'),
    path('hyaluron-details', views.hyaluronDetails, name='hyaluron-details'),
    path('makeup-gallery', views.makeupGallery, name='makeup-gallery'),
    path('makeup-details', views.makeupDetails, name='makeup-details'),
    path('laminare-gallery', views.laminareGallery, name='laminare-gallery'),
    path('laminare-details', views.laminareDetails, name='laminare-details'),
    path('gene-gallery', views.geneGallery, name='gene-gallery'),
    path('gene-details', views.geneDetails, name='gene-details'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

]