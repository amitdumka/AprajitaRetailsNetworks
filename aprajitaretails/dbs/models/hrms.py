

#Create your models here.
import calendar
import datetime
 
import uuid
from django.db import models
 
from dbs.models.clients import Store, StoreGroup, Client
from core.globalEnums import EmpType, Gender, AttUnit, SalaryComponent, PayMode
 
import logging
 
from django.utils import timezone

logger = logging.getLogger(__name__)

class Person(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Gender =models.IntegerField(choices=[(tag.value, tag.name) for tag in Gender]    )
    MobileNo = models.CharField(max_length=255)
    EmailId = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Country = models.CharField(max_length=255)
    PinCode = models.CharField(max_length=255)
    class Meta:
        abstract = True




class Employee(Person):
    EmployeeId = models.CharField(max_length=255, primary_key=True, null=False,editable=False, unique=True, db_index=True,)
    EmpId = models.IntegerField()  # Temp Till full migration is done.
    JoiningDate = models.DateTimeField()
    Leavingdate = models.DateTimeField(null=True, blank=True)
    IsWorking = models.BooleanField(default=True)
    Category =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  EmpType]    )
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    def StaffName(self):
        return self.FirstName + " " + self.LastName
    def __str__(self):
        return self.FirstName + " " + self.LastName

    class Meta:
       verbose_name = "Employee"
       verbose_name_plural = "Employees"
    # def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
    #     return super().save(force_insert, force_update, using, update_fields)
       
    # def save(self, *args, **kwargs):       
    #     count=Employee.objects.filter(Category=self.Category).count()
    #     self.EmployeeId=Auto_Id_Generator(self.__class__.__name__).generate_hrms_id(self.StoreId.pk,"employee",self.Category,self.JoiningDate,count)
    #    # self.VoucherNumber = Auto_Id_Generator(self.__class__.__name__).generate_id(self.StoreId.pk, "voucher", str(self.VoucherType), self.OnDate, count)
    #     super(Employee, self).save(*args, **kwargs)

    
        



class EmployeeDetails(models.Model):
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE,primary_key=True,null=False, unique=True, db_index=True, editable=True)
    DateOfBirth = models.DateTimeField(default= timezone.now)
    AdharNumber = models.CharField(max_length=255)
    PanNo = models.CharField(max_length=255)
    OtherIdDetails = models.CharField(max_length=255)
    FatherName = models.CharField(max_length=255)
    MaritalStatus = models.CharField(max_length=255)
    SpouseName = models.CharField(max_length=255, null=True)
    HighestQualification = models.CharField(max_length=255)
    BankAccountNumber = models.CharField(max_length=255)
    BankNameWithBranch = models.CharField(max_length=255)
    IFSCCode = models.CharField(max_length=255)

    class Meta:
        verbose_name = "EmployeeDetails"
        verbose_name_plural = "EmployeeDetails"
    def __str__(self):
        return self.DateOfBirth+", "+self.AdharNumber
    

class Attendance(models.Model):
    AttendanceId = models.CharField(max_length=30, primary_key=True, db_index=True, unique=True, null=False, editable=False)
   
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
   
    OnDate = models.DateTimeField(default= timezone.now)
    Status =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  AttUnit]    )
    EntryTime = models.CharField(max_length=255, null=True)
    Remarks = models.CharField(max_length=255, null=True)
    IsReadOnly=models.BooleanField(default=False)
   
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    #Check For Duplicate attendance
    def checkAttendance(self, id):
        check_exist= Attendance.objects.filter(AttendanceId=id).count()
        if check_exist>0 :
            return True
        else :
            return False

    
    class Meta:
        unique_together = (('EmployeeId', 'OnDate'),)
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
    def __str__(self):
        return self.EmployeeId.FirstName + " " + self.EmployeeId.LastName+" "+str(self.Status)
    
    # def save(self, *args, **kwargs):      
    #     #auto_id=Auto_Id_Generator(self.__class__.__name__).generate_hrms_id(self.StoreId.pk,"attendance",self.EmployeeId.pk,self.OnDate,-1)
    #     # self.AttendanceId=auto_id
    #     #self.validate_unique()
    #     super(Attendance, self).save(*args, **kwargs)
       

