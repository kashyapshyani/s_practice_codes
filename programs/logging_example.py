import logging  
    
a = 10  
b = 0  
    
try:  
    c = a / b  
except Exception as e:  
    logging.error("Exception occurred", exc_info=True)  