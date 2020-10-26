from django.shortcuts import render
from .models import hyaluronGalleryClass, hyaluronDetailsClass, makeupGalleryClass, makeupDetailsClass, laminareGalleryClass, laminareDetailsClass, geneGalleryClass, geneDetailsClass, aboutPage, contactPage
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def hyaluronGallery(request):
    context = hyaluronGalleryClass.objects.all().order_by('-date_published')
    return render(request, 'hyaluron-gallery.html', {'context':context})

def hyaluronDetails(request):
    context = hyaluronDetailsClass.objects.all()
    return render(request, 'hyaluron-details.html', {'context':context})

def makeupGallery(request):
    context = makeupGalleryClass.objects.all().order_by('-date_published')
    return render(request, 'makeup-gallery.html', {'context':context})

def makeupDetails(request):
    context = makeupDetailsClass.objects.all()
    return render(request, 'makeup-details.html', {'context':context})

def laminareGallery(request):
    context = laminareGalleryClass.objects.all().order_by('-date_published')
    return render(request, 'laminare-gallery.html', {'context':context})

def laminareDetails(request):
    context = laminareDetailsClass.objects.all()
    return render(request, 'laminare-details.html', {'context':context})

def geneGallery(request):
    context = geneGalleryClass.objects.all().order_by('-date_published')
    return render(request, 'gene-gallery.html', {'context':context})

def geneDetails(request):
    context = geneDetailsClass.objects.all()
    return render(request, 'gene-details.html', {'context':context})

def blog(request):
    return render(request, 'blog.html', {})

def about(request):
    context = aboutPage.objects.all()
    return render(request, 'about.html', {'context':context})

def contact(request):
    context = contactPage.objects.all()
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        service_choice = request.POST['service-choice']
        service = "Buna ziua, ati primit un email de la " + message_name + " cu privire la serviciul de " + service_choice
        send_mail(
            message_name,
            service + "\n" + message,
            message_email,
            ['beautifybyioanapopa@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_email':message_email, 'context':context})
    
    else:
        #return page
        return render(request, 'contact.html', {})