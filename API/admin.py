from django.contrib import admin

from API.models import Profile, Experience,Education, Post, Comment
# Register your models here.

class ProfileTable(admin.ModelAdmin):
    list_display = ('user', 'company', 'website', 'location', 'status', 'skills', 'bio', 'githubusername', 'youtube', 'twitter', 'facebook', 'linkedin', 'instagram')
admin.site.register(Profile, ProfileTable)

class ExperienceTable(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'from_date', 'to_date', 'current', 'description')
admin.site.register(Experience, ExperienceTable)

class EducationTable(admin.ModelAdmin):
    list_display = ('school', 'degree', 'field_of_study', 'from_date', 'to_date', 'current', 'description')
admin.site.register(Education, EducationTable)

class PostTable(admin.ModelAdmin):
    list_display = ('user', 'text', 'name', 'avatar', 'date')
admin.site.register(Post, PostTable)

class CommentTable(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'date')
admin.site.register(Comment, CommentTable)
