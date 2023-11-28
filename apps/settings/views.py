from django.shortcuts import render, redirect
from apps.settings.models import InfoUser, About, Skills, Contact, Experience, Education
# Create your views here.
def index(request):
    infouser = InfoUser.objects.latest("id")
    return render(request, "index.html", locals())

def about(request):
    info_me = About.objects.latest("id")
    skills = Skills.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    return render(request, "about.html", locals())

def contacts(request):
    info_me = About.objects.latest("id")
    infouser = InfoUser.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name = name, email = email, message = message)
        return redirect('index')
    return render(request, "contact.html", locals())

def portfolio(request):
    return render(request, "portfolio.html", locals())

def blog(request):
    return render(request, "blog.html", locals())

def blog_post(request):
    return render(request, "blog_post.html", locals())