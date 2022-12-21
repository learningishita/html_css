import requests
import json
import csv

states = ["ANDAMAN AND NICOBAR ISLAND",
"ANDHRA PRADESH",
"ARUNACHAL PRADESH",
"ASSAM",
"BIHAR",
"CHANDIGARH",
"CHATTISHGARH",
"DELHI",
"DAMAN AND DIU",
"GOA",
"GUJRAT",
"HARYANA",
"HIMACHAL PRADESH",
"JHARKHAND",
"JAMMU KASHMIR",
"KARNATAKA",
"KERALA",
"LADAKH",
"LAKSHDWEEP",
"MAHARASHTRA",
"MANIPUR",
"MADHYA PRADESH",
"MEGHALAYA",
"MIZORAM",
"NAGALAND",
"ODISHA",
"PONDICHERRY",
"PUNJAB",
"RAJASTHAN",
"SIKKIM",
"TAMIL NADU",
"TELANGANA",
"TRIPURA",
"UTTAR PRADESH",
"UTTARAKHAND",
"WEST BENGAL",
]
for i in states:
    print("********New State*****************")
#    f = open(i+'.csv','w',encoding="utf-8")
#    writer = csv.writer(f)
#    writer.writerow(['Name','Email','Phone Number','State Name'])
    for j in range(100):        
        response_API = requests.get('https://randomuser.me/api/')
        data = response_API.text
        parse_json = json.loads(data)
        name = parse_json["results"][0]["name"]["title"]+" "+parse_json["results"][0]["name"]["first"]+" "+parse_json["results"][0]["name"]["last"]
        email = parse_json["results"][0]["email"]
        phone_number = parse_json["results"][0]["phone"] 
#        writer.writerow([str(name) , str(email) , str(phone_number),i])
        htmlstr= "<tr><td>"+name+"</td><td>"+email+"</td><td>"+phone_number+"</td><td>"+i+"</td></tr>"
        print(htmlstr)
#<tr><td>Name</td><td>email</td><td>Phone Number</td><td>State</td></tr>