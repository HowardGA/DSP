from django.shortcuts import render, redirect
from django.views import generic
import requests
from .forms import CreateGrantGoalClientForm

# Create your views here.

class CreateGrantGoalClient(generic.View):
    template_name = "grantgoal/create_gg_cl.html"
    context = {}
    url = "http://localhost:8000/api/v1/list/grantgoal"
    response = None
    payload = {}
    form_class = CreateGrantGoalClientForm
    
    def get(self, request):
        self.context = {
            "form": self.form_class
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        self.payload = {
                "ggname": request.POST['ggname'],
                "description": request.POST['description'],
                "days_duration": request.POST['days_duration'],
                "priority": request.POST['priority'],
                "state": request.POST['state'],
                "status": request.POST['status'],
                "slug": request.POST['slug'],
                "user": 1 #Change this to the users data
        }
        self.response = requests.post(url=self.url, data=self.payload)
        return redirect("gg:client_list_gg")


class ListGrantGoalClient(generic.View):
    template_name = "grantgoal/list_gg_cl.html"
    url = "http://localhost:8000/api/v1/list/grantgoal"
    response = None
    context = {}
    
    def get(self, request):
        self.response = requests.get(url = self.url)
        self.context = {
            "grantgoals": self.response.json()
        }
        return render(request, self.template_name, self.context)
    
class DetailGrantGoalClient(generic.View):
    template_name = "grantgoal/detail_gg_cl.html"
    context = {}
    url = "http://localhost:8000/api/v1/detail/grantgoal/"
    response = None
    
    def get(self, request, pk):
        self.url = self.url + f'{pk}'
        self.response = requests.get(url = self.url)
        self.context = {
            "grantgoal": self.response.json()
        }
        return render(request, self.template_name, self.context)
