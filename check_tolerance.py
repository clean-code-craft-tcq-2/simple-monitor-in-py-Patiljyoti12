import  range
#Temperature_tolerance
def check_temp_tolerance(temperature):
    if(temperature in range(0,2)):
        temp_message="Warning:Temperature Approaching low"
    elif (temperature in range(42,45)):
        tempe_message="Warning:Temeprature Approaching high"
    else:
        temp_message="Temperature is within range"
    return temp_message
    
    
   
#soc_tolerance
def check_soc_tolerance(soc):
    if (soc in range(20,24)): 
       soc_message="Warning:SOC Approaching discharge"
    elif(soc in range(76,80)):
       soc_message="Warning:SOC Approaching charge-peak"
    else:
        soc_message="SOC is within range"
    return soc_message
  
    
#chargerate_tolerance
def check_chargerate_tolerance(chargeRate):
    if(chargeRate>=(0.8-0.05*0.8) and chargeRate<=0.8):
       chargerate_message="Warning:Charge rate Approaching peak"
    else:
       chargerate_message="Charge Rate is OK"
    return chargerate_message
   