#Monthly Attendance
class MonthlyAttendance(models.Model):
   
    MonthlyAttendanceId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
   
    OnDate = models.DateTimeField(default= timezone.now)
    Present = models.IntegerField()
    HalfDay = models.IntegerField()
    Sunday = models.IntegerField()
    PaidLeave = models.IntegerField()
    Holidays = models.IntegerField()
    CasualLeave = models.IntegerField()
    Absent = models.IntegerField()
    WeeklyLeave = models.IntegerField()
    Remarks = models.CharField(max_length=255)
    NoOfWorkingDays = models.IntegerField()
    IsReadOnly=models.BooleanField(default=False)
   
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
   
    @property
    def DayInMonths(self):
        return calendar.monthrange(self.OnDate.year, self.OnDate.month)

    @property
    def Count(self):
        return self.present + self.HalfDay + self.Sunday + self.PaidLeave + self.CasualLeave + self.Absent + self.WeeklyLeave + self.Holidays

    @property
    def BillableDays(self):
        return (self.HalfDay / 2.0) + self.Present + self.Sunday + self.PaidLeave + self.Holidays

    @property
    def Valid(self):
        return self.count == self.day_in_months
    class Meta:
        verbose_name = "MonthlyAttendance"
        verbose_name_plural = "MonthlyAttendances"



class SalaryLedger(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    EmployeeId=models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
   
    OnDate = models.DateTimeField(default= timezone.now)
    Particulars = models.CharField(max_length=255)
    InAmount = models.DecimalField(max_digits=10, decimal_places=2)
    OutAmount = models.DecimalField(max_digits=10, decimal_places=2)
   
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
   
    class Meta:
       #db_table SalaryLedger
        verbose_name = "SalaryLedger"
        verbose_name_plural = "SalaryLedgers"

class TimeSheet(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
   
    OutTime = models.DateTimeField(default= timezone.now)
    InTime = models.DateTimeField(null=True)
    Reason = models.CharField(max_length=255)
   
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    

    @property
    def Duration(self):
        return (self.InTime if self.InTime else datetime.now()) - self.OutTime

    class Meta:
       #db_table TimeSheet
        verbose_name = "TimeSheet"  
        verbose_name_plural = "TimeSheets"

 
class Salary(models.Model):
    SalaryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
   
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
   
    BasicSalary = models.DecimalField(max_digits=10, decimal_places=2)
    EffectiveDate = models.DateTimeField(default= timezone.now)
    CloseDate = models.DateTimeField(null=True)
    IsEffective = models.BooleanField(default=True)
    WowBill = models.BooleanField(default=False)
    Incentive = models.BooleanField(default=False)
    LastPcs = models.BooleanField(default=False)
    SundayBillable = models.BooleanField(default=False)
    FullMonth = models.BooleanField(default=False)
   
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
       #db_table Salary
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"


class SalaryPayment(models.Model):
    SalaryPaymentId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    SlipNo = models.PositiveIntegerField(  null=True, blank=True,   db_index=True, editable=False, auto_created=True)
    SalaryMonth = models.IntegerField()
    SalaryComponet =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  SalaryComponent]    )
    OnDate = models.DateTimeField(default= timezone.now)
    Amount = models.DecimalField (max_digits=10, decimal_places=2)
    PayMode = models.IntegerField(choices=[(tag.value, tag.name) for tag in PayMode]    )
    Details = models.CharField(max_length=255)
    
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
       #db_table SalaryPayment
        verbose_name = "SalaryPayment"
        verbose_name_plural = "SalaryPayments"
        
    #TODO: Implements Custom Save this model , add negative value for receipts 
    #TODO: add Entry on Salary Ledger for payment and receipts so No need to handle seprately
    #TODO: User Function to add Salary Ledger for payment and receipts

#StaffAdvanceReceip: Fuutre Merge with Salary Ledger and Payment and Receitp in one
# class StaffAdvanceReceipt(models.Model):
#     StaffAdvanceReceiptId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
#     SlipNo=models.IntegerField(auto_created=True,    editable=False, db_index=True, unique=True)
#     EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    
#     OnDate = models.DateTimeField(default= timezone.now)
#     Amount = models.DecimalField (max_digits=10, decimal_places=2)
#     PayMode =   models.IntegerField(choices=[(tag.value, tag.name) for tag in  PayMode]    )
#     Details = models.CharField(max_length=255)
    
