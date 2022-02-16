#Temperature_tolerance
def check_temp_tolerance(temperature):
    if(temperature>=0 and temperature<=(0+0.05*45)):
        print("Warning:Temperature Approaching low")
    elif (temperature >=(45-0.05*45)and temperature<=45):
        print("Warning:Temeprature Approaching high")
    else:
        print("Temperature is within range")
    
    
   
#soc_tolerance
def check_soc_tolerance(soc):
    if (soc>=20 and soc<=(20+0.05*80)): 
       print("Warning:SOC Approaching discharge")
    elif(soc>=(80-0.05*80) and soc<=80):
       print("Warning:SOC Approaching charge-peak")
    else:
        print("SOC is within range")
  
    
#chargerate_tolerance
def check_chargerate_tolerance(chargeRate):
    if(chargeRate>=(0.8-0.05*0.8) and chargeRate<=0.8):
       print("Warning:Charge rate Approaching peak")
    else:
       print("Charge Rate is OK")
   
