from login import login
from time import sleep

login()
sleep(2)
contact = driver.find_element_by_link_text('/contact/list/')
contact.click()