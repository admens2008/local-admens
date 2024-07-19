from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.

def index(request):
	active_postings = JobPosting.objects.filter(is_active=True)
	context = {
		"job_postings" : active_postings
	}
	return render (request, "job_board/index.html", context)

def job_detail(request, id):
	job_posting = get_object_or_404(JobPosting, id=id, is_active=True) #JobPosting.objects.get(id=id)
	context = {
		"job" : job_posting
	}
	return render(request, "job_board/job_detail.html", context)
