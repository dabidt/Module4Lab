import requests
from requests.auth import HTTPBasicAuth
"""
This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.
"""

#Creates empty array named addresses
addresses = []

#asks for user input on whether they have an email, puts user input into variable more
more = input("Do you have an email address to enter (y/n)? ")

#while loop that runs if more is y. it asks for the user to input their email, then adds the email to the address array
while more == "y":
  email = input("Enter the address: ")
  addresses.append(email)
#asks the user if they have more email addresses
  more = input("Do you have another address(y/n)? ")
  #if the user input (more) is not y and is N then the loop breaks
  while more != "y":
      if more == "n":
          break
  # if the user inputs something other than y or n then this will be displayed
      else:
          more = input("Please enter a y or n: ");

USERNAME = input("Enter webex teams username")
PASS = input("Enter webex teams pass")

url = "https://webexapis.com/v1/access_token"
headers = {'Content-type': 'application/json'}
response = requests.post(url, auth=HTTPBasicAuth(USERNAME, PASS), headers = headers, verify=false)
token = response.json()['Token']

url2 = "https://webexapis.com/v1/rooms"
roomtitle = input("Enter new room title")
response2 = requests.post(url2,headers = headers, authorization = token, title = roomtitle, verify=false)
roomID = response2.json()['roomId']
#need to create loop here to go through the array emails one by one
url3 = "https://webexapis.com/v1/memberships"
requests.post(url3,headers = headers, authorization = token, roomId= roomID, personEmail = email, verify=false)




#prints the array of email addresses
print(addresses)
