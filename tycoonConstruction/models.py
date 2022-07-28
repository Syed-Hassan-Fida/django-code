import email
from pickle import TRUE
from django.db import models
# Manualy Added
# from django.contrib.auth.models import User

# bidding model / projcts model


class Projects(models.Model):
    project_name = models.CharField(max_length=120, null=True)
    mobile_no = models.IntegerField(max_length=20, null=True)
    email = models.EmailField(max_length=50, null=True)
    project_address = models.CharField(max_length=200, null=True)
    desc = models.CharField(max_length=300, null=True)
    project_budget = models.IntegerField(max_length=200, null=True)
    project_assigned_to = models.CharField(max_length=120, null=True)
    meeting_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return "%s" % (self.project_name)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class bidContractor(models.Model):
    
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, default=1)
    mini_vendors = models.IntegerField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.projects.project_name)

class bidVendor(models.Model):
    
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE,  default=1)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s" % (self.projects.project_name)
    


# cost estimation model


class Estimation(models.Model):
    brickCost = models.IntegerField(help_text="Brick Cost")
    sandCost = models.IntegerField(help_text="Sand Cost")
    cementCost = models.IntegerField(help_text="Cement Cost")
    labourCost = models.IntegerField(help_text="Labour Cost")
    steelCost = models.IntegerField(help_text="Steel Cost")
    date = models.DateTimeField(auto_now_add=True)

# vendor to contractor request
class VtoC_req(models.Model):
    name = models.CharField(max_length=30)
    year_of_experience = models.IntegerField()
    projects_done = models.IntegerField()
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='vtoc/')
    date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name