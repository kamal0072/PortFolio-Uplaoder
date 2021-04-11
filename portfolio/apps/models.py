from django.db import models

STATE_CHOICE=(
    ('Andman & Nicobar Island','Andman & Nicobar Island'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunchal Pradesh','Arunchal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chatisgarh','Chatisgarh'),
)

class Portfolio(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=100)
    profile_image=models.ImageField(upload_to='profileimage',blank=True)
    my_file=models.FileField(upload_to='docs',blank=True)

