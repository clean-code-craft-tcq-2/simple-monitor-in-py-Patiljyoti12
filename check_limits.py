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
