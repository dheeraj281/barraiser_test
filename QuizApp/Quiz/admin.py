from django.contrib import admin
from .models import  AppUser,Quiz,Questions,Options, QuizProfile
# Register your models here.
admin.site.register(AppUser)
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(QuizProfile)
