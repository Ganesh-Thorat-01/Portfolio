from django.db import models
from ckeditor.fields import RichTextField

# HOME SECTION

class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    # save time when modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=200)
    description = RichTextField(blank=False)
    #description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


# SKILLS SECTION

class Category(models.Model):
    name = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)

    

#PROJECT SECTION

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Project {self.id}'

#Certification SECTION

class Certification(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certification/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'Certification {self.id}'

#Resume
class Resume(models.Model):
    link=models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Resume {self.id}'
