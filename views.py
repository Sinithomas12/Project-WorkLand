from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.shortcuts import redirect

from datetime import date as d, datetime as dt

# Create your views here.

def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')

######## HOME ########


'''def login(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        data = Login.objects.filter(email=email, password=password)
        
        if data:
            data = Login.objects.get(email=email, password=password)

            if data.userType == "admin":
                msg = "Welcome to Admin Page"
                return HttpResponseRedirect("/admin_home?msg="+msg)

            elif data.userType == "worker":
                workdata = WorkersReg.objects.get(email=email)
                uid = workdata.id
                request.session['uid'] = uid
                msg = "Welcome to Worker Page"
                return HttpResponseRedirect("/worker_home?msg="+msg)

            elif data.userType == "user":
                usrdata = UserReg.objects.get(email=email)
                uid = usrdata.id
                request.session['uid'] = uid
                msg = "Welcome to User Page"
                return HttpResponseRedirect("/user_home?msg="+msg)
        else:
            msg = "Invalid username or password provided"
    return render(request, 'login.html', {"msg": msg})'''
from django.core.exceptions import ObjectDoesNotExist


def login(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        try:
            data = Login.objects.get(email=email, password=password)

            if data.userType == "admin":
                msg = "Welcome to Admin Page"
                return HttpResponseRedirect("/admin_home?msg=" + msg)

            elif data.userType == "worker":
                try:
                    workdata = WorkersReg.objects.get(email=email)
                    uid = workdata.id
                    request.session['uid'] = uid
                    msg = "Welcome to Worker Page"
                    return HttpResponseRedirect("/worker_home?msg=" + msg)
                except ObjectDoesNotExist:
                    msg = "Worker does not exist"

            elif data.userType == "user":
                try:
                    usrdata = UserReg.objects.get(email=email)
                    uid = usrdata.id
                    request.session['uid'] = uid
                    msg = "Welcome to User Page"
                    return HttpResponseRedirect("/user_home?msg=" + msg)
                except ObjectDoesNotExist:
                    msg = "User does not exist"

        except ObjectDoesNotExist:
            msg = "Invalid username or password provided"

    return render(request, 'login.html', {"msg": msg})


def userregistration(request):
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")

        if UserReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email Already Registered"
        else:
            abc = Login.objects.create(
                email=email, password=password, userType='user')
            abc.save()
            reg = UserReg.objects.create(name=name, email=email, address=address,
                                         phone=phone, password=password, usrid=abc, gender=gender)
            reg.save()
            msg = "Registration Successful"
    return render(request, 'userregistration.html', {"msg": msg})


def workerregistration(request):
    msg = ""
    msg = request.GET.get('msg')
    cat = Category.objects.all()
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        image = None
        gender = request.POST.get("Gender")
        experience = request.POST.get("Experience")
        location = request.POST.get("Location")
        category = request.POST.get("Category")
        wages = request.POST.get("Wages")
        try:
            image = request.FILES["image"]
        except KeyError:
            msg = "Please upload image"
            return render(request, 'workerregistration.html', {"msg": msg, "cat": cat})
        if WorkersReg.objects.filter(email=email).exists() or Login.objects.filter(email=email).exists():
            msg = "Email Already Registered"
        else:
            abc = Login.objects.create(
                email=email, password=password, userType='worker')
            abc.save()
            reg = WorkersReg.objects.create(name=name, email=email, address=address,
                                            phone=phone, password=password, worid=abc, image=image, gender=gender, experience=experience, location=location, category=category, wages=wages)

            reg.save()
            msg = "Registration Successful"
    return render(request, 'workerregistration.html', {"msg": msg, "cat": cat})

######## // HOME ########
######## ADMIN ########


def admin_home(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'admin/adminhome.html', {})

def addcategory(request):

    category = request.POST.get("Category")
    msg = request.GET.get('msg')
    if Category.objects.filter(category=category).exists():
        msg = "Already Added"

    else:
       msg = ""
       msg = request.GET.get('msg')
       if request.POST:
           category = request.POST.get("Category")
           image = request.FILES["image"]
           abc = Category.objects.create(
               category=category, image=image)
           abc.save()
           msg = "Added Successfully"

    return render(request, 'admin/addcategory.html', {"msg": msg})
def payments(request):
       msg = ""
       msg = request.GET.get('msg')
       if request.POST:
           type = request.POST.get("type")
           amount= request.POST.get("amount")
           cardno = request.POST.get("cardno")
           pinno=request.POST.get("pinno")
           name=request.POST.get("name")
           month = request.POST.get("month")
           year = request.POST.get("year")

           abc = Payments.objects.create(
               type=type,amount=amount,cardno=cardno,pinno=pinno,name=name,month=month,year=year)
           abc.save()


           return HttpResponseRedirect("" )




def viewuser(request):
    abc = UserReg.objects.filter(status="pending")
    efg = UserReg.objects.filter(status="approved")
    return render(request, 'admin/viewuser.html', {"abc": abc, "efg": efg})


def approveuser(request):
    msg = ""
    id = request.GET.get("id")
    print(id)
    efg = UserReg.objects.filter(usrid=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/viewuser?msg="+msg)


def rejecteduser(request):
    msg = ""
    id = request.GET.get("ab")
    aab = Login.objects.filter(id=id).delete()
    efg = UserReg.objects.filter(id=id).delete()
    msg = "Rejected"
    return HttpResponseRedirect("/viewuser?msg="+msg)


def deleteuser(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    email = request.GET.get("cd")
    abb = UserReg.objects.filter(email=email).delete()
    abo = Login.objects.filter(email=email).delete()
    msg = "Deleted employee"
    return HttpResponseRedirect("/viewuser", {"msg": msg})


def viewworker(request):
    msg = request.GET.get("msg")
    abc = WorkersReg.objects.filter(status="pending")
    efg = WorkersReg.objects.filter(status="approved")
    return render(request, 'admin/viewworker.html', {"abc": abc, "efg": efg, "msg": msg})


def approveworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    print(id)
    efg = WorkersReg.objects.filter(worid=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/viewworker?msg="+msg)

def delbooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    abc = Booking.objects.filter(id=id).delete()

    msg = "Deleted"
    return HttpResponseRedirect("/viewbooking?msg="+msg)

def rejectedworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    aab = Login.objects.filter(id=id).delete()
    efg = WorkersReg.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/viewworker?msg="+msg)
def delcatw(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    aab = Login.objects.filter(id=id).delete()
    efg = WorkersReg.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/bookingcatadmin?msg="+msg)


def deleteworker(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    email = request.GET.get("cd")
    abb = WorkersReg.objects.filter(email=email).delete()
    abo = Login.objects.filter(email=email).delete()
    msg = "Deleted employee"
    return HttpResponseRedirect("/viewworker", {"msg": msg})


def userfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Addfeedback.objects.all()
    return render(request, 'admin/userfeedback.html', {"msg": msg, "abc": abc})


def viewcategory(request):
    msg = ""
    msg = request.GET.get("msg")
    abc = Category.objects.all()
    return render(request, 'admin/viewcategory.html', {"abc": abc, "msg": msg})


def deletecategory(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    abb = Category.objects.filter(id=id).delete()
    msg = "Deleted"
    return HttpResponseRedirect("/viewcategory", {"msg": msg})


def workerfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Workeraddfeedback.objects.all()
    return render(request, 'admin/workerfeedback.html', {"msg": msg, "abc": abc})
def viewbooking(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Booking.objects.all()
    return render(request, 'admin/viewbooking.html', {"msg": msg, "abc": abc})


######## // ADMIN ########
######## USER ########


def user_home(request):
    msg = ""
    msg = request.GET.get('msg')


    return render(request, 'user/userhome.html', {})


def userviewcategory(request):
    msg = request.GET.get('msg')
    abc = Category.objects.all()
    return render(request, 'user/userviewcategory.html', {"abc": abc, "msg": msg})


def bookingcategory(request):
    msg = request.GET.get('msg')
    type = request.GET.get("type")
    abc = WorkersReg.objects.filter(category=type)
    return render(request, 'user/bookingcategory.html', {"abc": abc, "msg": msg})

def bookingcatadmin(request):
    msg = request.GET.get('msg')
    type = request.GET.get("type")
    abc = WorkersReg.objects.filter(category=type)
    return render(request, 'admin/bookingcatadmin.html', {"abc": abc, "msg": msg})

from datetime import datetime, time

from .models import WorkersReg, Booking
from datetime import datetime

from .models import WorkersReg, UserReg, Booking

from django.db.models import Q
from .models import WorkersReg, Booking
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from .models import WorkersReg, Booking
def bookworker(request):
    msg = ""
    id = request.GET.get("id")
    uid = request.session['uid']
    rr = datetime.today()
    today = rr.strftime("%d-%m-%Y")
    abc = WorkersReg.objects.filter(id=id)

    if request.method == 'POST':
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        category = request.POST.get("Category")
        location = request.POST.get("Location")
        payment = request.POST.get("payment")
        startt = request.POST.get("StartTime")
        endt = request.POST.get("EndTime")


        if not startt or not endt:
            msg = "Please enter both start time and end time."
            return render(request, 'user/bookworker.html', {"msg": msg, "abc": abc, "today": today})

        start_time_obj = datetime.strptime(startt, "%I:%M %p").time()
        end_time_obj = datetime.strptime(endt, "%I:%M %p").time()

        startingdate = datetime.strptime(request.POST.get("Startdate"), "%Y-%m-%d").date()
        endingdate = datetime.strptime(request.POST.get("Enddate"), "%Y-%m-%d").date()

        previous_booking = Booking.objects.filter(worid_id=id, endingdate__gte=startingdate)

        if previous_booking.exists():
            previous_booking = previous_booking.latest('-endingdate')
            previous_end_time = datetime.strptime(previous_booking.end_time, "%I:%M %p").time()
            previous_start_time = datetime.strptime(previous_booking.start_time, "%I:%M %p").time()
            previous_start_date = previous_booking.startingdate
            previous_end_date = previous_booking.endingdate
            startingdate = datetime.strptime(request.POST.get("Startdate"), "%Y-%m-%d").date()
            endingdate = datetime.strptime(request.POST.get("Enddate"), "%Y-%m-%d").date()

            if startingdate != previous_start_date and endingdate != previous_end_date and start_time_obj == previous_start_time and end_time_obj == previous_end_time:
                save_booking(startingdate, endingdate, start_time_obj, end_time_obj, uid, id, name, email, phone,
                             category, location,payment)
                msg = "Booking successful."
                return HttpResponseRedirect("/userbookingconfirmation?id=" + id, {"msg": msg})

            else:
                if start_time_obj != previous_end_time and end_time_obj != previous_end_time:
                    if start_time_obj > previous_end_time or (
                            start_time_obj < previous_end_time and end_time_obj < previous_end_time):
                        save_booking(startingdate, endingdate, start_time_obj, end_time_obj, uid, id, name, email,
                                     phone, category, location,payment)
                        msg = "Booking successful."
                        return HttpResponseRedirect("/userbookingconfirmation?id=" + id, {"msg": msg})

                    else:
                        available_workers = get_available_workers(startingdate, start_time_obj, end_time_obj)
                        available_workers = available_workers.exclude( id=id)  # Exclude the current worker from the available workers list
                        print(available_workers)
                        if available_workers.exists():
                            msg = "Worker is already booked."
                            return render(request, 'user/availw.html', {"msg": msg, "abc": abc, "today": today,"available_workers": available_workers})
                        else:
                            msg = "No available workers found."
                            return render(request, 'user/availw.html', {"msg": msg, "abc": abc, "today": today})

                else:
                    available_workers = get_available_workers(startingdate, start_time_obj, end_time_obj)
                    available_workers = available_workers.exclude(
                        id=id)  # Exclude the current worker from the available workers list
                    print(available_workers)
                    if available_workers.exists():
                        msg = "Worker is already booked."
                        return render(request, 'user/availw.html',
                                      {"msg": msg, "abc": abc, "today": today, "available_workers": available_workers})
                    else:
                        msg = "No available workers found."
                        return render(request, 'user/availw.html', {"msg": msg, "abc": abc, "today": today})



        else:
            save_booking(startingdate, endingdate, start_time_obj, end_time_obj, uid, id, name, email, phone, category,
                         location,payment)
            msg = "Booking successful."
            return HttpResponseRedirect("/userbookingconfirmation?id=" + id, {"msg": msg})

    return render(request, 'user/bookworker.html', {"msg": msg, "abc": abc, "today": today})


def get_available_workers(date, start_time, end_time):
    booked_workers = Booking.objects.filter(
        Q(startingdate=date, start_time__lte=start_time, end_time__gte=start_time) |
        Q(startingdate=date, start_time__lte=end_time, end_time__gte=end_time) |
        Q(startingdate=date, start_time__gte=start_time, end_time__lte=end_time)
    ).values_list('worid_id', flat=True)

    available_workers = WorkersReg.objects.exclude(id__in=booked_workers)
    print(available_workers)
    return available_workers



def save_booking(startingdate, endingdate, start_time, end_time, uid, id, name, email, phone, category, location,payment):
    date_diff = endingdate - startingdate
    wages = WorkersReg.objects.get(id=id).wages

    if date_diff.days > 0:
        total_wage = int(date_diff.days) * (int(wages))
    else:
        total_wage = wages

    start_time = start_time.strftime("%I:%M %p")
    end_time = end_time.strftime("%I:%M %p")


    Booking.objects.create(
        name=name,
        email=email,
        phone=phone,
        category=category,
        location=location,
        startingdate=startingdate,
        endingdate=endingdate,
        start_time=start_time,
        end_time=end_time,
        wages=total_wage,
        payment=payment,
        usrid_id=uid,
        worid_id=id
    )
def userbookingconfirmation(request):
    id = request.GET.get("id")
    worker = Booking.objects.filter(worid=id).first()
    return render(request, 'user/userbookingconfirmation.html', {"worker": worker})



def userviewbooking(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    abc = Booking.objects.filter(usrid=uid, status="notbooked")
    efg = Booking.objects.filter(usrid=uid, status="approved")
    return render(request, 'user/userviewbooking.html', {"abc": abc, "efg": efg})


def cancelbooking(request):
    msg = ""
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()
    msg = "Cancelled"
    return HttpResponseRedirect("/userviewbooking?msg="+msg)





def userviewfeedback(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = Rating.objects.filter(worid=id)
    return render(request, 'user/userviewfeedback.html', {"abc": abc})


def addfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    uid = request.session['uid']
    if request.POST:
        feedback = request.POST.get("Feedback")
        efg = Addfeedback.objects.create(
            feedback=feedback, usrid_id=uid)
        efg.save()
        msg = " Feedback Added Successfully"
    return render(request, 'user/addfeedback.html', {"msg": msg})
def workerprofile(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = WorkersReg.objects.filter(id=uid)
    return render(request, 'worker/workerprofile.html', {"abc": abc})


def updateworker(request):
    msg = ""

    uid = request.session['uid']
    abc = WorkersReg.objects.filter(id=uid)
    cat = Category.objects.all()
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        image = request.FILES.get("image")
        gender = request.POST.get("Gender")
        experience = request.POST.get("Experience")
        location = request.POST.get("Location")
        category = request.POST.get("Category")
        wages = request.POST.get("Wages")



        abm = WorkersReg.objects.filter(id=uid)
        print(abm)
        for ab in abm:
            ab.name = name
            ab.email = email
            ab.phone = phone
            ab.password = password
            ab.address = address
            if image is not None:
                ab.image = image
            ab.gender = gender
            ab.experience = experience
            ab.location = location
            ab.category = category
            ab.wages = wages
            ab.save()
            print(ab)

            l = ab.worid
            l.email = email
            l.password = password
            print(l)
            l.save()
            msg = "updated Successfully"
    return render(request, 'worker/workerprofile.html', {"msg": msg, "abc": abc, "cat": cat})
def userprofile(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = UserReg.objects.filter(id=uid)
    return render(request, 'user/userprofile.html', {"abc": abc})
def updateuser(request):
    msg = ""


    uid = request.session['uid']
    print("Received uid:", uid)  # Debug print
    abc = UserReg.objects.filter(id=uid)
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        gender = request.POST.get("Gender")
        print(abc)

        abm = UserReg.objects.filter(id=uid)
        print(abm)
        for ab in abm:
         ab.name = name
         ab.email = email
         ab.phone = phone
         ab.password = password
         ab.address = address
         ab.gender = gender
         ab.save()
         print(ab)
         l = ab.usrid
         l.email = email
         l.password = password
         print(l)
         l.save()

        msg = "Updated successfully"

    return render(request, 'user/userprofile.html', {"msg": msg,"abc":abc})

def payment(request):
    msg = ""
    id = request.GET.get('id')
    print("id", id)
    efg = Booking.objects.filter(id=id)
    if request.POST:
        type = request.POST.get("type")

        amount = request.POST.get("amount")
        cardno = request.POST.get("cardno")
        pinno = request.POST.get("pinno")
        name = request.POST.get("name")
        month = request.POST.get("month")
        year = request.POST.get("year")
        print("Payment type:", type)

        abc = Payments.objects.create(
                type=type, amount=amount, cardno=cardno, pinno=pinno, name=name, month=month, year=year
            )
        abc.save()

        abc = Booking.objects.filter(id=id).update(status="paid")
        msg = "Payment Successful"

    return render(request, 'user/payment.html', {"msg": msg, "efg": efg})

def userpayment(request):
    msg = ""

    id = request.GET.get('id')
    print(id)
    efg = Booking.objects.filter(id=id)
    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        abc = Contactus.objects.create(
            name=name, email=email, message=message)
        abc.save()
        abc = Booking.objects.filter(id=id).update(status="paid")
        msg = "Payment Successfull"
        return HttpResponseRedirect("/userviewbooking?msg="+msg)
    return render(request, 'user/payment.html', {"msg": msg, "efg":efg})

def userviewpayment(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = Booking.objects.filter(usrid=uid, status="paid")
    return render(request, 'user/userviewpayment.html', {"abc": abc})



######## // USER ########
######## WORKER ########

def worker_home(request):
    msg = ""
    msg = request.GET.get('msg')
    return render(request, 'worker/workerhome.html', {})


def workerviewbooking(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    print(uid)
    id = request.GET.get("id")
    abc = Booking.objects.filter(worid=uid, status="notbooked")
    efg = Booking.objects.filter(worid=uid, status="approved")
    return render(request, 'worker/workerviewbooking.html', {"abc": abc, "msg": msg, "efg": efg})


from django.shortcuts import get_object_or_404


def viewfeedback(request):
    msg = ""
    abc = None  # Assign a default value to abc

    if request.method == "POST":
        # Process the form submission
        name = request.POST.get("Name")
        category = request.POST.get("Category")
        rating = request.POST.get("rating")
        feedback = request.POST.get("Feedback")
        abc = Rating.objects.create(rating=rating, feedback=feedback, category=category, name=name, usrid_id=uid,
                                    worid=id)
        abc.save()
        msg = "Feedback Added Successfully"


    # Assuming you want to retrieve all the Rating objects for rendering the template
    all_ratings = Rating.objects.all()
    return render(request, 'admin/viewfeedback.html', {"msg": msg, "abc": all_ratings})

def wviewfeedback(request):

    uid = request.session['uid']
    print(uid)
    abc = Rating.objects.filter(worid=uid)
    print(abc)
    return render(request, 'worker/wviewfeedback.html', {"abc": abc})


def workercompleted(request):
    msg = ""
    msg = request.GET.get("msg")
    uid = request.session['uid']
    id = request.GET.get("id")
    print(id)
    Booking.objects.filter(id=id).update(jobstatus="completed")
    msg = "Work completed"
    return redirect('/workerviewbooking?id=' + id + '&msg=' + msg)

def useraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = UserReg.objects.filter(id=id)
    abc = WorkersReg.objects.filter(id=id)
    booking = Booking.objects.filter(worid_id=id, jobstatus="completed")

    if booking.exists():
        if request.POST:
            name = request.POST.get("Name")
            category = request.POST.get("Category")
            rating = request.POST.get("rating")
            feedback = request.POST.get("Feedback")
            efg = Rating.objects.create(rating=rating, feedback=feedback, category=category, name=name, usrid_id=uid, worid=id)
            efg.save()
            msg = "Feedback Added Successfully"
            return HttpResponseRedirect("/userviewcategory?msg=" + msg)
        return render(request, 'user/useraddfeedback.html', {"msg": msg, "abc": abc})
    else:
        msg = "Cannot provide feedback until the worker completes the job."
        return render(request, 'user/error.html', {"msg": msg})



def rejectbooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    abc = Booking.objects.filter(id=id).delete()
    msg = "Rejected"
    return redirect('/workerviewbooking?msg=' + msg)


def deletebooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    abb = Booking.objects.filter(id=id).delete()
    msg = "Deleted"
    return redirect('/workerviewbooking?msg=' + msg)


def workerviewfeedback(request):
    id = request.GET.get("id")
    uid = request.session['uid']
    abc = Useraddfeedback.objects.filter(worid=uid)
    return render(request, 'worker/workerviewfeedback.html', {"abc": abc})


def workeraddfeedback(request):
    msg = ""
    msg = request.GET.get('msg')
    uid = request.session['uid']
    if request.POST:
        feedback = request.POST.get("Feedback")
        efg = Workeraddfeedback.objects.create(
            feedback=feedback, worid_id=uid)
        efg.save()
        msg = " Feedback Added Successfully"
        return HttpResponseRedirect("/worker_home?msg="+msg)
    return render(request, 'worker/workeraddfeedback.html', {"msg": msg})


def workerviewpayment(request):
    msg = request.GET.get('msg')
    uid = request.session['uid']
    print(uid)
    id = request.GET.get("id")
    abc = Booking.objects.filter(worid=uid, status="paid")
    return render(request, 'worker/workerviewpayment.html', {"abc": abc, "msg": msg})

'''def deletepayment(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("ab")
    abc = Booking.objects.filter(id=id).delete()
    msg = "Deleted"
    #return render(request, 'admin/viewpayment.html', {"msg": msg, "abc": abc})
    return HttpResponseRedirect("/viewpayment?msg="+msg)'''
def rejectedpayment(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()

    msg = "Deleted"
    return HttpResponseRedirect("/viewpayment?msg="+msg)
def wrejectedpayment(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()

    msg = "Deleted"
    return HttpResponseRedirect("/workerviewpayment?msg="+msg)
def urejectedpayment(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    efg = Booking.objects.filter(id=id).delete()

    msg = "Deleted"
    return HttpResponseRedirect("/userviewpayment?msg="+msg)
def viewbooking(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Booking.objects.all()
    return render(request, 'admin/viewbooking.html', {"msg": msg, "abc": abc})
def adminapprovebooking(request):
    msg = ""
    msg = request.GET.get("msg")
    id = request.GET.get("id")
    print(id)
    efg = Booking.objects.filter(id=id).update(status="approved")
    msg = "Approved"
    return HttpResponseRedirect("/viewbooking?msg="+msg)
def viewpayment(request):
    msg = ""
    msg = request.GET.get('msg')
    abc = Booking.objects.filter(status="paid")
    return render(request, 'admin/viewpayment.html', {"abc": abc, "msg": msg})
def search(request):
    query = request.GET.get('q')
    if query:
        abc = WorkersReg.objects.filter(location__icontains=query)
        return render(request, 'user/bookingcategory.html', {'abc': abc})
    else:
        '''abc = WorkersReg.objects.all()'''
        return render(request, 'user/searches.html', {'abc': abc})
def searches(request):
    query = request.GET.get('q')
    if query:
        abc = WorkersReg.objects.filter(location__icontains=query)
        return render(request, 'admin/viewworker.html', {'abc': abc})
    else:
        '''abc = WorkersReg.objects.all()'''
        return render(request, '/searches.html', {'abc': abc})
def contact(request):
    return render(request, 'contact.html')
def contactus(request):
    msg = ""

    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        abc = Contactus.objects.create(
            name=name, email=email,message=message)
        abc.save()

    return render(request, 'contact.html')
def bookworkers(request):
    msg = ""
    msg = request.GET.get('msg')
    id = request.GET.get("id")
    # print(id, " 3333333333333333333333333333333333")

    # print(uid, " 3333333333333333333333333333333333")
    # worid = request.session['worid']
    rr = d.today()
    today = rr.strftime("%Y-%m-%d")
    abc = WorkersReg.objects.filter(id=id)
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        phone = request.POST.get("Number")
        category = request.POST.get("Category")
        location = request.POST.get("Location")
        startingdate = request.POST.get("Startdate")
        endingdate = request.POST.get("Enddate")
        wages = request.POST.get("Wages")

        sdate = dt.strptime(startingdate, "%Y-%m-%d")
        edate = dt.strptime(endingdate, "%Y-%m-%d")

        date_diff = edate-sdate
        print("date_diff", date_diff)
        if date_diff.days > 0:
            totalWage = int(date_diff.days) * (int(wages))
            efg = Booking.objects.create(name=name, email=email, phone=phone, category=category, location=location,
                                         startingdate=startingdate, endingdate=endingdate, wages=totalWage,
                                         usrid_id=uid, worid=id)
            efg.save()
            msg = "Booked Successfully"
            return HttpResponseRedirect("/userviewcategory?msg=" + msg)
        else:
            efg = Booking.objects.create(name=name, email=email, phone=phone, category=category, location=location,
                                         startingdate=startingdate, endingdate=endingdate, wages=wages, usrid_id=uid,worid=id)

            efg.save()
            msg = "Booked Successfully"
            return HttpResponseRedirect("/userviewcategory?msg=" + msg)

    return render(request, 'user/bookworker.html', {"msg": msg, "abc": abc, "today": today})
def searchs(request):
    query = request.GET.get('q')
    if query:
        abc = WorkersReg.objects.filter(location__icontains=query)
        available_workers = abc.exclude(id__in=Booking.objects.values_list('worid_id', flat=True))
        return render(request, 'user/bookingcategory.html', {'abc': available_workers})
    else:
        abc = WorkersReg.objects.all()
        return render(request, 'user/searches.html', {'abc': abc})




