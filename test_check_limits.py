import check_limits

def validate_bms(temperature,soc,chargeRate):
    result=check_limits.Temperature_Ok(temperature) and check_limits.SOC_Ok(soc)and check_limits.Chargerate_Ok(chargeRate)
    print(result)
    
 

    
if __name__ == '__main__':
    #Positive scenarios
    validate_bms(25,70,0.7)
    validate_bms(25,30,0.6)
    validate_bms(22,70,0.5)
    #Negative Scenarios
    validate_bms(-6,10,0.6)   # Temp out of range
    validate_bms(25,106,0.8)  # Soc out of range 
    validate_bms(20,80,0.9)   #chargerate out of range 
    
