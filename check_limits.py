#Temperature_tolerance
def check_temp_tolerance(temperature):
    if (temperature<0 and  temperature>45):
        temp_message="Temperature out of range"
    elif (temperature>=0 and temperature<=(0+0.05*45)):
        temp_message="Warning:Temperature Approaching low"
    elif (temperature >=(45-0.05*45) and temperature<=45):
        temp_message="Warning:Temeprature Approaching high"
    else:
        temp_message="Temperature is OK"
    return temp_message
   
#soc_tolerance
def check_soc_tolerance(soc):
    if(soc<20 and soc>80):
        soc_message="State of Charge out of range"
    elif (soc>=20 and soc<=(20+0.05*80)): 
        soc_message= "Warning:SOC Approaching discharge"
    elif(soc>=(80-0.05*80) and soc<=80):
        soc_message="Warning:SOC Approaching charge-peak"
    else:
        soc_message="State of Charge is OK"
    return soc_message
    
#chargerate_tolerance
def check_chargerate_tolerance(chargeRate):
    if(chargeRate>0.8):
        chargerate_message="Warning:Charge Rate out of range"
    elif(chargeRate>=(0.8-0.05*0.8) and chargeRate<=0.8):
        chargerate_message= "Warning:Charge rate Approaching peak"
    else:
        chargerate_message="Charge Rate is OK"
    return chargerate_message
        


#Temperature verification
def Temperature_Ok(temperature):
    if(temperature<0 or temperature>45):
       return False
    else:
        return True
        
#SOC verification         
def SOC_Ok(soc):
    if(soc<20 or soc>80):
        return False
    else:
        return True

# Chargerate verification        
def Chargerate_Ok(chargeRate):
    if(chargeRate >0.8):
        return False
    else:
        return True

#Battery erification
def battery_Ok(temperature,soc,chargeRate):
    result =Temperature_Ok(temperature) and SOC_Ok(soc) and Chargerate_Ok(chargeRate)
    return result
