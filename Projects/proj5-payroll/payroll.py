from abc import ABC, abstractmethod
import os, os.path, shutil

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
            classification = int(employeeFields[7])
            salary = float(employeeFields[8])
            commission = int(employeeFields[9])
            hourly = float(employeeFields[10])

            if classification == 1:
                empClassification = Salaried(salary)
            elif classification == 2:
                empClassification = Commissioned(salary, commission)
            elif classification == 3:
                empClassification = Hourly(hourly)

            #pass in relevant stuff
            employees.append(Employee(empId, firstName, lastName, address, city, state, empZip, empClassification))

def process_timecards():
    with open(TIMECARD_FILE) as timecards:
        for line in timecards.readlines():
            empId, *hoursWorked = line.rstrip().split(',')
            emp = find_employee_by_id(empId)
            if isinstance(emp.classification, Hourly):
                for hours in hoursWorked:
                    emp.classification.add_timecard(float(hours))
            else:
                print("Invalid employee type")

def process_receipts():
    with open(SALES_FILE) as receipts:
        for line in receipts.readlines():
            empId, *allReceipts = line.rstrip().split(',')
            emp = find_employee_by_id(empId)
            if isinstance(emp.classification, Commissioned):
                for receipt in allReceipts:
                    emp.classification.add_receipt(float(receipt))
            else:
                print("Invalid employee type")

def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()

def find_employee_by_id(empId):
    for emp in employees:
        if emp.emp_id == empId:
            return emp
    raise Exception("Employee not found")


class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zip_code, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.classification = classification

    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(salary, commission_rate);

    def issue_payment(self):
        pay = self.classification.compute_pay()
        if pay > 0:
            with open(PAY_LOGFILE, 'a') as pay_f:
                first_name = self.first_name
                last_name = self.last_name
                addr = self.address
                city = self.city
                state = self.state
                zipCode = self.zip_code
                amount = f'{pay:.2f}'
                print("Mailing", amount, "to", first_name, last_name, "at", addr, city, state, zipCode, file=pay_f)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass

class Hourly(Classification):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = [] #list to hold hours worked

    def add_timecard(self, hours):
        self.timecard.append(hours)

    def compute_pay(self):
        pay = round(self.hourly_rate * sum(self.timecard), 2)
        self.timecard.clear()
        return pay


class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return round(self.salary / 24, 2)

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        salariedPay = self.salary / 24
        commissionRateAsDecimal = self.commission_rate / 100
        totalCommissions = sum(self.receipts) * commissionRateAsDecimal
        totalPay = salariedPay + totalCommissions
        return round(totalPay, 2)


def main():
    load_employees() # You will implement the first three of these functions
    process_timecards()
    process_receipts()
    run_payroll() # This function is given to you in Part 2

    # Save copy of payroll file; delete old file
    shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE) # You define PAY_LOGFILE = ‘paylog.txt’ globally

    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()

    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()

    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()

if __name__ == '__main__':
    main()