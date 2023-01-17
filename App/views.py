from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from App.forms import *
# Create your views here.
#FBV for returning string as REsponse

def FBV_String(request):
    return HttpResponse('<h1>This is returned by FBV</h1>')

#CBV for returning string as REsponse

class CBV_String(View):
    def get(self,request):
        return HttpResponse('CBV String')

#FBV for returning HTML page as response

def FBV_Page(request):
    return render(request,'FBV_Page.html')

#CBV for returning HTML page as response

class CBV_Page(View):
    def get(self,request):
        return render(request,'CBV_Page.html')

# FBV for dealing with django forms

def FBV_Form(request):
    form=StudentForm()
    d={'form':form}

    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'FBV_Form.html',d)

# CBV for dealing with django forms

class CBV_Form(View):
    def get(self,request):
        form=StudentForm()
        d={'form':form}
        return render(request,'CBV_Form.html',d)
    
    def post(self,request):
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

# returning HTML page By using TemplateView Class

class CBV_Template(TemplateView):
    template_name='CBV_Template.html'