from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Project,Resume, Certification

def index(request):

    # Home
    home = Home.objects.latest('updated')

    #Resume
    resume=Resume.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Project
    projects = Project.objects.all()
    
    # Certification
    certification = Certification.objects.all()

    context = {
        'home': home,
        'resume' : resume,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'certification':certification
    }


    return render(request, 'index.html', context)