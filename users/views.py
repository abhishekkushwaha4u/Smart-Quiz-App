from django.shortcuts import render,HttpResponse,redirect
from . models import  Profile


def profile_create(request):
        if request.method=="POST":
                first_name = request.POST.get("First Name")
                last_name = request.POST.get("Last Name")
                registration_number = request.POST.get("Registration Number")
                phone_number = int(request.POST.get("Phone Number"))
                profile_picture = request.POST.get("Profile Picture")
                email = request.user.email
                role = request.POST.get("role")
                k = Profile(first_name,last_name,registration_number,phone_number,profile_picture,email,role)
                k.save()
                return redirect("users:user_profile",permanent=True)
                
        elif request.user.is_authenticated:
                k = Profile.objects.filter(email=request.user.email)
                if len(k)==0:
                        return render(request,"users/create_profile.html")
                else:
                        return redirect("users:user_profile")
                
        else:
                return redirect("/accounts/login",permanent=True)

def user_profile(request):
        if request.user.is_authenticated:
                k = Profile.objects.get(email=request.user.email)
                if k.role == "student" and k.registration_number!="":
                        profile = [k.first_name,k.last_name,k.registration_number,k.phone_number,k.profile_picture,k.email,k.role]
                        return render(request,"users/user_profile.html",context={"profile":profile})
                elif k.role == "teacher" and k.registration_number=="":
                        profile = [k.first_name, k.last_name, k.registration_number,k.phone_number, k.profile_picture, k.email, k.role]
                        return render(request, "users/user_profile.html", context={"profile": profile})
                else:
                        return HttpResponse("Error in user_profile handling!")

        else:
                return redirect("/accounts/login")
                

    
