#Aprajita Retail - A Complete E-SRP Solution
#Author: Amit Kumar (AKS Labs(India))
#Date : 03/03/2024
#Copyright(C) 2024
#All rights reserved

# modelmapping.py - A mapping of model names to actual model classes

#import  and Required modules
from dbs.models.hrms import Employee, EmployeeDetails, Salary, SalaryLedger, SalaryPayment,Attendance, MonthlyAttendance, TimeSheet, PaySlip
from dbs.models.inventory import Tax
from dbs.models.pos import *
from dbs.models.banking import *
from dbs.models.accounting import *



class ModelMapping:
    # Model mapping
    model_mapping = {
        'employee': Employee,
        'employeedetails': EmployeeDetails,
        'attendance': Attendance,
        'monthlyattendance': MonthlyAttendance,
        'salaryledger': SalaryLedger,
        'timesheet': TimeSheet,
        'salary': Salary,
        'payslip': PaySlip,
       # 'staffadvancereceipt': StaffAdvanceReceipt,

        # Add more mappings as needed
        # Other model mappings...
    }
    
    def get_model_class(self, model_name):
        # Map model names to actual model classes
        return self.model_mapping.get(model_name, None)
