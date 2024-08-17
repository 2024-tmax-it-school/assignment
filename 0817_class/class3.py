import json

json_file = "setting.json"

default_setting = {
    "volume" : 100,
    "light" : 100,
    "display" : "800x600"
}

display_sizes = ["1920x1090", "1280x920", "1024x768", "800x600"]

data = default_setting

try :
    data = json.load(open(json_file, "r"))
except FileNotFoundError:
    print("",end ="")
    

while 1 :     
    size = 0
    
    while 1 :
        size = int(input("volume : "))
        
        if size <0 or size >100 : 
            print("error!")
        else :break
        
    while 1 :
        light = int(input("light : "))
        if light <0 or light >100 : 
            print("error!")
        else : break
    
    while 1: 
        display = input ("display : ")
    
        if not(display in display_sizes):
            print("error!")
        else : break
            
    data["size"] = size
    data["light"] = light
    data["display"] = display
    
    with open(json_file, 'w') as outfile:
        json.dump(data, outfile)
    
    
    break
    


