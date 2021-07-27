from django.contrib import messages
from django.shortcuts import redirect, render
from emp_pages.models import Up_Docs
from hr_pages.models import Docs, UserData
from project1.models import Notifications
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

        users = UserData.objects.filter(is_staff=True)

        for user in users:
            Notifications.objects.create(

                    user = user,
                    title = "Document Submission",
                    notification = "Employee {} (ID:{}) has submitted his/her documents for review".format(request.user.get_full_name(), request.user.emp_id),
                )

        messages.success(request, 'The Documents Have Been Uploaded')
        return redirect('/emp/up_docs/')

    else:
        fields = dict()

        docs = Docs.objects.get(pk=request.user.id)
        temp = model_to_dict(docs, fields=['aadhar_card', 'pan_card', 'passport', 'driving_license'])

        for key, value in temp.items():
            if value:
                fields[key.replace('_', ' ').title()] = value

        return render(request, 'DocSubmit.html', {'fields':fields})
    