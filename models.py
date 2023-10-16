from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    userType = models.CharField(max_length=100, null=True)
    
class WorkersReg(models.Model):
    worid = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    image= models.ImageField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    wages = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, default="pending")
    jobstatus = models.CharField(max_length=100, null=True, default="not completed")
    
class UserReg(models.Model):
    usrid = models.ForeignKey(Login, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)

    gender = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, default="pending")
    
class Category(models.Model):
    category = models.CharField(max_length=100, null=True)
    image= models.ImageField(max_length=100, null=True)
    
class Booking(models.Model):
    usrid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True)
    worid = models.ForeignKey(WorkersReg, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    startingdate = models.DateField(null=True)
    endingdate = models.DateField(null=True)
    start_time = models.CharField(max_length=20, default='00:00')
    end_time = models.CharField(max_length=20, default='00:00')
    service_completed = models.BooleanField(default=False)
    wages = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True, default="notbooked")
    payment = models.CharField(max_length=100, null=True)
    jobstatus=models.CharField(max_length=100, null=True, default="not completed")
    
class Useraddfeedback(models.Model):
    usrid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True)
    worid = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    feedback = models.CharField(max_length=100, null=True)
    
class Addfeedback(models.Model):
    usrid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=100, null=True)
    
class Workeraddfeedback(models.Model):
    worid = models.ForeignKey(WorkersReg, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=100, null=True)
class Contactus(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    message = models.CharField(max_length=100, null=True)
class Rating(models.Model):
    usrid = models.ForeignKey(UserReg, on_delete=models.CASCADE, null=True,)
    worid = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    rating = models.IntegerField( null=True)
    feedback = models.TextField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Payments(models.Model):
    type = models.CharField(max_length=100, null=True)
    amount = models.EmailField(max_length=100, null=True)
    cardno = models.CharField(max_length=100, null=True)
    pinno = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    month = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)