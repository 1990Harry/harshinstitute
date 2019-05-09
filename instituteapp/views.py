from django.shortcuts import render
from .models import ContactData
from .forms import ContactForm
from .forms import FeedbackForm
from .models import FeedbackData
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def ServicesViews(request):
    return render(request,'services.html')


def ContactViews(request):
    if request.method=='POST':

        cform=ContactForm(request.POST)

        if cform.is_valid():
            fname=request.POST.get('firstname','')
            lname=request.POST.get('lasttname','')
            email=request.POST.get('email','')
            mobile=request.POST.get('mobile','')
            data=ContactData(
                firstname=fname,
                lastname=lname,
                email=email,
                mobile=mobile,
              )
        data.save()
        return HttpResponse('Data inserted')
    else:
        cform=ContactForm()
        return render(request,'contact.html',{'cform':cform})


import datetime
time1=datetime.datetime.now()

def FeedbackView(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')
            name = name.capitalize()

            data=FeedbackData(
                name=name,
                feedback=feedback,
                rating=rating,
                time=time1

            )
            data.save()
            fform=FeedbackForm()
            return render(request,'feedback.html',{'fform':fform})
    else:
        fdata=FeedbackData.objects.all()
        #fdata=FeedbackData.objects.all()
        fform=FeedbackForm()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})



def GallaryView(request):
    return render(request,'gallary.html')