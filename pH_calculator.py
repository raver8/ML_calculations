import json
import numpy as np
import math


def alpha():
    with open('all_TPEN_DERIVATIVE_records.json', 'r', encoding = 'utf8') as f:
        json_data = json.load(f)
    
        filtered_data = []

    for aqueous in json_data["aqueous phase"]:
        aqueous_data = {
            "solutes" == aqueous["solutes"],
            "pH" == aqueous["pH"],
            "volume" == aqueous["volume"],}
                        
    filtered_data.append(aqueous_data)
                    
    if isinstance("pH", (int, float)):
        pH = np.array(pH, dtype=float)
                        
        h3o = -math.log10(pH)

        return h3o
    print(h3o)

alpha()
        
