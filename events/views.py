from django.shortcuts import render,redirect

from django.views.generic import View

from events.forms import EventForm,SignInForm,RegistrationForm

from django.contrib.auth import authenticate,login,logout

from events.models import Events,User

from events.decorators import sign_in_required

from django.views.decorators.cache import never_cache

from django.utils.decorators import method_decorator

# Create your views here.
# decs = [sign_in_required,never_cache]
# @method_decorator(decs,name="dispatch")
class SigUpView(View):
    
    template_name = "signup.html"
    
    form_class = RegistrationForm
    
    def get(self,request,*args,**kwargs):
        
        from_instance = self.form_class()
        
        return render(request,self.template_name,{"form":from_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("signin")
            
        
        return render(request,self.template_name,{"form":form_instance})
        
class SigninView(View):

     template_name = "signin.html"
    
     form_class = SignInForm
    
     def get(self,request,*args,**kwargs):
        
        form_instance = self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
     def post(self,request,*args,**kwargs):
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data = form_instance.cleaned_data
            
            uname = data.get("username")

            pwd = data.get("password")
            
            user_object = authenticate(request,username=uname,password=pwd)
            
            if user_object is not None:
                
                login(request,user_object)
                
                print("session started")
                
                return redirect("eventadd")
            
            print("invalid Login Data")

        print("invalid")
         
        return render(request,self.template_name,{"form":form_instance})
    
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        return redirect("signin")


    
class EventsaddView(View):
    
    template_name = "eventsadd.html"
    
    form_class = EventForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance = self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data)
        
        if form_instance.is_valid():
            
            form_instance.instance.owner = request.user
            
            form_instance.save()
            
            return redirect("eventlist")
        
        return render(request,self.template_name,{"form":form_instance})
    
class EventListView(View):
    
    template_name = "eventlist.html"
    
    def get(self,request,*args,**kwargs):
        
        qs = Events.objects.filter(owner=request.user)
        
        return render(request,self.template_name,{"data":qs})
            
            
        
        
        