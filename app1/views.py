from django.shortcuts import render,HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.
# def index(request):
#     return render(request=request,template_name='index.html')


def home(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ResumeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # return HttpResponseRedirect('/home/') # Redirect after POST
            form.save()
            form=ResumeForm()
    else:
        form = ResumeForm() # An unbound form

    return render(request=request,template_name='home.html', context={'form': form})
