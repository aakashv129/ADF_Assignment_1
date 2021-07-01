"""Views Page"""
#pylint: disable=relative-beyond-top-level
#pylint: disable=too-many-locals
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from . models import Request_info, Response_info
from . validation_checker import valid_check
# Create your views here.


def index(request):
    """Index Method"""
    return render(request, 'home.html')


def home(request):
    """POST METHOD"""
    if request.method == 'POST':
        first_name = request.POST['f_name']
        middle_name = request.POST['m_name']
        last_name = request.POST['l_name']
        dob = request.POST['dob']
        gender = request.POST['gen']
        nationality = request.POST['nation']
        city = request.POST['city']
        state = request.POST['state']
        pin_code = request.POST['pin']
        qualification = request.POST['qualification']
        salary = request.POST['salary']
        pan_number = request.POST['pan']
        flag, reason = valid_check(first_name, middle_name, last_name, dob, gender, nationality,
                                   city, state, pin_code, qualification, salary, pan_number)
        if flag == 0:
            data = Request_info(f_name=first_name,m_name=middle_name,l_name=last_name,
                                date_of_birth=dob,gender=gender,nation=nationality,
                                city=city,state=state,pin_code=pin_code,qualification=qualification,
                                salary=salary,pan_number=pan_number)
            data.save()
        else:
            print("Flag:", flag)
            print("Reason:", reason)
        if flag == 0:
            data_2 = Response_info(response="Success",reason="Validation Succeeded")
        elif flag == 1:
            data_2 = Response_info(response="Failed",reason="Validation Failure")
        else:
            data_2 = Response_info(response="Failure",reason=reason)
        data_2.save()
        messages.info(request, reason)
        return HttpResponse(reason)
    return render(request, 'home.html')
