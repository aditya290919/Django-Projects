from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def create(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		summary = request.POST.get('summary')
		degree = request.POST.get('degree')
		school = request.POST.get('school')
		university = request.POST.get('university')
		previous_work = request.POST.get('experience')
		skills = request.POST.get('skills')

		form = Profile(name=name, email=email, phone=phone, 
			summary=summary, degree=degree, school=school, university=university,
			previous_work=previous_work, skills=skills)

		form.save()

	return render(request,'pdf/profile.html')

def profile(request):
	profile_list = Profile.objects.all()
	return render(request, 'pdf/profile_list.html',{'profile_list':profile_list})


def resume(request,pk):
	candidate_info = Profile.objects.get(pk=pk)
	template = loader.get_template('pdf/resume.html')
	html = template.render({'candidate_info':candidate_info})
	options = {
		'page-size':'Letter',
		'encoding':"UTF-8",
	}
	pdf = pdfkit.from_string(html, False, options)
	response = HttpResponse(pdf, content_type = 'application/pdf')
	response['Content-Disposition'] = 'attachment'
	filename = "resume-pdf"

	return response

