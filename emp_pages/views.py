from django.shortcuts import render
from emp_pages.models import Up_Docs
from hr_pages.models import Docs
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse

# Create your views here.

@login_required
def up_docs(request):

    if request.method == "POST":

        aadhar = request.FILES.get('Aadhar Card', None)
        pan = request.FILES.get('Pan Card', None)
        passport = request.FILES.get('Passport', None)
        d_license = request.FILES.get('Driving License', None)

        Up_Docs.objects.update_or_create(

            user = request.user,
            defaults={
                'aadhar_card' : aadhar,
                'pan_card' : pan,
                'passport' : passport,
                'driving_license' : d_license,
            }
        )

        return HttpResponse("<h3>Docs Submitted</h3>")
 

    else:
        fields = dict()

        user = Docs.objects.get(pk=request.user.id)
        temp = model_to_dict(user, exclude='user')

        for key, value in temp.items():
            fields[key.replace('_', ' ').title()] = value

        return render(request, 'DocSubmit.html', {'fields':fields})
    