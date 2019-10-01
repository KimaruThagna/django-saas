from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from PIL import Image
# Create your views here.
# home page and also login page
def Home(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('starter_kit:landing'))
        else:
            messages.error(request, "You have entered the wrong credentials. Try again")
            return HttpResponseRedirect(reverse('starter_kit:home'))
    else:
        return render(request, 'starter_kit/index.html', context={})

# logout and redirect to homepage
@login_required()
def GoodBye(request):
    logout(request)
    return HttpResponseRedirect(reverse('starter_kit:home'))

# From this page one can proceed to the upload section of the different imagery
@login_required()
def Landing(request):
    con={}
    return render(request, 'starter_kit/landing.html', context=con)


@login_required()
def Uploadform(request):

        return render(request, 'starter_kit/uploadform.html', context=con)

# previous uploads ordered from the most recent
@login_required()
def UploadPage(request):
    con = {}
    return render(request, 'starter_kit/uploads.html', context=con)
# Web page version of downloadable PDF
@login_required()
def ResultsPage(request,id):
    con = {}
    return render(request, 'starter_kit/results.html', context=con)