state_to_abbrev = {'United States':'US','Alabama': 'AL','Alaska': 'AK','American Samoa': 'AS','Arizona': 'AZ',
                   'Arkansas': 'AR','California': 'CA','Colorado': 'CO', 'Connecticut': 'CT','Delaware': 'DE',
                   'District of Columbia': 'DC', 'Florida': 'FL','Georgia': 'GA','Guam': 'GU','Hawaii': 'HI', 
                   'Idaho': 'ID','Illinois': 'IL','Indiana': 'IN', 'Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY',
                   'Louisiana': 'LA', 'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA', 'Michigan': 'MI',
                   'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO', 'Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
                   'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC', 
                   'North Dakota': 'ND','Northern Mariana Islands':'MP','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR',
                   'Pennsylvania': 'PA','Puerto Rico': 'PR', 'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
                   'Tennessee': 'TN','Texas': 'TX','Utah': 'UT', 'Vermont': 'VT','Virgin Islands': 'VI','Virginia': 'VA',
                   'Washington': 'WA','West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY'}
                   
abbrev_to_state = dict(map(reversed, state_to_abbrev.items()))

abbrev_to_fips = {"AL":"01","AK":"02","AZ":"04","AR":"05","CA":"06","CO":"08","CT":"09","DE":"10","DC":"11","FL":"12",
                  "GA":"13","HI":"15","ID":"16","IL":"17","IN":"18","IA":"19","KS":"20","KY":"21","LA":"22","ME":"23",
                  "MD":"24","MA":"25","MI":"26","MN":"27","MS":"28","MO":"29","MT":"30","NE":"31","NV":"32","NH":"33",
                  "NJ":"34","NM":"35","NY":"36","NC":"37","ND":"38","OH":"39","OK":"40","OR":"41","PA":"42","RI":"44",
                  "SC":"45","SD":"46","TN":"47","TX":"48","UT":"49","VT":"50","VA":"51","WA":"53","WV":"54","WI":"55",
                  "WY":"56","PR":"72"}

abbrev_to_crs = {'WA': 'EPSG:2285', 'DE': 'EPSG:2235', 'DC': 'EPSG:2283', 'WI': 'EPSG:2288', 'WV': 'EPSG:2857', 'HI': 'EPSG:2786','FL': 'EPSG:2778', 'WY': 'EPSG:2863', 
               'PR': 'EPSG:2866', 'NJ': 'EPSG:2824', 'NM': 'EPSG:2258', 'TX': 'EPSG:2277','LA': 'EPSG:2801', 'NC': 'EPSG:2264', 
               'ND': 'EPSG:2266', 'NE': 'EPSG:2819','TN': 'EPSG:2204', 'NY': 'EPSG:2261','PA': 'EPSG:2272', 'AK': 'EPSG:3467', 
                'NV': 'EPSG:2821', 'NH': 'EPSG:2823', 'VA': 'EPSG:2284', 'CO': 'EPSG:2232','CA': 'EPSG:2769', 'AL': 'EPSG:2759',  'AR': 'EPSG:2765', 'VT': 'EPSG:2852', 'IL': 'EPSG:2790', 
               'GA': 'EPSG:2239','IN': 'EPSG:2244','IA': 'EPSG:2795', 'MA': 'EPSG:2249','AZ': 'EPSG:2223', 'ID': 'EPSG:2242', 'CT': 'EPSG:2775','ME': 'EPSG:2802', 'MD': 'EPSG:2804', 'OK': 'EPSG:2268', 
               'OH': 'EPSG:2835', 'UT': 'EPSG:2280','MO': 'EPSG:2816','MN': 'EPSG:2811', 'MI': 'EPSG:2252', 'RI': 'EPSG:2840', 'KS': 'EPSG:2796', 'MT': 'EPSG:2256', 
               'MS': 'EPSG:2254','SC': 'EPSG:2273', 'KY': 'EPSG:2205', 'OR': 'EPSG:2991', 'SD': 'EPSG:2266'}

abbrevs = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
          "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", 
          "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA","PR",
          "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
