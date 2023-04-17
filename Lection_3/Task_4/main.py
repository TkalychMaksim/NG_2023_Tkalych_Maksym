import requests
user_url = input("Enter the url list separated by commas: ").split(',')

for sites in user_url:
        answer = requests.get(sites)
        if answer.status_code == 200:
            print("Status: OK")
        else:
            print("Status: Failed") 

