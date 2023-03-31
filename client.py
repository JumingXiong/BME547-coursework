import requests

server = "http://vcm-7631.vm.duke.edu:5002"

r = requests.get(server + "/get_patients/jx132")
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_blood_type/M3")
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_blood_type/F8")
print(r.status_code)
print(r.text)

result = {"Name": "jx132", "Match": "Yes"}
r = requests.post(server + "/match_check", json = result)
print(r.status_code)
print(r.text)