

class UpdateTrigger:

    def __init__(self):
        pass
    
    def handle_update(self, model_name, model, request):
        
        match model_name._meta.verbose_name:
            case "SalaryPayment":
                pass
            case "ProductSale":
                pass
            case "Employee":
                pass
            case _:
                pass        
        pass
    
    
    