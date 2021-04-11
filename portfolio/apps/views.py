from django.shortcuts import render
from .forms import PortFolioForm
from django.views import View
from django.http import HttpResponseRedirect
from .models import Portfolio

class PortView(View):
    def get(self,request):
        port=Portfolio.objects.all()
        form=PortFolioForm()
        return render(request,'apps/home.html',{'postf':port,'form':form})

    def post(self,request):
        form=PortFolioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        # return render(request,'apps/home.html',{'form':form})
        return HttpResponseRedirect('//')
        
class UserView(View):
    def get(self,request,pk):
        print(pk)
        bio=Portfolio.objects.get(pk=pk)
        return render(request,'apps/info.html',{'bio':bio})
