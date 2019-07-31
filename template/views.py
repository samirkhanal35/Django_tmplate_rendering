from django.shortcuts import render

# Create your views here.

from .models import detail

def user_detail_view(request):
    obj = detail.objects.get(id=1)
    context={
        'name':obj.name,
        'address':obj.address

    }
    return render(request,"home.html",context=context)

