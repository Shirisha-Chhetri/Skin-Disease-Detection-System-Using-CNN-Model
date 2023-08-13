from django.shortcuts import render

from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .ml import predict
import tensorflow as tf
import numpy as np
from PIL import Image
from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile, DiseaseDetail, SkinCareCenter,DiseaseImage, UserUpload


# home
def home(request):
    prediction = None
    disease = DiseaseDetail.objects.all().order_by('id')
    carecenter= SkinCareCenter.objects.all().order_by('id')
    if request.method == "POST" and request.FILES['affectedphoto']: 
        if request.user.is_authenticated:
            addProfile = UserUpload(user= request.user, image= request.FILES['affectedphoto'])
            addProfile.save()
            imagePath = addProfile.image.url
            fullImagePath = "C:/Users/Admin/Desktop/Files/Skin Disease Detection System/detection_system" + imagePath

            image = Image.open(fullImagePath)
            resizedImage = image.resize((256, 256))
           
            # Convert the image to a NumPy array
            imageArray = np.array(resizedImage)

            trainedModel = tf.keras.models.load_model('C:/Users/Admin/Documents/Model/dataset_trained.h1')
            prediction = predict(trainedModel, imageArray)
        else:
            return redirect('/login')
    return render(request, 'home.html',
                  {'diseases':disease,
                   'carecenters': carecenter,
                   'prediction' : prediction})

# about
def about(request):
    return render(request,'about.html')

def carecenters(request):
    carecenter= SkinCareCenter.objects.all().order_by('id')
    return render(request,'carecenters.html', {'carecenters': carecenter})

# specific center
def specific_center(request,id):
    specificcenter = get_object_or_404(SkinCareCenter, pk=id)
    return render(request,'specific_center.html',{'center':specificcenter})

# specific disease
def specific_disease(request,id):
    specificdisease = get_object_or_404(DiseaseDetail, pk=id)
    photos = DiseaseImage.objects.filter(existing=specificdisease)
    return render(request,'diseaseinfo.html',{'disease':specificdisease, 'photos' : photos})


@login_required(login_url ='login')
# to change user password 
def change_password_profile(request):
    img={}
    if Profile.objects.filter(user=request.user):
        img = Profile.objects.get(user=request.user)
        
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Your password is successfully updated!')     
        else: 
            messages.success(request,'You got error while changing password.Please correct them!')    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'profile.html', {'form': form ,'img':img})

    
def addprofile(request):
    if request.method == "POST" and request.FILES['profileimage']:
        addProfile = Profile(user=request.user, image= request.FILES['profileimage'])
        addProfile.save()
        # encrypt("media/userprofile/", key)
        return redirect('/profile/')
    
def updateImage(request):
    if request.method == "POST":
        img = Profile.objects.get(user=request.user)
        img.image = request.FILES['updateimg']
        img.save()
        return redirect('/profile/')

def deleteimage(request):
    if Profile.objects.filter(user=request.user):
        img = Profile.objects.get(user=request.user)
        request.user.profile.image.delete()  # delete old image file
        request.user.profile.image = '../media/user.png' # set default image
        request.user.profile.save()
    return redirect('/profile/')

def reset_password(request):
    form = PasswordResetForm()
    return render(request, 'reset_confirm_4.html', {'form': form })


# login module
def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request,"Invalid username or password")
            return redirect('/login/')   
    return render(request,'login.html')


@login_required(login_url ='login')
def logouts(request):
    logout(request)
    return redirect('/')

# signup module   
def signup(request):
    error_message = {}

    if request.method == "POST":
        fn = request.POST['first_name']
        ln =  request.POST['last_name']
        un =  request.POST['username']
        email = request.POST['email']
        password =  request.POST['password']

        user = User(first_name = fn,
                        last_name = ln,
                        username = un,
                        email = email,
                        password = password)
          
        if(not fn):
            error_message = "Enter firstname"
        elif (fn.isnumeric()):
            error_message = "Name cannot have number"

        elif (not ln):
            error_message = "Enter lastname"
        elif (ln.isnumeric()):
            error_message = "Name cannot have number"
        
        elif not un:
            error_message = "Enter username"
        elif (un.isnumeric()):
            error_message = "Username cannot be the number"

        elif not email:
            error_message = "Enter Email"
        elif (email.isnumeric()):
            error_message = "Email cannot be the number"

        elif not password:
            error_message = "Enter Password"
        elif len(password) < 5:
            error_message = "Password must be greater than 5 character"

        elif User.objects.filter(email = email).exists():
            error_message = "Email already registered.."

        elif User.objects.filter(username = un).exists():
            error_message = "Username already registered.."

        if not error_message:
            user.password = make_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request,'register.html',{'error':error_message})
    return render(request,'register.html')
