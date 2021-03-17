from django.shortcuts import render,redirect,HttpResponse
from .models import Course, Description, CommentSet
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'all_courses':Course.objects.all()
    }
    return render(request,"add_view.html",context)

def add_course(request):
    if(request.method=='POST'):
        errors=Course.objects.create_validator(request.POST)
        if len(errors)>=1:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect('/') 
        else:   
            dk=Description.objects.create(content=request.POST['desc'])
            bk=Course.objects.create(name=request.POST['name'],desc= dk)
            return redirect('/')

def show_delete_page(request,course_id):
    context={
        'this_course':Course.objects.get(id=course_id)
    }
    return render(request,"delete_course.html",context)

def remove(request,remove_id):
    if(request.POST['button']=='No'):
        return redirect('/')
    if(request.POST['button']=='yes i want to delete this'):
        course_to_remove=Course.objects.get(id=remove_id)
        course_to_remove.delete()
        return redirect('/')

def add_comments(request,course_id):
    
    if(request.method=="POST"):
        errors=CommentSet.objects.create_validator(request.POST)
        if len(errors)>=1:
            for key,value in errors.items():
                messages.error(request, value)
            return redirect(f"/comment/{course_id}") 
        this_course=Course.objects.get(id=course_id)
        this_comment=CommentSet.objects.create(content=request.POST['content'],course=this_course)
        
    return redirect(f"/comment/{course_id}")    
    

def display_comments(request, course_id):
    print(Course.objects.get(id=course_id).comments.all())
    context={
        'course':Course.objects.get(id=course_id),
        'all_comments':Course.objects.get(id=course_id).comments.all()
    }
    
    return render(request,"add_comment.html",context)
