from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from road.forms import SignUpForm,SignInForm,RoadViolationForm

from django.contrib.auth import authenticate,login,logout

from road.models import RoadViolation

from django.contrib import messages

from road.decorators import signin_required

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache

# Create your views here.

decs=[signin_required,never_cache]

class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signin")
        
        print("account creation failed")

        return render(request,self.template_name,{"form":form_instance})
    

class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pswd=data.get("password")

            user_obj=authenticate(request,username=uname,password=pswd)

            if user_obj:

                login(request,user_obj)

                return redirect("violation-add")
            
        return render(request,self.template_name,{"form":form_instance})

@method_decorator(decs,name="dispatch")
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

@method_decorator(decs,name="dispatch")
class RoadViolationAddView(View):

    template_nmae="violation_add.html"

    form_class=RoadViolationForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_nmae,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            RoadViolation.objects.create(**data,owner=request.user)

            messages.success(request,"road violations added successfully")

            return redirect("violation-list")
        
        messages.error(request,"sorry !! not added")

        return render(request,self.template_nmae,{"form":form_instance})
    
class ViolationListView(View):

    template_name="list.html"

    def get(self,request,*args,**kwargs):

        qs=RoadViolation.objects.all()

        return render(request,self.template_name,{"data":qs})

#delete
   
class ViolationDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        RoadViolation.objects.get(id=id).delete()

        messages.success(request,"succssfully removed!!")

        return redirect("violation-list")

#update

class ViolationUpdateView(View):

    template_name="update.html"

    form_class=RoadViolationForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        property_object=get_object_or_404(RoadViolation,id=id)

        form_instance=self.form_class(instance=property_object)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        property_object=get_object_or_404(RoadViolation,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=property_object)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"succssfully  updated!!")
            
            return redirect("violation-list")
        
        messages.error(request,"failed to update ")
        
        return render(request,self.template_name,{"form":form_instance})
    









