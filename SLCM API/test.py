from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'txtUserId':'180907612', 
          'txtpassword':'Mitaspirant14@'
         }

# Post the payload to the site to log in
s = session.post("https://slcm.manipal.edu/loginForm.aspx", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://slcm.manipal.edu/studenthomepage.aspx')

soup = BeautifulSoup(s.text, 'html.parser')
print(soup)