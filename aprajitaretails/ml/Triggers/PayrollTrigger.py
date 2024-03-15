#Aprajita Retails- Network
#Date: 13/03/2024
#Author: Amit Kumar

#Prayroll Trigger: Handel all payroll level opertation

from hrms.models import Attendance, EmployeeDetails, MonthlyAttendance
from django.db.models import Count, Case, When, IntegerField
from datetime import datetime
import calendar

class PayrollManger:
    
    
    def __init__(self, storegroupid,storeId, appclinetid) -> None:
        self.StoreGroupId=storegroupid
        self.StoreId=storeId
        self.ClientId=appclinetid
    
    
    
    def calculate_attendance(self,  year=2024, month=3):
        
        #Calculate No of Working Days in the month
        noOfWorkingDays=calculate_working_days(year, month)
        
        # Define the start and end dates for the month
        start_date = datetime(year, month, 1)
        end_date = datetime(year, month+1, 1) if month < 12 else datetime(year+1, 1, 1)

        # Query the Attendance model for the given store_id and date range, and group by employee_id
        attendance_records = Attendance.objects.filter(store_id=self.StoreId, date__range=(start_date, end_date)).values('employee_id')

        # Annotate the queryset with the counts of 'Present', 'Absent', and 'HalfDay'
        attendance_records = attendance_records.annotate(
            Present=Count(Case(When(status='Present', then=1), output_field=IntegerField())),
            Absent=Count(Case(When(status='Absent', then=1), output_field=IntegerField())),
            HalfDay=Count(Case(When(status='HalfDay', then=1), output_field=IntegerField()))
        )

        # Create a MonthlyAttendance object for each group of attendance records
        monthly_attendance_records = [
            MonthlyAttendance (
                EmployeeId=record['employee_id'],
                OnDate=datetime(year, month, 1),
                Present=record['Present'],
                Absent=record['Absent'],
                HalfDay=record['HalfDay'],
                
                Sunday = record['Sunday'],
                PaidLeave = record['PaidLeave'],
                Holidays = record['Holidays'],
                CasualLeave = record['CasualLeave'],
                 
                WeeklyLeave = record['WeeklyLeave'],
                Remarks = f'Auto Generated on {datetime.now()}',
                NoOfWorkingDays = noOfWorkingDays,
                IsReadOnly=True,
            
                StoreId=self.StoreId,
                StoreGroupId=self.StoreGroupId,
                ClientId=self.ClientId
            )
            for record in attendance_records
        ]

        return monthly_attendance_records
    
    def save_monthly_attendances(self, monthly_attendances):
        try:
            MonthlyAttendance.objects.bulk_create(monthly_attendances)
            return True
        except Exception as e:
            print(e)
            return False
         
        
 

def calculate_working_days(year, month):
    # Get the total number of days in the month
    total_days = calendar.monthrange(year, month)[1]

    # Initialize the count of working days
    working_days = 0

    # Iterate over all the days in the month
    for day in range(1, total_days + 1):
        # Get the weekday of the current day (0 is Monday, 6 is Sunday)
        weekday = datetime(year, month, day).weekday()

        # If the weekday is not Sunday, increment the count of working days
        if weekday < 6:
            working_days += 1

    return working_days

def get_days_in_month(date):
    # Extract the year and month from the date
    year = date.year
    month = date.month

    # The function monthrange() returns a tuple containing the number of days in the month and the day of the week that the month starts on.
    _, num_days = calendar.monthrange(date, month)
    return num_days