import  range
#Temperature_tolerance
def check_temp_tolerance(temperature):
    if(temperature in range(0,2)):
        print("Warning:Temperature Approaching low")
    elif (temperature in range(42,45)):
        print("Warning:Temeprature Approaching high")
    else:
        print("Temperature is within range")
    
    
   
#soc_tolerance
def check_soc_tolerance(soc):
    if (soc in range(20,24)): 
       print("Warning:SOC Approaching discharge")
    elif(soc in range(76,80)):
       print("Warning:SOC Approaching charge-peak")
    else:
        print("SOC is within range")
  
    
#chargerate_tolerance
def check_chargerate_tolerance(chargeRate):
    if(chargeRate>=(0.8-0.05*0.8) and chargeRate<=0.8):
       print("Warning:Charge rate Approaching peak")
    else:
       print("Charge Rate is OK")
   
