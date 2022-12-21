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
"WEST BENGAL"]

#<tr><th scope="row"><a href="xyz.html">Bihar</a></th></tr>
htmlStr1 = '<tr><th scope="row"><a href="'
htmlStr2= '">'
htmlStr3='</a></th></tr>'
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bootstrap demo</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>

<body>
  <nav class="navbar navbar-expand-lg" style="background-color: #e50e0e;">
    <div class="container-fluid">
      <a class="navbar-brand" href="https://herovired.com/"></a><img src="images/newlogo.png" width="180" height="50">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#" style="color: #f5f2f2;"><b>Home</b></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" style="color: #f5f2f2;"><b>More</b></a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">

            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="https://vlearn.herovired.com/local/learningpaths/view.php?id=85">Cloud
                  and DevOps Engineering: Batch 1</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><a class="dropdown-item" href="https://herovired.freshdesk.com/support/tickets/new">Raise a Ticket</a>
              </li>
              <li><a class="dropdown-item" href="https://herovired.com/">Hero Vired</a></li>
            </ul>
          </li>

        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit"
            style="color: #f5f2f2; border-color: #f8f9fa">Search</button>
        </form>
      </div>
    </div>
  </nav>
  </div>
  <div class="container" style = "width: 1000px;">
    <table style="margin-left: 50px; margin-top: 50px;"
      class=" table table-bordered  table-sm table-striped table-hover border border-dark">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Phone Number</th>
          <th scope="col">State</th>
        </tr>
      </thead>
      <tbody>"""
html_last_template ="""<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4"
    crossorigin="anonymous"></script>
  <script src="script.js">  </script>
</body>
</html>"""
f = open('state.csv','w',encoding="utf-8")
writer = csv.writer(f)
writer.writerow(['Name','Email','Phone Number','State Name'])
for i in states:
    print("********New State*****************")
    concatenated_htmlstr =""
    for j in range(100):        
        response_API = requests.get('https://randomuser.me/api/')
        data = response_API.text
        parse_json = json.loads(data)
        name = parse_json["results"][0]["name"]["title"]+" "+parse_json["results"][0]["name"]["first"]+" "+parse_json["results"][0]["name"]["last"]
        email = parse_json["results"][0]["email"]
        phone_number = parse_json["results"][0]["phone"] 
        writer.writerow([str(name) , str(email) , str(phone_number),i])
        htmlstr= "<tr><td>"+name+"</td><td>"+email+"</td><td>"+phone_number+"</td><td>"+i+"</td></tr>"
        print(htmlstr)
#<tr><td>Name</td><td>email</td><td>Phone Number</td><td>State</td></tr>
        concatenated_htmlstr = htmlstr + concatenated_htmlstr
    html_final_template = html_template+concatenated_htmlstr+html_last_template
    f = open(i+'.html', 'w',encoding="utf-8")
    f.write(html_final_template)
    f.close()
