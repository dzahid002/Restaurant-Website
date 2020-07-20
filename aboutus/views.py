from django.shortcuts import render
from .models import AboutUs,Why_Choose_US

# Create your views here.

def aboutus_list(request):
    about= AboutUs.objects.last()
    why_choose_us= Why_Choose_US.objects.all()

    context={
        'about': about,
        'why_choose_us': why_choose_us
    }

    return render(request,'aboutus/about.html',context)
    

 