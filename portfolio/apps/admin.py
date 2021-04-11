from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','pin','state',
    'mobile','email','job_city','profile_image','my_file']
    
