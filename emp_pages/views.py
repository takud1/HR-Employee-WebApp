from django.shortcuts import render
from hr_pages.models import Docs
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def up_docs(request):

    fields = dict()

    for field in Docs._meta.get_fields():
        user = Docs.objects.all().filter(user_id=request.user.id)
        attr = getattr(user[0], field.name)
        fields[field.name.replace('_', ' ').capitalize()] = attr
    
    fields.pop('User')

    return render(request, 'DocSubmit.html', {'fields':fields})