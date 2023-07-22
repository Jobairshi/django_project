from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render,redirect,HttpResponse
from  .Forms import  userForm
from .models import userInfo
# def register_view(request, *args, **kwargs):
#     # if request.method == 'POST':
#     #     u_name = request.POST.get('name')
#     #     u_phone = request.POST.get('phone')
#     #     u_email = request.POST.get('email')
#     #     u_pass = request.POST.get('pass')
#      form = userForm(request.POST or None)
#      if form.is_valid():
#         form.save()
#      context = {
#          'form':form
#      }
#      return render(request,'register.html',context)
def register_view(request, *args, **kwargs):
    msg = None
    if request.method == 'POST':
        u_name = request.POST.get('name')
        u_phone = request.POST.get('phone')
        u_email = request.POST.get('email')
        u_pass = request.POST.get('pass')
        try:
            user = userInfo.objects.get(user_email=u_email)
        except userInfo.DoesNotExist:
            new_user = userInfo(user_name = u_name, user_email = u_email, user_pass = u_pass, user_phone = u_phone)
            new_user.save()
            msg = "congrats new user created!!"
        else:
            msg = "user exists with the same email"
            return HttpResponse(json.dumps(msg), content_type='application/json')
    context = {
        'msg': msg
    }
    return render(request, "register.html", context)

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Query the database for the user with the given email and password
        try:
            user = userInfo.objects.get(user_email=email, user_pass=password)
        except userInfo.DoesNotExist:
            # If user does not exist, show an error message or redirect to a login failed page
            return render(request, "login.html", {"error_message": "Invalid email or password."})
        else:
            # If the user exists, perform the necessary login actions (e.g., set a session, redirect to a protected page)
            # For example, you can set a session to mark the user as logged in:
            request.session['id'] = user.id
            return redirect('/register')  # Replace 'protected_page' with the name of the URL pattern for the protected page

    return render(request, "login.html")
