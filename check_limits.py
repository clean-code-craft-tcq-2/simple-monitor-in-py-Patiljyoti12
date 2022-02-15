#Temperature_tolerance
def check_temp_tolerance(temperature,language):
    if (temperature<0 and  temperature>45):
        if (language == 'English'):
            temp_message="Temperature out of range"
        elif (language == 'German'):
            temp_message = "Temperatur außerhalb des Bereichs" 
        elif (language=="Spanish"):
            temp_message="Temperatura fuera de rango"
    elif (temperature>=0 and temperature<=(0+0.05*45)):
        if (language == 'English'):
            temp_message="Warning:Temperature Approaching low"
        elif (language == 'German'):
            temp_message = "Warnung: Temperatur nähert sich niedrig" 
        elif (language=="Spanish"):
            temp_message="Advertencia: temperatura acercándose a baja" 
    elif (temperature >=(45-0.05*45)and temperature<=45):
        if (language == 'English'):
            temp_message="Warning:Temeprature Approaching high"
        elif (language == 'German'):
            temp_message = "Warnung: Temperatur nähert sich hoch" 
        elif (language=="Spanish"):
            temp_message="Advertencia: temperatura acercándose a un nivel alto" 
    else:
        if (language == 'English'):
            temp_message="Temperature is OK"
        elif (language == 'German'):
            temp_message = "Temperatur ist in Ordnung" 
        elif (language=="Spanish"):
            temp_message="La temperatura está bien" 
        
    return temp_message
   
#soc_tolerance
def check_soc_tolerance(soc,language):
    if(soc<20 and soc>80):
        if (language == 'English'):
            soc_message="State of Charge out of range"
        elif (language == 'German'):
            soc_message= "Ladezustand außerhalb des Bereichs"
        elif (language=="Spanish"):
            soc_message="Estado de carga fuera de rango" 
    elif (soc>=20 and soc<=(20+0.05*80)): 
        if (language == 'English'):
            soc_message="Warning:SOC Approaching discharge"
        elif (language == 'German'):
            soc_message= "Warnung: SOC Entladung nähert sich"
        elif (language=="Spanish"):
            soc_message= "Advertencia: SOC acercándose a la descarga" 
    elif(soc>=(80-0.05*80) and soc<=80):
        if (language == 'English'):
            soc_message="Warning:SOC Approaching charge-peak"
        elif (language == 'German'):
            soc_message= "Warnung:SOC Ladespitze nähert sich"
        elif (language=="Spanish"):
            soc_message="Advertencia: SOC se acerca al pico de carga" 
    else:
        if (language == 'English'):
            soc_message="State of Charge is OK"
        elif (language == 'German'):
            soc_message= "Ladezustand ist OK" 
        elif (language=="Spanish"):
            soc_message="El estado de carga es correcto"
    
    return soc_message
    
#chargerate_tolerance
def check_chargerate_tolerance(chargeRate,language):
    if(chargeRate>0.8):
        if (language == 'English'):
           chargerate_message="Warning:Charge Rate out of range"   
        elif (language == 'German'):
           chargerate_message="Warnung: Laderate außerhalb des Bereichs"
        elif (language=="Spanish"):
           chargerate_message= "Advertencia: Tasa de carga fuera de rango" 
    elif(chargeRate>=(0.8-0.05*0.8) and chargeRate<=0.8):
        if (language == 'English'):
            chargerate_message= "Warning:Charge rate Approaching peak"
        elif (language == 'German'):
            chargerate_message="Warnung: Laderate nähert sich dem Höhepunkt" 
        elif (language=="Spanish"):
            chargerate_message="Advertencia: Tasa de carga acercándose al pico" 
    else:
        if (language == 'English'):
           chargerate_message="Charge Rate is OK"
        elif (language == 'German'):
           chargerate_message="Laderate ist OK" 
        elif (language=="Spanish"):
            chargerate_message="La tasa de carga está bien" 
            
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
