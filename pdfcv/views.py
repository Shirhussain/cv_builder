from django.shortcuts import render, get_object_or_404
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


    return render(request, "pdfcv/accept.html")


def web_cv(request, id):
    cv = get_object_or_404(Profile, pk=id)
    return render(request, "pdfcv/web_cv.html", {"cv":cv})



