from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date, timedelta
import math
from .models import Course


# Create your views here.
def index_view(request: HttpRequest):

    posts = Course.objects.all()
    return render(request, "main/index.html",{'courses':posts})

def add_courses_view(request: HttpRequest):

    if not request.user.is_staff :
        return render(request, "main/not.html")
    if request.method == 'POST':
        try:
            new_post = Course(
                coursename=request.POST['coursename'], 
                              numberhours=request.POST['numberhours'], 
                              price=request.POST["price"], 
                              startdate= request.POST["startdate"], 
                              expirydate=request.POST["expirydate"], 
                              poster=request.FILES["poster"],
                              categories=request.POST["categories"],
                              content=request.POST["content"]),

            new_post.save()
            new_post.categories.set(request.POST.getlist("categories"))

            return redirect("main:base_view")
        except Exception as e:
            print(e)

    return render(request, "main/add_courses.html", {"categories" : Course.COURSE_CATEGORIES})





def post_detail_view(request:HttpRequest, post_id):

    try:
        post = Course.objects.get(pk=post_id)
    except Course.DoesNotExist:
        post = None
    except Exception as e:
        print(e)


    return render(request, "main/post_detail.html", {"post" : post})

def update_post_view( request:HttpRequest , post_id):
    post = Course.objects.get(pk=post_id)
    if request.method == "POST":
            try:
                post.coursename=request.POST['coursename'], 
                post. numberhours=request.POST['numberhours'], 
                post.startdate= request.POST["startdate"], 
                post. expirydate=request.POST["expirydate"], 
                post. poster=request.FILES["poster"],
                post.categories=request.POST["categories"]
                post.save()
                
                return redirect('main:post_detail_view', {"post" : post})
            except Exception as e:
             print(e)
    return render(request,'main/update_post.html',{'post':post})

def delete_post_view(request, post_id):

    try:
        post = Course.objects.get(pk=post_id)
        post.delete()
    except Exception as e:
        print(e)
    

    return redirect("main:index_view")







def all_courses_view(request:HttpRequest):
    courses=Course.objects.all()

    return render(request, "main/Courses_list.html",{'courses':courses})



def add_about_view(request: HttpRequest):
    return render(request, "main/about.html")


def register_courses_view(request: HttpRequest):
    pass
    return render (request, "main/registerr.html")


def posts_search_view(request:HttpRequest):
    courses = []

    if "search" in request.GET:
        courses = Course.objects.filter(coursename__contains=request.GET["search"])



    return render(request, "main/search_page.html", {"courses" : courses})

import smtplib
from email.message import EmailMessage

def send_zoom_link(receiver_email, zoom_link):
    # تكوين الرسالة
    msg = EmailMessage()
    msg.set_content(f"Here is the Zoom link for your meeting: {zoom_link}")
    msg['Subject'] = 'Zoom Meeting Link'
    msg['From'] = 'your_email@example.com'  # تعديل: استبدلها ببريدك الإلكتروني
    msg['To'] = receiver_email

    # إرسال الرسالة
    try:
        smtp_obj = smtplib.SMTP('smtp.example.com', 587)  # تعديل: استبدلها ببيانات الخادم الخاص بك
        smtp_obj.starttls()
        smtp_obj.login('your_email@example.com', 'your_password')  # تعديل: استبدلها ببيانات البريد الإلكتروني الخاص بك
        smtp_obj.send_message(msg)
        smtp_obj.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# استخدام الدالة لإرسال رابط Zoom
receiver_email = 'recipient@example.com'  # تعديل: استبدلها ببريد المستلم
zoom_link = 'https://zoom.us/example-meeting'  # تعديل: استبدلها برابط Zoom الخاص بك
send_zoom_link(receiver_email, zoom_link)
