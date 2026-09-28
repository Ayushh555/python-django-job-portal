from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Company, Job, Application
from .forms import ApplyForm, JobForm


def landingPage(request):
    return render(request, 'landing.html')


def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

        # HR → see applicants for their jobs
        if profile and profile.role == 'HR':
            applications = Application.objects.filter(
                job__company__user=request.user
            ).select_related('job', 'job__company')

            return render(request, 'hr.html', {'applications': applications})

        # Job seeker → see jobs
        jobs = Job.objects.select_related('company').all()

        applied_jobs = Application.objects.filter(user=request.user)\
                                        .values_list('job_id', flat=True)

        return render(request, 'Jobseeker.html', {
            'jobs': jobs,
            'applied_jobs': applied_jobs
        })

    # Not logged in → still show jobs
    jobs = Job.objects.select_related('company').all()
    return render(request, 'Jobseeker.html', {
        'jobs': jobs,
        'applied_jobs': []
    })


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        name = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')

        if form.is_valid() and role:
            user = form.save()

            # create profile
            Profile.objects.create(user=user, role=role)

            # HR gets a company
            if role == 'HR':
                Company.objects.create(
                    user=user,
                    name=user.username,
                    location="Unknown",
                    description="No description"
                )

            return redirect('login')

    return render(request, 'register.html', {'form': form})

@login_required
def postJob(request):
    profile = Profile.objects.filter(user=request.user).first()

    if not profile or profile.role != 'HR':
        return HttpResponse("Unauthorized", status=403)

    # 🔥 AUTO GET COMPANY
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        return HttpResponse("No company found for this HR")

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company   # ✅ auto attach
            job.save()
            return redirect('home')
    else:
        form = JobForm()

    return render(request, 'post_job.html', {'form': form})


@login_required
def applyJob(request, job_id):
    job = Job.objects.get(id=job_id)

    # ✅ CHECK FIRST (before POST logic)
    if Application.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, "You already applied to this job")
        return redirect('home')

    if request.method == 'POST':
        resume = request.FILES.get('resume')
        mobile = request.POST.get('mobile')

        Application.objects.create(
            user=request.user,
            job=job,
            resume=resume,
            mobile=mobile
        )

        return redirect('home')

    return render(request, 'apply.html', {'job': job})

@login_required
def hrDashboard(request):
    applications = Application.objects.filter(job__company__user=request.user)

    return render(request, 'hr.html', {'applications': applications})

@login_required
def update_status(request, app_id, status):
    application = Application.objects.get(id=app_id)

    if request.user.profile.role != 'HR':
        return HttpResponse("Unauthorized")

    application.status = status
    application.save()

    return redirect('home')

@login_required
def candidateDashboard(request):
    applications = Application.objects.filter(user=request.user)

    return render(request, 'candidate_dashboard.html', {
        'applications': applications
    })