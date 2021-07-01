"""Validation Checking file"""
import datetime
import re
from datetime import date
from datetime import datetime
#pylint: disable=anomalous-backslash-in-string
#pylint: disable=too-many-arguments


def calculate_age(birthdate_date):
    """Age Calculation"""
    today = date.today()
    age = today.year - birthdate_date.year - \
          ((today.month, today.day) < (birthdate_date.month, birthdate_date.day))
    return age


def f_name_checker(name):
    """First Name Validation"""
    if name.isalpha():
        flag_2 = 0
        reason_2 = "Success"
        #logger.info("First Name is Valid")
    else:
        reason_2 = "Invalid name it should be ascii value"
        flag_2 = 1
        #logger.warning("First Name is Invalid")
    return flag_2, reason_2


def m_name_checker(name):
    """Middle Name Validation"""
    flag_3 = 0
    if name.isalpha() or name.isspace():
        reason_3 = "Success"
        #logger.info("Middle name is Valid")
    else:
        reason_3 = "Invalid name it should be ascii value"
        flag_3 = 1
        #logger.warning("Middle Name is Invalid")
    return flag_3, reason_3


def l_name_checker(name):
    """Last Name Validation"""
    if name.isalpha():
        flag_4 = 0
        reason_4 = "Success"
        #logger.info("Last name is Valid")
    else:
        reason_4 = "Invalid name it should be ascii value"
        flag_4 = 1
        #logger.warning("Last Name is Invalid")
    return flag_4, reason_4


def dob_checker(date_of_birth):
    """Date Of Birth Validation"""
    temp=[]
    print(date_of_birth)
    try:
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        birth_date = birth_date.date()
        birth_date = str(birth_date)
        temp = birth_date.split('-')
        reason_5 = "Success"
        flag_5 = 0
        print(temp)
        #logger.info("Date-Of-Birth is valid")
    except ValueError:
        flag_5 = 1
        reason_5 = "Incorrect data format, should be DD-MM-YYYY"
        #logger.error("Date-Of-Birth in Incorrect Format")
    return flag_5, reason_5, temp


def gender_checker(gender_1):
    """Gender Validation"""
    if gender_1.lower() == 'male' or gender_1.lower() == 'female':
        reason_6 = "Success"
        flag_6 = 0
        #logger.info("Gender is Valid")
    else:
        flag_6 = 1
        reason_6 = "Gender Should be M/F"
        #logger.warning("Gender Should be M/F")
    return flag_6, reason_6


def age_validity_checker(gender_gen, bind):
    """Age Validation"""
    years = calculate_age(date(int(bind[0]), int(bind[1]), int(bind[2])))
    print("Age:", years)
    gender_gen = gender_gen.lower()
    if int(years) < 21 and gender_gen == 'male':
        reason_7 = "Age is less than expected"
        flag_7 = 2
        #logger.warning("Age Validation Failed")
    elif int(years) < 18 and gender_gen == 'female':
        reason_7 = "Age is less than expected"
        flag_7 = 2
        #logger.warning("Age Validation Failed")
    else:
        reason_7 = "Success"
        flag_7 = 0
        #logger.info("Age Validation is Succeeded")
    return flag_7, reason_7


def nation_checker(nation):
    """Nationality Validation"""
    if nation.lower() == 'indian' or nation.lower() == 'american':
        reason_8 = "Success"
        flag_8 = 0
        #logger.info("Nation is Validated")
    else:
        reason_8 = "Should be an Indian/American"
        flag_8 = 2
        #logger.warning("Nationality should be Indian/American")
    return flag_8, reason_8


def city_checker(cit):
    """City Validation"""
    if cit.isalpha():
        reason_9 = "Success"
        flag_9 = 0
        #logger.info("City is Validated")
    else:
        reason_9 = "City validation Error"
        flag_9 = 1
        #logger.warning("City Validation Failed")
    return flag_9, reason_9


def state_checker(state_1):
    """State Validation"""
    state_list = ["andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh",
                  "karnataka", "madhya pradesh", "odisha", "tamil nadu",
                  "telangana", "west bengal"]
    if state_1.lower() not in state_list:
        reason_10 = "State not in the list"
        flag_10 = 2
        #logger.warning("State Validation Failed")
    else:
        reason_10 = "Success"
        flag_10 = 0
        #logger.info("State Validation Success")
    return flag_10, reason_10


def pin_code_checker(pin):
    """Pin_Code Validation"""
    if len(str(pin)) == 6 and str(pin).isdigit():
        reason_11 = "Success"
        flag_11 = 0
        #logger.info("Pin Code is in correct Format")
    elif len(str(pin)) != 6:
        reason_11 = "Invalid Pin-Code it should have six digits"
        flag_11 = 1
        #logger.warning("Pin-Code Validation Failed")
    else:
        reason_11 = "Invalid Pin-Code it should be digits"
        flag_11 = 1
        #logger.warning("Pin-Code Validation Failed")
    return flag_11, reason_11


def qualification_checker(qual):
    """Qualification Validation"""
    result = re.match('[a-zA-Z\s]+$', qual)
    if bool(result):
        reason_12 = "Success"
        flag_12 = 0
        #logger.info("Qualification is Validated")
    else:
        reason_12 = "Invalid Educational qualification"
        flag_12 = 1
        #logger.warning("Invalid Educational Qualification")
    return flag_12, reason_12


def salary_checker(sal):
    """Salary Validation"""
    if int(sal) < 10000:
        reason_13 = "Salary is less than expected"
        flag_13 = 2
        #logger.warning("Salary is less than Expected")
    elif int(sal) > 90000:
        reason_13 = "Salary is more than expected"
        flag_13 = 2
        #logger.warning("Salary is more than expected")
    else:
        reason_13 = "Success"
        flag_13 = 0
        #logger.info("Salary is validated")
    return flag_13, reason_13


def pan_checker(pan):
    """Pan_card Validation"""
    if len(pan) == 10 and re.match('[A-Z]+$', pan[0:3]) and re.match('[0-9]+$', pan[3:10]):
        reason_14= "success"
        flag_14 = 0
        #logger.info("Pan_Card is Validated")
    else:
        reason_14 = "Invalid Pan Credential"
        flag_14 = 1
        #logger.warning("Invalid Pan_details")
    return flag_14, reason_14


def valid_check(f_name, m_name, l_name, dob, gender, nationality,
                city, state, pin_code, qualification, salary, pan_number):
    """Validation"""
    flag_1 = 0
    flag_1, reason = f_name_checker(f_name)
    if flag_1 == 0:
        flag_1, reason = m_name_checker(m_name)
    if flag_1 == 0:
        flag_1, reason = l_name_checker(l_name)
    if flag_1 == 0:
        flag_1, reason, bind = dob_checker(dob)
        if flag_1 == 0:
            flag_1, reason = gender_checker(gender)
            if flag_1 == 0:
                flag_1, reason = age_validity_checker(gender, bind)
    if flag_1 == 0:
        flag_1, reason = nation_checker(nationality)
    if flag_1 == 0:
        flag_1, reason = city_checker(city)
    if flag_1 == 0:
        flag_1, reason = state_checker(state)
    if flag_1 == 0:
        flag_1, reason = pin_code_checker(pin_code)
    if flag_1 == 0:
        flag_1, reason = qualification_checker(qualification)
    if flag_1 == 0:
        flag_1, reason = salary_checker(salary)
    if flag_1 == 0:
        flag_1, reason = pan_checker(pan_number)
    return flag_1, reason
