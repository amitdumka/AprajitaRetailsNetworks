# Aprajita Retails - Network
# Author : Amit Kumar

#nav_manager.py

class NavManager:
    def __init__(self):
        pass
    # Setting Navigation Data
    def _setNavData(self, title,model_name, base_url, icon): 
        self.title = title
        self.model_name = model_name
        self.base_url = base_url
        self.icon = icon
        self.createurl = base_url + '_create'
        self.updateurl = base_url + '_update'
        self.deleteurl = base_url + '_delete'
        self.listurl = base_url + '_list'
        self.detailurl = base_url + '_detail'
        pass
    
    def getNavData(self):
        return self
    
    
    #TODO: make the static function here for easy use all url in one place