#     StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
#     StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
#     ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

#     class Meta:
       
#         verbose_name = "StaffAdvanceReceipt"
#         verbose_name_plural = "StaffAdvanceReceipts"


#PaySlip model: This will be autogenrated always. on monthly basis

class PaySlip(models.Model):
    PaySlipId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    OnDate = models.DateTimeField(default= timezone.now)
    Month = models.IntegerField()
    Year = models.IntegerField()
    
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    #SalaryId = models.ForeignKey(Salary, on_delete=models.CASCADE, null=True)

    CurrentSalary = models.ForeignKey(Salary, on_delete=models.CASCADE, null=True)
    BasicSalaryRate = models.DecimalField(max_digits=10, decimal_places=2)
    BasicSalary = models.DecimalField(max_digits=10, decimal_places=2)
    TotalPayableSalary = models.DecimalField(max_digits=10, decimal_places=2)
    NoOfDaysPresent = models.DecimalField(max_digits=10, decimal_places=2)
    WorkingDays = models.IntegerField()
    TotalSale = models.DecimalField(max_digits=10, decimal_places=2)
    SaleIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    WowBillAmount= models.DecimalField(max_digits=10, decimal_places=2)
    WowBillIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    LastPcsAmount = models.DecimalField(max_digits=10, decimal_places=2)
    LastPcsIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    OtherIncentive = models.DecimalField(max_digits=10, decimal_places=2)
    GrossSalary = models.DecimalField(max_digits=10, decimal_places=2)
    TDSDeduction = models.DecimalField(max_digits=10, decimal_places=2)
    PFDeduction = models.DecimalField(max_digits=10, decimal_places=2)
    AdvanceDeducation= models.DecimalField(max_digits=10, decimal_places=2)
    Remarks = models.CharField(max_length=255, null=True,blank=True)
    
    StoreId=models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    StoreGroupId=models.ForeignKey(StoreGroup, on_delete=models.CASCADE, null=True, blank=True)
    ClientId=models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    


    class Meta:
       #db_table PaySlip
        verbose_name = "PaySlip"
        verbose_name_plural = "PaySlips"


# #Salary 
# class Salary(models.Model):
#     salaryId = models.IntegerField(primary_key=True)
#     employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     salaryBasicAmount = models.IntegerField()
#     salaryHRA = models.IntegerField()
#     salaryDA=models.IntegerField()
#     salaryPF = models.IntegerField()
#     salaryTDS = models.IntegerField()
#     salaryOhterAllowance = models.IntegerField()
#     salaryOtherDeduction = models.IntegerField()
#     salaryIncentive=models.IntegerField()
#     salaryTotalSalary = models.IntegerField()
#     noodworkingDays = models.IntegerField()
#     salarybonus = models.IntegerField()

# #Payslip model 
# class Payslip(models.Model):
#     payslipId = models.IntegerField(primary_key=True)
#     employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     payslipMonth = models.IntegerField()
#     payslipYear = models.IntegerField()
#     payslipBasicAmount = models.IntegerField()
#     payslipHRA = models.IntegerField()
#     payslipDA=models.IntegerField()
#     payslipPF = models.IntegerField()
#     payslipTDS = models.IntegerField()
#     payslipOhterAllowance = models.IntegerField()
#     payslipOtherDeduction = models.IntegerField()
#     payslipIncentive=models.IntegerField()
#     payslipTotalSalary = models.IntegerField()
#     payslipNetSalary = models.IntegerField()
#     payslipStatus=models.CharField(max_length=100)
#     payslipRemarks = models.CharField(max_length=100)
#     payslipDate = models.DateTimeField(default= timezone.now)
#     payslipPaymentDate = models.DateTimeField(default= timezone.now)
#     payslipPaymentMode = models.CharField(max_length=100)
#     payslipPaymentAmount = models.IntegerField()
#     payslipPaymentRemarks = models.CharField(max_length=100)