from django.shortcuts import render
from .forms import DonateForm, AppointmentForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from . import forms
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


# Create your views here.

def base(request):
    return render(request,'medical/base.html')

@login_required
def appointment(request):
    temp = 'medical/appt.html'
    if request.method == 'POST':
        form1 = AppointmentForm(request.POST)
        if form1.is_valid():
            form1.save()
    else:
        form1 = AppointmentForm()
    context = {
        'form1':form1,
    }
    return render(request,temp,context)

@login_required
def donation(request):
    template = 'medical/donate.html'
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST.copy()
            name1 = data.get('name')
            email1 = data.get('email')
            mobile1 = data.get('mobile')
            blood1 = data.get('bloodgroup')
            sex1 = data.get('sex')
            age1 = data.get('age')
            address1 = data.get('address')

            records = {'name1':name1 , 'email1':email1 , 'mobile1':mobile1 ,
                        'blood1':blood1, 'sex1':sex1, 'age1':age1 , 'address1':address1}

            return render_to_response('medical/disp.html',records)
    else:
        form = DonateForm()

    context = {
        'form':form,
    }
    return render(request,template,context)

@login_required
def sympt(request):
    return render(request,'medical/symp.html')
