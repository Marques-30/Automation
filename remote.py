from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import getpass
import requests
from bs4 import BeautifulSoup

user = raw_input("username: ")
pwd = getpass.getpass('Password: ')

driver=webdriver.Ie("C:\Users\Butilm01\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
driver.get('www.linkedIn.com')

username = driver.find_element_by_id("login-email")
username.send_keys(user)

password = driver.find_element_by_id("login-password")
password.send_keys(pwd)

driver.find_element_by_id("login-submit").click()
print "Access Granted"
search=driver.find_element_by_name("search")
search.send_keys("Recuiter")

link = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx?display=50"

html = requests.get(link).text

"""If you do not want to use requests then you can use the following code below 
   with urllib (the snippet above). It should not cause any issue."""
soup = BeautifulSoup(html, "lxml")
res = soup.findAll("article", {"class": "listingItem"})
for r in res:
    print("Company Name: " + r.find('a').text)
    print("Address: " + r.find("div", {'class': 'address'}).text)
    print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)