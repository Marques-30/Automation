from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import requests

driver=webdriver.Ie("C:\Users\Butilm01\Downloads\IEDriverServer_x64_3.4.0\IEDriverServer.exe")
driver.get('https://sharepoint/sites/it/BIDMProdOps/DevOps/SprintPlan/_layouts/15/datasheetrevive/datasheet.aspx?List={28d88940-2e76-4b34-9b04-35a304674823}&View={36C8CB70-7D6B-46FD-A519-E7AA1C0E3219}')

driver.find_element_by_id("DeltaPlaceHolderSearchArea").click()

