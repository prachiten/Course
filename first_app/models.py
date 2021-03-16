from django.db import models
from datetime import datetime

# Create your models here.
class CourseManager(models.Manager):
    def create_validator(self,reqPost):
        errors={}
        course_name=Course.objects.filter(name=reqPost['name'])
        if len(course_name)>=1:
            errors['unique']="Name already taken"
        if len(reqPost['name'])<5:
            errors['name']="name must be at least 5 characters"
        if len(reqPost['desc'])<5:
            errors['desc']="description must be at least 5 characters"
        return errors

class CommentManager(models.Manager):
    def create_validator(self,reqPost):
        errors={}
        if len(reqPost['content'])<2:
            errors['content']="comment must be at least 2 characters"
        return errors  

class Description(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

class Course(models.Model):
    name=models.TextField()
    desc=models.OneToOneField(Description,related_name="course",null=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()
    


class CommentSet(models.Model):
    content=models.TextField()
    course=models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CommentManager()
    