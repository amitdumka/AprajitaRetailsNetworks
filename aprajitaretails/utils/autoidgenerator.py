# function and class to generate auto id
# Amit Kumar
# 13/02/2024

import datetime
from core.globalEnums import EmpType


class Auto_Id:
    def __init__(self):
        pass
    # Generate Department Code

    def getDeptCode(self, dept):
        print(f"Dept:{dept}")
        match dept:
            case 1:
                return "SM"
            case 4:
                return "ACC"
            case 2:
                return "HK"
            case 3:
                return "OWR"
            case 0:
                return "SLM"
            case 8:
                return "OTH"
            case _:
                return "_ERR_"
    # Generate Salesman Id

    def generate_salesman_id(self, owner_code, date,  count):
        auto_id = f"{owner_code}-{date.year}-SM-{count}"
        return auto_id

    # Generate autoid
    def get_auto_id(self, model_name, model):

        optionName = model_name._meta.verbose_name.lower()
        print(f"Model Name:{model_name}, optionName:{optionName}")
        match optionName:
            case "employee":
                return self.generate_hrms_id(model.StoreId.pk, "employee", model.Category, model.JoiningDate, model_name.objects.filter(Category=model.Category).count()+1)
            case "attendance":
                return self.generate_hrms_id(model.StoreId.pk, "attendance", model.EmployeeId.pk, model.OnDate, -1)
            # auto_id=Auto_Id_Generator(self.__class__.__name__).generate_hrms_id(self.StoreId.pk,"attendance",self.EmployeeId.pk,self.OnDate,-1)
            case "voucher":
                # generate_id(self.StoreId.pk, "voucher", str(self.VoucherType), self.OnDate, count)
                return self.generate_id(model.StoreId.pk, "voucher", str(model.VoucherType), model.OnDate, model_name.objects.filter(VoucherType=model.VoucherType).count()+1)
            case "cashvoucher":
                return self.generate_id(model.StoreId.pk, "cashvoucher", str(model.VoucherType), model.OnDate, model_name.objects.filter(VoucherType=model.VoucherType).count()+1)
            case "salary payment":
                return self.generate_id(model.StoreId.pk, "salary payment", model.OnDate, model_name.objects.filter(OnDate=model.OnDate).count()+1)
            case "salesman":
                # Salesman.SalesmanId=f"{self.StoreId.pk}-{datetime.now().year}-SM-{count}"
                return f'{model.StoreId.pk}-{datetime.now().year}-SM-{model_name.objects.count()+1}'
            case _: return "NOTSUPPORTED"

    def generate_id(self, owner_code, entity_name, entity_type, date, count):
        """Generates an auto ID based on date, count, and employee code.

        Args:
          owner_code: The owner code of the entity.
          entity_name: The name of the entity.
          entity_type: The type of the entity.
          date: The date of the entity.
          count: The count of the entity.

        Returns:
          An auto ID.
        """
        # Get the entity code from the entity name.
        e_name = entity_name._meta.verbose_name.lower()
        entity_code = self.get_entityCode(e_name, entity_type)
        # Create the basic structure of the auto ID.
        auto_id = f"{
            owner_code}-{entity_code}-{date.year}-{date.month}-{date.day}"
        # Add the count to the auto ID.
        if count >= 0:
            auto_id += f"-{count}"
        return auto_id

    def get_entityType_code(self, entity_type):

        print(f"Entity Type:{entity_type}")
        # Payment = 0
        # Receipt = 1
        # Contra = 2
        # DebitNote = 3
        # CreditNote = 4
        # JV = 5
        # Expense = 6
        # CashReceipt = 7
        # CashPayment = 8
        match entity_type:
            case "0":
                return "PY"
            case "1":
                return "RP"
            case "2":
                return "CON"
            case "3":
                return "DN"
            case "4":
                return "CRN"
            case "5":
                return "JV"
            case "6":
                return "EXP"
            case "7":
                return "CRP"
            case "8":
                return "CPT"

            case "Payment":
                return "py"
            case "Receipt":
                return "RP"
            case "Expense":
                return "EXP"
            case "CashPayment":
                return "CPT"
            case "CashReceipt":
                return "CRP"
            case _:
                return "_ERR_"

    def get_entityCode(self, entityCode, entityType):
        match entityCode:
            case "voucher":
                return self.get_entityType_code(entityType)
            case "cashvoucher":
                return self.get_entityType_code(entityType)
            case "salary payment":
                return "SPAY"
            case "note":
                return "NTS"
            case "purchase":
                return "INWD"
            case "sale":
                return "INV"
            case "payslip":
                return "PSP"
            case _:
                return "_ERR_"

    def generate_hrms_id(self, owner_code, entity_name, entity_type, date, count):
        print(f"Entity Type:{entity_type}, Entity Name:{entity_name}")
       # optionName = entity_name._meta.verbose_name.lower()
        match entity_name:
            case "employee":
                # Get the department code from the Department.
                dept = self.getDeptCode(entity_type)
                auto_id = f"{owner_code}-{date.year}-{dept}"
                if count >= 0:
                    auto_id += f"-{count}"
                return auto_id
            case "attendance":
                # auto_id = f"{
                #     owner_code}-{entity_type}-{date.year}-{date.month}-{date.day}"
                auto_id = f"{entity_type}-{date.year}-{date.month}-{date.day}"
                return auto_id
            case _:
                return self.generate_id(owner_code, entity_name, entity_type, date, count)


# Notes: For Employee and Attendance,
# We need to use OwerCode/EmpCode/Date for attendance
# for Empy  Owner/Dept/Year/Count
# for Payslip is normal, salypayment is normal,  only need to handle emp and attenance. rest is normal
# either make special function for HRMS or use project generic.  Implement it and remove this comment when done;
# __end of Functions

class Auto_Id_DuplicateChecker:
    def __init__(self):
        pass

    def check_for_duplicate(self, model_name, model):
        
        optionName=model_name._meta.verbose_name.lower()
        match(optionName):
            case "employee":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case "attendance":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case "voucher":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case "cashvoucher":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case "salarypayment":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case "salesman":
                return self.is_exist(model_name=model_name, pkid=model.pk)
            case _:
                return False

    # Check for Record Exist or not

    def is_exist(self, model_name, pkid):
    
        try:             
            obj = model_name.objects.get(pk=pkid)
            if obj:
                return True
            else:
                return False
                        
        except model_name.DoesNotExist:
            return False

