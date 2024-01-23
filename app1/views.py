from django.shortcuts import render,HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django. contrib import messages
# Create your views here.
# def index(request):
#     return render(request=request,template_name='index.html')


def home(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ResumeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            candidates=Resume.objects.all()

            form.save()
            # messages.add_message(request, messages.success, "Form Sucessfull Filled ")
            return render(request=request,template_name='home.html', context={'candidates':candidates,'form': form})

            # return render(request=request,template_name='msg.html')#show msg at last
    else:
        form = ResumeForm() # An unbound form

    return render(request=request,template_name='home.html', context={'form': form})

def candidate(request):
    return render(request=request,template_name='candidate.html')
