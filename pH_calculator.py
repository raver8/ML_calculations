
import json
import numpy as np
import math 

def alpha(file_name):

    with open(file_name, "r",  encoding = 'utf-8') as file:
    
        json_data = json.load(file)
    
    filtered_data = []
    
    for record in json_data:
        
        filtered_data.append(record["aqueous phase"])

    #this will print a list of associated name-value pairs of all data within the aqueous phase key
    
    for lst in filtered_data:
        
        pH = filtered_data[1]
        
        if isinstance(pH, (int, float)):
            
            pH = np.array("pH", dtype=float)
            
            h3o = -math.log10(pH)
            
            return h3o
        
        elif:
            
            for lst_2 in filtered_data:
                
                pH = filtered_data [0]

#trying to access all information within "solutes" in the list containing all aqueous phase data, to access concentration of strong acid and use that for pH
            

alpha("all_TPEN_DERIVATIVE_records.json")
