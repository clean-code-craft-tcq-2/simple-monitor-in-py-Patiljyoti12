
def print_warning(message):
    print("{} is out of range!".format(message))

#Temperature verification
def Temperature_Ok(temperature):
    if(temperature<0 or temperature>45):
        print_warning("Temperature")
        return False
    else:
        return True
        
#SOC verification         
def SOC_Ok(soc):
    if(soc<20 or soc>80):
        print_warning("State of Charge")
        return False
    else:
        return True

# Chargerate verification        
def Chargerate_Ok(chargeRate):
    if(chargeRate >0.8):
        print_warning("Charge Rate")
        return False
    else:
        return True

