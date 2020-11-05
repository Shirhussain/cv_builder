from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

import pdfkit 
import io

from .models import Profile 

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")

        cv = Profile(name=name, email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work, skills=skills)
        cv.save()
        return redirect('cv_list')


    return render(request, "pdfcv/accept.html")


def web_cv(request, id):
    cv = get_object_or_404(Profile, pk=id)
    template = loader.get_template('pdfcv/web_cv.html')
    html = template.render({"cv":cv})
    options = {
        'page-size':'Letter',
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html,False, options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response


def cv_list(request):
    cv_list = Profile.objects.all()
    context = {
        'cv_list': cv_list
    }
    return render(request, "pdfcv/list.html", context)
