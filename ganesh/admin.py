from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Project,Resume, Certification


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]


# Project
admin.site.register(Project)

# Certification
admin.site.register(Certification)

#Resume
admin.site.register(Resume)