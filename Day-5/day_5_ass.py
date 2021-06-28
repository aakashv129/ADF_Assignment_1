"""MYSQL CONNECTIVITY EXAMPLE DAY 5"""
import datetime
import json
import re
from datetime import date
from datetime import datetime
import logging
import config as cf


logging.basicConfig(filename="message_log.log",
                    format="%(asctime)s : %(name)s : %(message)s",
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def calculate_age(birthdate_date):
    """Age Calculation"""
    today = date.today()
    age = today.year - birthdate_date.year - \
          ((today.month, today.day) < (birthdate_date.month, birthdate_date.day))
    return age


now = datetime.now()

my_cursor = cf.my_db.cursor()

"""my_cursor.execute
        ("CREATE TABLE Request_info (FIRST_NAME VARCHAR(45) NOT NULL,"
         "MIDDLE_NAME VARCHAR(45), LAST_NAME VARCHAR(45) NOT NULL, DOB DATE NOT NULL, "
         "GENDER VARCHAR(45) NOT NULL,NATIONALITY VARCHAR(45) NOT NULL, "
         "CURRENT_CITY VARCHAR(45) NOT NULL, STATE VARCHAR(45) NOT NULL,"
         "PIN_CODE INT(6) NOT NULL, QUALIFICATION VARCHAR(45) NOT NULL, "
         "SALARY INT(45) NOT NULL,PAN_NUMBER INT(10) NOT NULL,TIME DATETIME NOT NULL,  "
         "ID INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY)")
my_cursor.execute
        ("CREATE TABLE Response_info (RESPONSE_ID INT(10) AUTO_INCREMENT PRIMARY KEY,"
         "REQUEST_ID INT(10), RESPONSE VARCHAR(45), "
         "FOREIGN KEY(REQUEST_ID) REFERENCES python_connection.Request_info(ID))")"""

STMT_1 = "INSERT INTO Request_info " \
         "(FIRST_NAME , MIDDLE_NAME, LAST_NAME, DOB, " \
         "GENDER, NATIONALITY,CURRENT_CITY, STATE, PIN_CODE, " \
         "QUALIFICATION, SALARY, PAN_NUMBER, TIME)" \
         " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

STMT_2 = "INSERT INTO Response_info (REQUEST_ID, RESPONSE, REASON) VALUES (%s, %s, %s)"


#pylint: disable=anomalous-backslash-in-string
#pylint: disable=singleton-comparison
#pylint: disable=pointless-string-statement
#pylint: disable=logging-fstring-interpolation
class Base:
    """Validation checker Class"""
    logger.info("Class created for Validating the input details")

    def __init__(self):
        """INIT METHOD"""
        self.reason = ""
        self.flag = 0
        self.temp = []

    def f_name_checker(self, name):
        """First Name Validation"""
        if name.isalpha():
            self.flag = 0
            self.reason = "Success"
            logger.info("First Name is Valid")
        else:
            self.reason = "Invalid name it should be ascii value"
            self.flag = 1
            logger.warning("First Name is Invalid")
        return self.flag, self.reason

    def m_name_checker(self, name):
        """Middle Name Validation"""
        if name.isalpha() or name.isspace():
            self.reason = "Success"
            logger.info("Middle name is Valid")
        else:
            self.reason = "Invalid name it should be ascii value"
            self.flag = 1
            logger.warning("Middle Name is Invalid")
        return self.flag, self.reason

    def l_name_checker(self, name):
        """Last Name Validation"""
        if name.isalpha():
            self.reason = "Success"
            logger.info("Last name is Valid")
        else:
            self.reason = "Invalid name it should be ascii value"
            self.flag = 1
            logger.warning("Last Name is Invalid")
        return self.flag, self.reason

    def dob_checker(self, date_of_birth):
        """Date Of Birth Validation"""
        try:
            birth_date = datetime.strptime(date_of_birth, "%Y/%m/%d")
            birth_date = birth_date.date()
            birth_date = str(birth_date)
            self.temp = birth_date.split('-')
            self.reason = "Success"
            logger.info("Date-Of-Birth is valid")
        except ValueError:
            self.flag = 1
            self.reason = "Incorrect data format, should be YYYY-MM-DD"
            logger.error("Date-Of-Birth in Incorrect Format")
        return self.flag, self.reason, self.temp

    def gender_checker(self, gender_1):
        """Gender Validation"""
        if gender_1.lower() == 'male' or gender_1.lower() == 'female':
            self.reason = "Success"
            logger.info("Gender is Valid")
        else:
            self.flag = 1
            self.reason = "Gender Should be M/F"
            logger.warning("Gender Should be M/F")
        return self.flag, self.reason

    def age_validity_checker(self, gender_gen):
        """Age Validation"""
        years = calculate_age(date(int(b[0]), int(b[1]), int(b[2])))
        print("Age:", years)
        gender_gen = gender_gen.lower()
        if years < 21 and gender_gen == 'male':
            self.reason = "Age is less than expected"
            self.flag = 2
            logger.warning("Age Validation Failed")
        elif years < 18 and gender_gen == 'female':
            self.reason = "Age is less than expected"
            self.flag = 2
            logger.warning("Age Validation Failed")
        else:
            self.reason = "Success"
            logger.info("Age Validation is Succeeded")
        return self.flag, self.reason

    def nation_checker(self, nation):
        """Nationality Validation"""
        if nation.lower() == 'indian' or nation.lower() == 'american':
            self.reason = "Success"
            logger.info("Nation is Validated")
        else:
            self.reason = "Should be an Indian/American"
            self.flag = 2
            logger.warning("Nationality should be Indian/American")
        return self.flag, self.reason

    def city_checker(self, cit):
        """City Validation"""
        if cit.isalpha():
            self.reason = "Success"
            logger.info("City is Validated")
        else:
            self.reason = "City validation Error"
            self.flag = 1
            logger.warning("City Validation Failed")
        return self.flag, self.reason

    def state_checker(self, state_1):
        """State Validation"""
        state_list = ["andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh",
                      "karnataka", "madhya pradesh", "odisha", "tamil nadu",
                      "telangana", "west bengal"]
        if state_1.lower() not in state_list:
            self.reason = "State not in the list"
            self.flag = 2
            logger.warning("State Validation Failed")
        else:
            self.reason = "Success"
            logger.info("State Validation Success")
        return self.flag, self.reason

    def pin_code_checker(self, pin):
        """Pin Code Validation"""
        if len(str(pin)) == 6 and str(pin).isdigit():
            self.reason = "Success"
            logger.info("Pin Code is in correct Format")
        elif len(str(pin)) != 6:
            self.reason = "Invalid Pin-Code it should have six digits"
            self.flag = 1
            logger.warning("Pin-Code Validation Failed")
        else:
            self.reason = "Invalid Pin-Code it should be digits"
            self.flag = 1
            logger.warning("Pin-Code Validation Failed")
        return self.flag, self.reason

    def qualification_checker(self, qual):
        """Qualification Validation"""
        result = re.match('[a-zA-Z\s]+$', qual)
        if bool(result):
            self.reason = "Success"
            logger.info("Qualification is Validated")
        else:
            self.reason = "Invalid Educational qualification"
            self.flag = 1
            logger.warning("Invalid Educational Qualification")
        return self.flag, self.reason

    def salary_checker(self, sal):
        """Salary Validation"""
        if sal < 10000:
            self.reason = "Salary is less than expected"
            self.flag = 2
            logger.warning("Salary is less than Expected")
        elif salary > 90000:
            self.reason = "Salary is more than expected"
            self.flag = 2
            logger.warning("Salary is more than expected")
        else:
            self.reason = "Success"
            logger.info("Salary is validated")
        return self.flag, self.reason

    def pan_checker(self, pan):
        """Pan_Card Validation"""
        if len(pan) == 10 and re.match('[A-Z]+$', pan[0:3]) and re.match('[0-9]+$', pan[3:10]):
            self.reason = "success"
            logger.info("Pan_Card is Validated")
        else:
            self.reason = "Invalid Pan Credential"
            self.flag = 1
            logger.warning("Invalid Pan_details")
        return self.flag, self.reason


v = Base()
logger.info("Getting input from user")
f_name = input("Enter your First Name:")
m_name = input("Enter your middle name:")
l_name = input("Enter your Last Name:")
dob = input("Enter your Date-Of-Birth:yyyy/mm/dd:")
gender = input("Enter your Gender:")
nationality = input("Enter your Nationality:American/Indian:")
city = input("Enter your Current City:")
state = input("Enter your State:")
pin_code = int(input("Enter your Pin_code:"))
qualification = input("Enter your Qualification:")
salary = int(input("Enter your Salary:"))
pan_number = input("Enter your Pan Card Number:")
logger.info("Checking for validity using flag")

flag, reason = v.f_name_checker(f_name)
if flag == 0:
    flag, reason = v.m_name_checker(m_name)
if flag == 0:
    flag, reason = v.l_name_checker(l_name)
if flag == 0:
    flag, reason, b = v.dob_checker(dob)
if flag == 0:
    flag, reason = v.gender_checker(gender)
if flag == 0:
    flag, reason = v.age_validity_checker(gender)
if flag == 0:
    flag, reason = v.nation_checker(nationality)
if flag == 0:
    flag, reason = v.city_checker(city)
if flag == 0:
    flag, reason = v.state_checker(state)
if flag == 0:
    flag, reason = v.pin_code_checker(pin_code)
if flag == 0:
    flag, reason = v.qualification_checker(qualification)
if flag == 0:
    flag, reason = v.salary_checker(salary)
if flag == 0:
    flag, reason = v.pan_checker(pan_number)
if flag == 0:
    logger.info("Storing the validated details into the tables")
    data = (
            f_name, m_name, l_name, dob, gender, nationality, city, state, pin_code, qualification,
            salary, pan_number, now)
    my_cursor.execute(STMT_1, data)
    d = my_cursor.lastrowid
    k = "Validation Success"
    data_2 = (d, reason, k)
    my_cursor.execute(STMT_2, data_2)
    cf.my_db.commit()
    diction = {"Request_id ": d, "Response ": reason}
    diction = json.dumps(diction)
    print(diction)
    logger.info(f"Output is successfully printed in json format:{diction}")
    cf.my_db.close()
    """my_cursor.execute('select * from Request_info')
        user = my_cursor.fetchall()
        for u in user:
            print(u)"""
    """my_cursor.execute('select * from Response_info')
    user_2 = my_cursor.fetchall()
    for u in user_2:
        print(u)"""
if flag == 1:
    logger.info("validation failure")
    k = "Validation Failure"
    diction = {"Response ": k, "Reason ": reason}
    diction = json.dumps(diction)
    print(diction)
if flag == 2:
    logger.info("If Eligibility failed output is stored in table-2 only")
    my_cursor.execute("SELECT max(ID) FROM Request_info")
    my_id = my_cursor.fetchone()
    my_id = int(my_id[0])
    k = "Failed"
    diction = {"Request_id ": my_id, "Response ": k, "Reason ": reason}
    diction = json.dumps(diction)
    print(diction)
    data_2 = (my_id, k, reason)
    my_cursor.execute(STMT_2, data_2)
    cf.my_db.commit()
    logger.info(f"Output is successfully printed in json format:{diction}")
    cf.my_db.close()
    """my_cursor.execute('select * from Response_info')
    user_2 = my_cursor.fetchall()
    for u in user_2:
        print(u)"""
