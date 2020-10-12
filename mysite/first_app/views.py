from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app.forms import UserForm,UserProfileForm
# Create your views here.

def index(request):
#    return HttpResponse("Hello World!")
    my_dict={'insert_me':"Hello I'm from views.py"}
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}

    return render(request,'first_app/index.html',context=date_dict)


def form_name_view(request):
    form=forms.FormName()

    if request.method == "POST":
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print("Text"+form.cleaned_data['text'])
    return render(request,'first_app/form_page.html',{'form':form})

def register(request):
    registered= False
    if request.method =="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_forms.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form, 'registered':registered})
