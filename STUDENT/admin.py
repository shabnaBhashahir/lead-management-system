from django.contrib import admin
from.models import *
from lead.widgets import PastCustomDatePickerWidget
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from.models import Register
from django.utils.http import urlencode
from django.urls import NoReverseMatch



# Register your models here.
# class TrackerJetAdminSite(AdminSite):




#  def get_app_list(self, request, app_label=None):
# # print("hi")
#     """
#     Return a sorted list of all the installed apps that have been
#     registered in this site.
#     """
ordering = {
        "Company": 1,
        "States": 2,
        "Districts": 3,
        "Branches": 4,
        "Enquiry source": 5,
        "Follow up status": 6,
        "Qualification": 7,
        "Syllabus": 8,
        "Course": 9,
        "Batch": 10,
        "Master Data": 11,

    }
appordering = {
   "Settings": 1,
    "Student": 2,
}

    
    
#     app_dict = self._build_app_dict(request, app_label)
#     # a.sort(key=lambda x: b.index(x[0]))
#     # Sort the apps alphabetically.
#     app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

#     app_list = list(app_dict.values())
#     # print(app_dict.values())

#     # app_list = sorted(app_dict.values(), key=lambda x: appordering[x['name']])

#     # app_list.sort(key=lambda x: appordering[x['name']])

#     # Sort the models alphabetically within each app.
#     for app in app_list:
#         app['models'].sort(key=lambda x: ordering[x['name']])

#     return app_list






# mysite = TrackerJetAdminSite()
# admin.site = mysite



class StudentAdmin(admin.ModelAdmin):


    def confirmed(self, obj):
        url = reverse('admin:confirm_url', kwargs={'id': obj.id})
        return format_html('<a class="button" href="{}">Confirm</a>', url)

    fieldsets = (
        ('General', {
            'fields': ('Enquiry_source',),
        }),
        ('Phone', {
            'fields': ('Phone',),
        }),
        ('Personal Info', {
            'fields': (('Student','Gender'),('email','Alternative_email'),('Address','Alternative_Address'),('Dob','Mobile'),( 'State', 'District'),('Pincode','Whatsapp',),)
        }),
        ('Academic Info', {
            'fields': (('College_Name','Year_of_pass'),('Qualification'),('Roll_No','Registration_No'),)
        }),
        ('Course Info', {
            'fields': ('Course',),
        }),
         ('Photo', {
            'fields': ('Photo',),
        }),
         ('STUDENT CALL STATUS', {
            'fields': ('Student_Call_Status','Next_Follow_up_Date','To_Staff','Comments'),
        }),
        
        

  
        
)
    
    formfield_overrides={
        models.DateField: {'widget': PastCustomDatePickerWidget},
    }
    list_display=('Student','Course','Qualification','Mobile','Student_Call_Status','is_active','reg_link')

     
    def reg_link(self,obj):
        try:
            url= f"/admin/STUDENT/register/add/?name={obj.id}"
            link = f'<a href="{url}">Register</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    reg_link.short_description='Register'
    reg_link.allow_tags=True
        

# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
     list_display = ['name', 'phone', 'email', 'course', 'batch', 'have_laptop', 'isactive']


admin.site.register(Student,StudentAdmin)
admin.site.register(Register,RegisterAdmin)