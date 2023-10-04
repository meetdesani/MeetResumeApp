from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('status/', views.status, name='status'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('project/', views.project, name='project'),
    path('certificate/', views.certificate, name='certificate'),
    path('contactus/',views.contactus,name='contactus'),
    path('download_resume/',views.download_resume,name='download_resume'),
]