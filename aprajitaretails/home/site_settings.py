# Aprajita Retails - Networks
# Author: Amit Kumar(AKS Labs(India))
# Date: 14?March/2024

#site_settings.py
#Site Settings: Holds all site settings,
#     Session Data
#     Store Selection Settings
#     Location  Setting
#     Operating Mode
#     User Infomation
#     Some Other Detail , That will be mention or added here later as created

class SessionData:

    def __init__(self,request):        
        self.LoadSessionData(request)
        pass
    
    def LoadSessionData(self, request):
        self.UserName=request.session.get(SiteSetting.User)
        self.EmployeeName=request.session.get(SiteSetting.EmployeeName)
        self.EmployeeId=request.session.get(SiteSetting.EmpId)
        self.EmpType=request.session.get(SiteSetting.EmpType)
        self.Role=request.session.get(SiteSetting.Role)
        self.StoreId=request.session.get(SiteSetting.StoreId)
        self.GroupId=request.session.get(SiteSetting.GroupId)
        self.ClientId=request.session.get(SiteSetting.ClientId)
        self.IsLoggedIn=request.session.get(SiteSetting.IsLoggedIn)
        self.StoreName=request.session.get(SiteSetting.StoreName)
        self.OperationalMode=request.session.get(SiteSetting.OperationalMode)
        pass

class SiteSetting:

    User="user"
    StoreId="StoreId"
    GroupId="GroupId"
    ClientId="ClientId"
    Role="Role"
    StoreName="StoreName"
    IsLoggedIn="IsLoggedIn"
    EmpId="EmpId"
    EmployeeName="EmployeeName"
    EmpType="EmpType"
    OpsMode="OpsMode"
    
     
    
    def Set(self, request, key, value):
        try :
            request.session[key]=value
            return True
        except :
            return False
    
    def Read(self, request, key, default=None):
        return request.session.get(key, default)
    
    
    def Set_LoggedUser(self, request, user):
        
        
        request.session[self.EmpId]=user.EmployeeId
        request.session[self.EmployeeName]=user.EmployeeId.StaffName
        request.session[self.EmpType]=user.EmployeeId.EmpType
        request.session[self.IsLoggedIn]=True        
        request.session[self.Role]=user.Role
        request.session[self.User]=user.username
        request.session[self.StoreId]=user.StoreId
        request.Session[self.GroupId]=user.GroupId
        request.session[self.ClientId]=user.ClientId        
        request.session[self.StoreName]=user.StoreId.StoreName
        request.session[self.OpsMode]="Normal"
        #request.session['greeting'] = 'Hello, Django Sessions!'
        pass
    
    def Get_StoreId(self,request):
        return request.session.get(SiteSetting.StoreId)
    def Get_GroupId(self,request):
        return request.session.get(SiteSetting.GroupId)
    def Get_ClientId(self,request):
        return request.session.get(SiteSetting.ClientId)
    def Get_Role(self,request):
        return request.session.get(SiteSetting.Role)
    def Get_StoreName(self,request):
        return request.session.get(SiteSetting.StoreName)
    def Get_EmpId(self,request):
        return request.session.get(SiteSetting.EmpId)
    def Get_EmployeeName(self,request):
        return request.session.get(SiteSetting.EmployeeName)
    def Get_EmpType(self,request):
        return request.session.get(SiteSetting.EmpType)
    def Get_IsLoggedIn(self,request):
        return request.session.get(SiteSetting.IsLoggedIn)
    def Get_OpsMode(self,request):
        return request.session.get(SiteSetting.OperationalMode)
    def Get_User(self,request):
        return request.session.get(SiteSetting.User)
    
    
    
    
    
    