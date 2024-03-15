# #Aprajita Retail HRMS URLS
# #Date: 15/02/2024
# #Author: Amit Kumar (AKS Lab(India))

# import uuid
# from django.urls import path
 
# from hrms.models import Employee, EmployeeDetails, Salary, SalaryLedger, SalaryPayment,Attendance, MonthlyAttendance, TimeSheet, PaySlip, StaffAdvanceReceipt
# from inventory.models import Tax
# from . import views
# from django.urls import  re_path, register_converter


# # Register the UUIDConverter
# class UUIDConverter:
#     regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

#     def to_python(self, value):
#         return uuid.UUID(value)

#     def to_url(self, value):
#         return str(value)

# register_converter(UUIDConverter, 'uuid')

# #Pos is also not added EDC
# app_name='hrms'

# urlpatterns = [
#     path("", index, name="index"),

# #Employee
#     path('employees/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': Employee, 'create_url':'hrms:employee_create','model_name':'employee'},name='employee_list'),
#     path('employees/update/<str:model_id>/', global_model_update, {'model_class': Employee, 'create_url':'hrms:employee_create' ,'return_url':'hrms:employee_list'}, name='employee_create'),
#     path('employees/create/', global_model_create, {'model_class': Employee, 'create_url':'hrms:employee_create' ,'return_url':'hrms:employee_list'}, name='employee_create'),
#     path('employees/detail/<str:model_id>/', global_model_display, {'model_name': Employee, 'return_url':'hrms:employee_list'}, name='employee_detail'),
    

# #EmployeeDetails
#     path('employeedetails/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': EmployeeDetails, 'create_url':'hrms:employeedetails_create','model_name':'employeedetails'},name='employeedetails_list'),
#     path('employeedetails/update/<str:model_id>/', global_model_update, {'model_class': EmployeeDetails, 'create_url':'hrms:employeedetails_create' ,'return_url':'hrms:employeedetails_list'}, name='employeedetails_create'),
#     path('employeedetails/create/', global_model_create, {'model_class': EmployeeDetails, 'create_url':'hrms:employeedetails_create' ,'return_url':'hrms:employeedetails_list'}, name='employeedetails_create'),
#     path('employeedetails/detail/<str:model_id>/', global_model_display, {'model_name': EmployeeDetails, 'return_url':'hrms:employeedetails_list'}, name='employeedetails_detail'),
    

# #Salary
#     path('salary/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': Salary, 'create_url':'hrms:salary_create','model_name':'salary'},name='salary_list'),
#     path('salary/update/<str:model_id>/', global_model_update, {'model_class': Salary, 'create_url':'hrms:salary_create' ,'return_url':'hrms:salary_list'}, name='salary_create'),
#     path('salary/create/', global_model_create, {'model_class': Salary, 'create_url':'hrms:salary_create' ,'return_url':'hrms:salary_list'}, name='salary_create'),
#     path('salary/detail/<str:model_id>/', global_model_display, {'model_name': Salary, 'return_url':'hrms:salary_list'}, name='salary_detail'),
    

# #SalaryLedger
#     path('salaryledger/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': SalaryLedger, 'create_url':'hrms:salaryledger_create','model_name':'salaryledger'},name='salaryledger_list'),
#     path('salaryledger/update/<str:model_id>/', global_model_update, {'model_class': SalaryLedger, 'create_url':'hrms:salaryledger_create' ,'return_url':'hrms:salaryledger_list'}, name='salaryledger_create'),
#     path('salaryledger/create/', global_model_create, {'model_class': SalaryLedger, 'create_url':'hrms:salaryledger_create' ,'return_url':'hrms:salaryledger_list'}, name='salaryledger_create'),
#     path('salaryledger/detail/<str:model_id>/', global_model_display, {'model_name': SalaryLedger, 'return_url':'hrms:salaryledger_list'}, name='salaryledger_detail'),
    

# #SalaryPayment
#     path('salarypayment/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': SalaryPayment, 'create_url':'hrms:salarypayment_create','model_name':'salarypayment'},name='salarypayment_list'),
#     path('salarypayment/update/<str:model_id>/', global_model_update, {'model_class': SalaryPayment, 'create_url':'hrms:salarypayment_create' ,'return_url':'hrms:salarypayment_list'}, name='salarypayment_create'),
#     path('salarypayment/create/', global_model_create, {'model_class': SalaryPayment, 'create_url':'hrms:salarypayment_create' ,'return_url':'hrms:salarypayment_list'}, name='salarypayment_create'),
#     path('salarypayment/detail/<str:model_id>/', global_model_display, {'model_name': SalaryPayment, 'return_url':'hrms:salarypayment_list'}, name='salarypayment_detail'),
    

