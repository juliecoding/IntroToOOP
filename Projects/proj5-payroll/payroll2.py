from abc import ABC, abstractmethod
import os, os.path

#Module Definitions
employees = []
EMPLOYEE_FILE = "employees.csv"
TIMECARD_FILE = "timecards.csv"
SALES_FILE = "receipts.csv"
PAY_LOGFILE = "paylog.txt"

def load_employees():
    with open(EMPLOYEE_FILE) as empFile:
        firstLine = empFile.readline()

        for emp in empFile.readlines():
            employeeFields = emp.rstrip().split(',')
            empId = employeeFields[0]
            firstName = employeeFields[1]
            lastName = employeeFields[2]
            address = employeeFields[3]
            city = employeeFields[4]	
            state = employeeFields[5]	
            empZip = employeeFields[6]
            classification = employeeFields[7]
            salary = employeeFields[8]	
            commission = employeeFields[9]	
            hourly = employeeFields[10]

            #Figure out what Classification the Employee is and Create that object
            #1 is hourly, 2 salary, and 3 is commision
            if classification == 1: #hourly
                empClassification = Hourly(hourly)
            elif classification == 2: #salary
                empClassification = Salaried(salary)
            else: #classiffication
                empClassification = Commissioned(salary, commission)

            employees.append(Employee(empId, firstName, lastName, address, city, state, empZip, empClassification))

def process_timecards():
    #51-4678119,7.6,3.1,1.4,4.1,6.4,7.7,6.6
    with open(TIMECARD_FILE) as timecards:
        for line in timecards.readlines():
            empId, *hoursWorked = line.rstrip().split(',')
            emp = find_employee_by_id(empId)

            for hours in hoursWorked:
                emp.add_timecard(float(hours))

def process_receipts():
    pass

def run_payroll():
    pass

def find_employee_by_id(empId):
    for emp in employees:
        if emp.emp_id == empId:
            return emp
    raise Exception("Employee not found")
    

###Class Employee###
class Employee:
    def __init__(self,emp_id,first_name,last_name,address,city,state,emp_zip,classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.emp_zip = emp_zip
        self.classifcation = classification

    def make_hourly(self, hourly_rate):
        pass

    def make_salaried(self, salary):
        pass

    def make_commissioned(self, salary, commission_rate):
        pass

    def issue_payment(self):
        pass

    def __str__(self):
        pass

class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass

class Hourly(Classification):
    def __init__(self, hourly_rate):
        self.hourlyRate = hourly_rate

    def add_timecard(self, hours):
        #Begin here next time
        pass

    def compute_pay(self):
        pass

class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        pass

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate

    def add_receipt(self, amount):
        pass

    def compute_pay(self):
        pass




    