from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Profile
# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}
    form_class = LoginForm()

    def get(self, request):
        self.context = {
            "users": User.objects.all(),
            "form": self.form_class
        }
        return render(request, self.template_name, self.context)
    
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password) #check the db
        if user is not None:
            login(request, user)
            redirect("home:index")
        return redirect("home:index")

    

class LogOut(generic.View):
    def get(self, request):
        logout(request)
        return render(request, "home/index.html", {})
    

class SignUp(generic.CreateView):
    template_name = "home/signup.html"
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy("home:index")
    
    def form_invalid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password1 =form.cleaned_data.get("password1")
        user = authenticate(self.request, username = username, password = password1) #check the db
        if user is not None:
            login(self.request, user)
        return redirect("home:index")
  
  
class ListProfile(generic.View):
      template_name = "home/list_profile.html"
      context = {}
      
      def get(self, request):
            self.context = {
                    "profiles": Profile.objects.filter(status=True)
            }
            return render(request, self.template_name, self.context)
        
class DetailProfile (generic.View):
    template_name = "home/detail_profile.html"
    context = {}
      
    def get(self, request, pk):
            self.context = {
                    "profiles": Profile.objects.get(pk=pk)
            }
            return render(request, self.template_name, self.context)
