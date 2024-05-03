from rest_framework import serializers


try:

    from dbs.models.clients import Client
    from dbs.models.clients import Store
    from dbs.models.clients import StoreGroup
    from dbs.models.banking import BankAccount
    from dbs.models.banking import VendorBankAccount
    from dbs.models.accounting import Voucher
    from dbs.models.accounting import CashVoucher
    from dbs.models.accounting import DailySale
    from dbs.models.accounting import CustomerDue
    from dbs.models.accounting import Salesman
    from dbs.models.hrms import Employee
    from dbs.models.hrms import Attendance

except:
    pass 

class ClientSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Client
        except:
            pass    
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Store
        except:
            pass    
        fields = '__all__'

class StoreGroupSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = StoreGroup
        except:
            pass    
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = BankAccount
        except:
            pass    
        fields = '__all__'

class VendorBankAccountSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = VendorBankAccount
        except:
            pass    
        fields = '__all__'

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Voucher
        except:
            pass    
        fields = '__all__'

class CashVoucherSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = CashVoucher
        except:
            pass    
        fields = '__all__'

class DailySaleSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = DailySale
        except:
            pass    
        fields = '__all__'

class CustomerDueSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = CustomerDue
        except:
            pass    
        fields = '__all__'

class SalesmanSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Salesman
        except:
            pass    
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Employee
        except:
            pass    
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Attendance
        except:
            pass    
        fields = '__all__'

