from django.contrib import admin
from .models import Education, Skills, Project, Certificate, ContactUs

# Register your models here.
class EducationModelAdmin(admin.ModelAdmin):
    list_display= ('title',)

class SkillsModelAdmin(admin.ModelAdmin):
    list_display= ('skill',)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display= ('project',)

class CertificateModelAdmin(admin.ModelAdmin):
    list_display= ('title',)

class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Education, EducationModelAdmin)
admin.site.register(Skills, SkillsModelAdmin)
admin.site.register(Project, ProjectModelAdmin)
admin.site.register(Certificate, CertificateModelAdmin)
admin.site.register(ContactUs,ContactUsModelAdmin)
