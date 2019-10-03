from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
import json
from .payments import *
#saas-admin checkmate123
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

    def form_valid(self, form):

        if form == PatientRecordForm:
            self.instance.requestingPractitioner = request.user# autofill with current user

    dataform=PatientRecordForm()
    if request.method=='POST':
        dataform=PatientRecordForm(request.POST,request.FILES)
        if dataform.is_valid():
            form_valid(dataform,PatientRecordForm)
            dataform.save()
            messages.success(request,'Patient Data sucessfully uploaded')
            return HttpResponseRedirect(reverse('starter_kit:uploads'))
        else:
            messages.error(request, 'ERROR. Upload failed. Kindly Correcr errors and try again')
            return HttpResponseRedirect(reverse('starter_kit:uploadform'))
    else:
        con={
            "fillform":dataform
        }
        return render(request, 'starter_kit/uploadform.html', context=con)

# previous uploads ordered from the most recent
@login_required()
def UploadPage(request):
    results = PatientData.objects.all().order_by('-addedOn')
    con = {
        'results': results
    }
    return render(request, 'starter_kit/uploads.html', context=con)
# Web page version of downloadable PDF
@login_required()
def ResultsPage(request,id):
    con = {}
    return render(request, 'starter_kit/results.html', context=con)


@login_required()
def process_image(request, requestNum):

    patientRecord = get_object_or_404(PatientData, requestNumber=requestNum)
    PatientData.objects.filter(requestNumber=patientRecord.requestNumber).update(processed=True)

    return HttpResponseRedirect(reverse('mriAnalysis:results', kwargs={'id': requestNum}))

def app_charge(request):
    amount = 5100
    payment_id = request.form['razorpay_payment_id']
    client.payment.capture(payment_id, amount)
    print(json.dumps(client.payment.fetch(payment_id)))
    return json.dumps(client.payment.fetch(payment_id))