
from typing import ItemsView
from django.db import models
import re

from django.db.models.fields.related import ManyToManyField 
import bcrypt 

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserManager(models.Manager):
    def Validate_Registration(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['existingUser'] = 'User already registered with that username'
        if len(postData['first_name']) < 2:
            errors['first_name']='First Name should be atleast 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name']='Last Name should be atleast 2 characters'
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 4:
            errors['first_name']='Password should be atleast 8 characters'
        if postData['password'] != postData['cf_password']:
            errors['confirm_pw']='Password and confirm password must match'
        # Secret password validation
        if postData['secret_password'] != 'password':
            errors['secret_password'] = 'Invalid secret password'

        return errors
    
    def Login_Validator(self, postData):
        errors = {}
        checkUser = User.objects.filter(email = postData['log_email'])
        if len(checkUser) < 1:
            errors['NoUser'] = 'Invalid Username and Password cobination'
        elif not bcrypt.checkpw(postData['log_password'].encode(), checkUser[0].password.encode()):
            errors['passwordNoMatch'] = 'Invalid user and password combination'
        return errors

class TaskManager(models.Manager):
    def Task_Validator(self, postData):
        errors = {}
        if len(postData['Update_Title']) < 3:
                errors['Update_Title']='Title should be atleast 3 characters'
        if postData['update_due_date'] == False:
                errors['update_due_date']='Must select due date '
        if len(postData['update_description']) < 10:
                errors['update_description']='Description not long enough '
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)

    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=[('manager', 'Manager'), ('employee', 'Employee'), ('head', 'Head'), ('executive', 'Executive')])
   
    secret_password = models.CharField(max_length=255)

    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_head(cls):
        head = cls(
            first_name='Head',
            last_name='of the Organization',
            email='head@abc.com',
            password=bcrypt.hashpw('1234'.encode(), bcrypt.gensalt()).decode(),
            phone_number='1234567890',
            role='head'
        )
        head.save()
        return head

    @classmethod
    def create_executive(cls):
        executive = cls(
            first_name='Chief Executive Officer',
            last_name='of the Organization',
            email='ceo@abc.com',
            password=bcrypt.hashpw('1234'.encode(), bcrypt.gensalt()).decode(),
            phone_number='1234567897',
            role='executive',
        )
        executive.save()
        return executive    


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(User, related_name="has_created_task", on_delete=models.CASCADE)
    assigned_user = ManyToManyField(User, related_name="users_tasks")
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TaskManager()


class Complete(models.Model):
    completion_notes = models.TextField()
    date_completed = models.DateTimeField(null=True)
    status = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    task = models.ForeignKey(Task, related_name="task_notes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

