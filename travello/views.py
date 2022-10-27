from django.shortcuts import render
from about_us.models import About_Us
from dest.models import Dest
from contacts.models import UserContacts
from home.models import HomeImage

def homePage(request):
    
    homeData = HomeImage.objects.all()
    hmData = {
        'hmd' : homeData,
    }
    return render(request, 'home.html', hmData)


def aboutPage(request):

    abtData = About_Us.objects.all()
    serviceData = {
        'titleData': abtData
    }
    return render(request, 'about.html', serviceData)

def destPage(request):

    destData = Dest.objects.all()
    dstData = {
        'dst': destData
    }
    return render(request, 'dest.html', dstData)

def contactPage(request):

    return render(request, 'contact.html')

def userData(request):
    
    if request.method == "POST":
        usrname = request.POST.get('username')
        eml = request.POST.get('email')
        mbl = request.POST.get('mobile')
        mssg = request.POST.get('message')
        en = UserContacts(username = usrname,email= eml,mobile= mbl,message= mssg)
        en.save()
    return render(request, 'contact_data.html')