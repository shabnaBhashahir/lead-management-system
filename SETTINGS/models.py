from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.



class Companie(models.Model):
    Company=models.CharField(max_length=100)
    Address1=models.CharField(max_length=100)
    Address2=models.CharField(max_length=100)
    Address3=models.CharField(max_length=100)
    Address1=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Website=models.CharField(max_length=100)
    Logo=models.ImageField
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Company
    
    
    class Meta:
        verbose_name_plural = "Company"

    


class State(models.Model):
    state=models.CharField(max_length=300)

    def __str__(self):
        return self.state

    class Meta:
        verbose_name_plural = "States"

class District(models.Model):
    State = models.ForeignKey(State, on_delete=models.CASCADE)
    District = models.CharField(max_length=300, unique=True)



    def __str__(self):
        return self.District

    class Meta:
        verbose_name_plural = "Districts"


class Branch(models.Model):
    Branch=models.CharField(max_length=300)
    Branchcode=models.CharField(max_length=200, verbose_name= "Branch Code")
    Address=models.CharField(max_length=400, blank=True)
    Street=models.CharField(max_length=250, blank=True)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    district=ChainedForeignKey(District,chained_field="State",
                               chained_model_field="State",
                               show_all=False,
                               auto_choose=False,
                               sort=True,
                               verbose_name= "District")
    Pincode=models.CharField(max_length=250, blank=True)
    Mobile=models.CharField(max_length=200)
    Email=models.EmailField(blank=True)
    class Meta:
        verbose_name_plural="Branches"


    def __str__(self):
       return self.Branch



  

    
class Enquiry_source(models.Model):
    Enquirysourcename=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)

    def __str__(self):
     return self.Enquirysourcename
    
    class Meta:
        verbose_name_plural = "Enquiry source"
    
Followupstatuschoices=(("Yes","Yes"),("No","No"))    

class Follow_up_status(models.Model):
    Followupstatusname=models.CharField(max_length=150)
    def __str__(self):
        return self.Followupstatusname
    Followupstatus=models.CharField(max_length=35,
        choices=Followupstatuschoices,default=1)
    class Meta:
        verbose_name_plural = "Follow up status"
    
    


    def __str__(self):
         return f"{self.Followupstatusname},{self.Followupstatus}"
    

class Qualification(models.Model):
    Qualificationname=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Qualificationname}"
    class Meta:
        verbose_name_plural = "Qualification"
    

    
    
class Syllabus(models.Model):
    Syllabus=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Syllabus}"
    class Meta:
        verbose_name_plural = "Syllabus"
    
class Course(models.Model):
    Course=models.CharField(max_length=100)
    Course_code=models.CharField(max_length=100)
    Trainers=models.OneToOneField(User,on_delete=models.CASCADE)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Course}"
    class Meta:
        verbose_name_plural = "Course"
    

class Batch(models.Model):
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch=models.CharField(max_length=100)
    Trainers=models.OneToOneField(User,on_delete=models.CASCADE)
    Start_date=models.DateField()
    End_date=models.DateField()
    Closed=models.BooleanField()
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Course},{self.Trainers},{self.Start_date},{self.End_date},{self.Closed},{self.Batch}"
    


    class Meta:
        verbose_name_plural = "Batch"

class Master_data(models.Model):
    Name=models.CharField(max_length=100)
    Value=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)
    Active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Name},{self.Value},{self.Type}"
    class Meta:
        verbose_name_plural = "Master Data"