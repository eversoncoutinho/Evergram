from time import sleep
from selenium import webdriver
from credentials import Usuario
from selenium.webdriver.firefox.options import Options

'''
Para baixar o Feirefox webdriver
wget https:// caminho do git
tar xzf arquivo.tar.gz
sudo mv geckodriver /usr/bin/geckodriver 
'''

options = Options()
options.headless = True

#browser = webdriver.Firefox(options=options) #acessar o firefox

browser = webdriver.Firefox() #mais simples
browser.implicitly_wait(5) #espera 5 s para carregar qualquer coisa
browser.get(Usuario.url) #acessar a url
#login_link = browser.find_element_by_xpath("//a[text()='Log in']"#encontra o elemento <a> cujo texto é igual a Log in suando xPath.
#login_link.click()

sleep(2)
username_input = browser.find_element_by_css_selector("input[name='email']") #encontra o username input pelo css. 
                                                                                #Verifique o name inspecionando a página

password_input = browser.find_element_by_css_selector("input[name='password']") #encontra o username input pelo css. 
                                                                                #Verifique o name inspecionando a página

#preenchimento dos campos
username_input.send_keys(Usuario.username)
password_input.send_keys(Usuario.password)

#procura do botão entrar
login_button = browser.find_element_by_xpath("//button[@type='button']")
login_button.click()



browser.close()
print("Fim do programa")
