await page.type('[name="user[email]"]', process.env.UNSPLASH_EMAIL)
await page.type('#user_password', process.env.UNSPLASH_EMAIL)















from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\users\Matheus\Desktop\geckodriver-v0.29.1-win64\geckodriver.exe")
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(3)
        botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        botao_login.click()
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_hastag('jogos')

    def comente_nas_fotos_com_a_hastag(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(3)

        for i in range(1,3):
            driver.execute_script('window.scroolTo(0, document.body.scrollHeight);')
            time.sleep(5)

MatheusBot = InstagramBot('cesinhatomabloqueio','moraes2204')
MatheusBot.login()

