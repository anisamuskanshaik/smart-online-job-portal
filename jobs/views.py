from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
from django.shortcuts import get_object_or_404

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
from .models import Application

@login_required(login_url='/login/')
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        Application.objects.create(
    job=job,
    user=request.user,
    name=name,
    email=email
)


        return render(request, 'jobs/apply_success.html', {'job': job})

    return render(request, 'jobs/apply_job.html', {'job': job})
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def my_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'jobs/my_applications.html', {'applications': applications})
