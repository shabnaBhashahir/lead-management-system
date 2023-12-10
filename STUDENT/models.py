from django.db import models
from SETTINGS.models import *
from smart_selects.db_fields import ChainedForeignKey
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from STUDENT.models import Course

# Create your models here.

Genderchoices=(("Male","Male"),("Female","Female"),("Others","Others"))
yearchoices=(("2018","2018"),("2019","2019"),("2020","2020"),("2021","2021"),("2022","2022"),("2023","2023"))
callstatuschoices=(("Interested","Interested"),("Not Interesrted","Not Interested"))
tostaffchoices=(("Harsha","Harsha"),("Mini","Mini"))
qualificationchoices=(("BE","BE"),("B.Tech","B.Tech"))

class Student(models.Model):
    Enquiry_source=models.ForeignKey(Enquiry_source,on_delete=models.CASCADE)
    Phone=models.CharField(max_length=30)
    Student=models.CharField(max_length=50)
    email=models.EmailField()
    Address=models.CharField(max_length=200)
    Dob=models.DateField()
    Street=models.CharField(max_length=50)
    State=models.ForeignKey(State,on_delete=models.CASCADE)
    Pincode=models.CharField(max_length=20)

    Gender=models.CharField(max_length=50,choices=Genderchoices)
    Alternative_email=models.EmailField()
    Alternative_Address=models.CharField(max_length=200)
   
    Mobile=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
   
    District=ChainedForeignKey(District,
                               chained_field="State",
                               chained_model_field="State",
                               show_all=False,  
                               auto_choose=False,
                               sort=True,
                               verbose_name= "District")
    Whatsapp=models.CharField(max_length=30)
    College_Name=models.CharField(max_length=100)
   
    Year_of_pass=models.CharField(max_length=50,choices=yearchoices)
    Qualification=models.CharField(max_length=10,choices=qualificationchoices)

    Roll_No=models.CharField(max_length=100)
    Registration_No=models.CharField(max_length=100)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Photo=models.ImageField(blank=True)
    Student_Call_Status=models.CharField(max_length=50,choices=callstatuschoices)
    Next_Follow_up_Date=models.DateField()
    To_Staff=models.CharField(max_length=50,choices=tostaffchoices)
    Comments=models.CharField(max_length=100,blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Active/Inactive')

    class Meta:
        verbose_name_plural = "Student"

    

    def __str__(self):
        return f" {self.Student}"
    

class Register(models.Model):
    LAPTOP_CHOICES = (("YES","YES"),("NO","NO"))

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    phone = models.CharField(validators=[phone_regex], max_length=12,verbose_name='Phone')
    email = models.EmailField(max_length=200,blank=True,verbose_name='Email')
    course = models.ForeignKey(Course,max_length=100,on_delete=models.CASCADE,verbose_name='Course')
    batch = models.CharField(max_length=200,verbose_name='Batch')
    trainer=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Trainer")
    have_laptop = models.CharField(max_length=100,choices=LAPTOP_CHOICES,verbose_name="Do you have laptop")
    isactive = models.BooleanField(default=True, verbose_name="Registered")


    class Meta:
        verbose_name_plural = "Register"

    def __str__(self):
        return f"{self.name}"