# #Attendance
#     path('attendance/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': Attendance, 'create_url':'hrms:attendance_create','model_name':'attendance'},name='attendance_list'),
#     path('attendance/update/<str:model_id>/', global_model_update, {'model_class': Attendance, 'create_url':'hrms:attendance_create' ,'return_url':'hrms:attendance_list'}, name='attendance_create'),
#     path('attendance/create/', global_model_create, {'model_class': Attendance, 'create_url':'hrms:attendance_create' ,'return_url':'hrms:attendance_list'}, name='attendance_create'),
#     path('attendance/detail/<str:model_id>/', global_model_display, {'model_name': Attendance, 'return_url':'hrms:attendance_list'}, name='attendance_detail'),
    

# #MonthlyAttendance
#     path('monthlyattendance/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': MonthlyAttendance, 'create_url':'hrms:monthlyattendance_create','model_name':'monthlyattendance'},name='monthlyattendance_list'),
#     path('monthlyattendance/update/<str:model_id>/', global_model_update, {'model_class': MonthlyAttendance, 'create_url':'hrms:monthlyattendance_create' ,'return_url':'hrms:monthlyattendance_list'}, name='monthlyattendance_create'),
#     path('monthlyattendance/create/', global_model_create, {'model_class': MonthlyAttendance, 'create_url':'hrms:monthlyattendance_create' ,'return_url':'hrms:monthlyattendance_list'}, name='monthlyattendance_create'),
#     path('monthlyattendance/detail/<str:model_id>/', global_model_display, {'model_name': MonthlyAttendance, 'return_url':'hrms:monthlyattendance_list'}, name='monthlyattendance_detail'),
    

# #TimeSheet
#     path('timesheet/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': TimeSheet, 'create_url':'hrms:timesheet_create','model_name':'timesheet'},name='timesheet_list'),
#     path('timesheet/update/<str:model_id>/', global_model_update, {'model_class': TimeSheet, 'create_url':'hrms:timesheet_create' ,'return_url':'hrms:timesheet_list'}, name='timesheet_create'),
#     path('timesheet/create/', global_model_create, {'model_class': TimeSheet, 'create_url':'hrms:timesheet_create' ,'return_url':'hrms:timesheet_list'}, name='timesheet_create'),
#     path('timesheet/detail/<str:model_id>/', global_model_display, {'model_name': TimeSheet, 'return_url':'hrms:timesheet_list'}, name='timesheet_detail'),
    

# #PaySlip
#     path('payslip/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': PaySlip, 'create_url':'hrms:payslip_create','model_name':'payslip'},name='payslip_list'),
#     path('payslip/update/<str:model_id>/', global_model_update, {'model_class': PaySlip, 'create_url':'hrms:payslip_create' ,'return_url':'hrms:payslip_list'}, name='payslip_create'),
#     path('payslip/create/', global_model_create, {'model_class': PaySlip, 'create_url':'hrms:payslip_create' ,'return_url':'hrms:payslip_list'}, name='payslip_create'),
#     path('payslip/detail/<str:model_id>/', global_model_display, {'model_name': PaySlip, 'return_url':'hrms:payslip_list'}, name='payslip_detail'),
    

# #StaffAdvanceReceipt
#     path('staffadvancereceipt/', Global_ListView.as_view(),  { 'app_name':'hrms','model_class': StaffAdvanceReceipt, 'create_url':'hrms:staffadvancereceipt_create','model_name':'staffadvancereceipt'},name='staffadvancereceipt_list'),
#     path('staffadvancereceipt/update/<str:model_id>/', global_model_update, {'model_class': StaffAdvanceReceipt, 'create_url':'hrms:staffadvancereceipt_create' ,'return_url':'hrms:staffadvancereceipt_list'}, name='staffadvancereceipt_create'),
#     path('staffadvancereceipt/create/', global_model_create, {'model_class': StaffAdvanceReceipt, 'create_url':'hrms:staffadvancereceipt_create' ,'return_url':'hrms:staffadvancereceipt_list'}, name='staffadvancereceipt_create'),
#     path('staffadvancereceipt/detail/<str:model_id>/', global_model_display, {'model_name': StaffAdvanceReceipt, 'return_url':'hrms:staffadvancereceipt_list'}, name='staffadvancereceipt_detail'),
    


# #Delete pages
#     path('delete/<str:model_name>/<uuid:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
#     path('delete/<str:model_name>/<str:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
#     path('delete/<str:model_name>/<int:model_id>/', Global_DeleteView.as_view(), name='core_delete'),
     
# ]

