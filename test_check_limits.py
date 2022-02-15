import check_limits

def test_temperature_ok(temperature,expected_temp_result):
    resultant_temp_result =check_limits.Temperature_Ok(temperature)
    assert(resultant_temp_result==expected_temp_result)


def test_SOC_ok(soc,expected_soc_result):
    resultant_soc_result=check_limits.SOC_Ok(soc)
    assert(resultant_soc_result==expected_soc_result)
    

def test_chargerate_ok(chargeRate,expected_chargerate_result):
    resultant_chargerate_result=check_limits.Chargerate_Ok(chargeRate)
    assert(resultant_chargerate_result==expected_chargerate_result)

def test_battery_ok(temperature,soc,chargeRate,expected_result):
    resultant_result=check_limits.battery_Ok(temperature,soc,chargeRate)
    assert(resultant_result==expected_result)
    
def test_temp_tolerance(temperature,expected_temptolerance_result):
    resultant_temptolerance_result=check_limits.check_temp_tolerance(temperature,)
    assert(resultant_temptolerance_result==expected_temptolerance_result)
    
def test_soc_tolerance(soc,expected_soctolerance_result):
    resultant_soctolerance_result=check_limits.check_soc_tolerance(soc)
    assert( resultant_soctolerance_result==expected_soctolerance_result)
    
def test_chargerate_tolerance(chargeRate,expected_chargeRatetolerance_result):
    resultant_chargeratetolerance_result=check_limits.check_chargerate_tolerance(chargeRate)
    assert(resultant_chargeratetolerance_result==expected_chargeRatetolerance_result)
    


    
if __name__ == '__main__':
    #temperature validation
    test_temperature_ok(0,True)
    test_temperature_ok(45,True)
    test_temperature_ok(-1,False)
    test_temperature_ok(60,False)
    
    #SOC validation
    test_SOC_ok(25,True)
    test_SOC_ok(40,True)
    test_SOC_ok(10,False)
    test_SOC_ok(90,False)
    
    #Charge rate validation
    test_chargerate_ok(0.5,True)
    test_chargerate_ok(0.4,True)
    test_chargerate_ok(0.9,False)
    test_chargerate_ok(1,False)
    
    #Battery_ok validation
    test_battery_ok(25,70,0.7,True)
    test_battery_ok(-6,10,0.6,False)
    test_battery_ok(25,70,0.7,True)
    test_battery_ok(25,30,0.6,True)
    test_battery_ok(22,70,0.5,True)
    test_battery_ok(-6,10,0.6,False)
    test_battery_ok(25,106,0.8,False)
    test_battery_ok(20,80,0.9,False)
    
  #temperature_tolerance validation
    test_temp_tolerance(0,"English","Warning:Temperature Approaching low")
    test_temp_tolerance(1.25,"English","Warning:Temperature Approaching low")
    test_temp_tolerance(43,"English","Warning:Temeprature Approaching high")
    test_temp_tolerance(45,"English","Warning:Temeprature Approaching high")
    test_temp_tolerance(30,"English","Temperature is OK")
    test_temp_tolerance(35,"English","Temperature is OK")
  
    
    #soc_tolerance validation
    test_soc_tolerance(20,"English","Warning:SOC Approaching discharge")
    test_soc_tolerance(24,"English","Warning:SOC Approaching discharge")
    test_soc_tolerance(77,"English","Warning:SOC Approaching charge-peak")
    test_soc_tolerance(80,"English","Warning:SOC Approaching charge-peak")
 
    
    #chargerate_tolerance validation
    test_chargerate_tolerance(0.76,"English", "Warning:Charge rate Approaching peak")
    test_chargerate_tolerance(0.77, "English","Warning:Charge rate Approaching peak")
    test_chargerate_tolerance(0.9,"English","Warning:Charge Rate out of range")
    test_chargerate_tolerance(0.6,"English","Charge Rate is OK")
    test_chargerate_tolerance(0.5,"English","Charge Rate is OK")
  
    
    

    
