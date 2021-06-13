from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from core.models import Profile
from core.forms import SubscriberForm

# def index(request):
#     return render(request, 'index.html')


class IndexView(View):
    def get(self, request):
        profile = Profile.objects.get(id=2)

        form = SubscriberForm()

        email = profile.email
        phone_no = profile.phone_no
        return render(
            request,
            'index.html', 
            {
                "email": email,
                "phone_no": phone_no,
                "form": form
            }
        )
    
    def post(self, request):
        print(request.POST)
        
        profile = Profile.objects.get(id=2)
        form = SubscriberForm(request.POST)
        
        if form.is_valid():
            profile = Profile.objects.create(email=form.cleaned_data.get("email"))

        email = profile.email
        phone_no = profile.phone_no
        return render(
            request,
            'index.html', 
            {
                "email": email,
                "phone_no": phone_no,
                "form": form
            }
        )
