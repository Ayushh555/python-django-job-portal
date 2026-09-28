from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('jobs/', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('post-job/', views.postJob, name='post_job'),
    path('apply/<int:job_id>/', views.applyJob, name='apply'),
    path('update-status/<int:app_id>/<str:status>/', views.update_status, name='update_status'),
    path('my-applications/', views.candidateDashboard, name='candidate_dashboard'),

]