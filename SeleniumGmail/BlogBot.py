import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from userModule import User


class Bot(User):

    def __init__(self):

        super().__init__()

    def register(self,name,username,adres,password,confirm):

        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:5000/")
        registerPath = self.browser.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul[2]/li[2]/a")
        time.sleep(2)
        registerPath.click()

        isim = self.browser.find_element(By.XPATH,"//*[@id='name']")
        kullanıcıAdı = self.browser.find_element(By.XPATH,"//*[@id='username']")
        mail = self.browser.find_element(By.XPATH,"//*[@id='mail']")
        sifre = self.browser.find_element(By.XPATH,"//*[@id='password']")
        dogrulama = self.browser.find_element(By.XPATH,"//*[@id='confirm']")

        time.sleep(3)

        isim.send_keys(self.name(name))
        kullanıcıAdı.send_keys(self.username(username))
        mail.send_keys(self.mail(adres))
        sifre.send_keys(self.password(password,confirm))
        dogrulama.send_keys(confirm)

        registerButton = self.browser.find_element(By.XPATH,"/html/body/div/form/button")
        time.sleep(2)
        registerButton.click()
        time.sleep(2)
        self.browser.close()

    def login(self,username,password):

        self.browser = webdriver.Chrome()
        self.browser.get("http://localhost:5000/")
        loginPath = self.browser.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul[2]/li[1]/a")
        loginPath.click()
        kullanıcıGiriş = self.browser.find_element(By.XPATH,"//*[@id='username']")
        şifreGiriş = self.browser.find_element(By.XPATH,"//*[@id='password']")
        loginButton = self.browser.find_element(By.XPATH,"/html/body/div/form/button")
        time.sleep(2)

        kullanıcıGiriş.send_keys(username)
        şifreGiriş.send_keys(password)

        time.sleep(2)
        loginButton.click()
        
        time.sleep(2)
        

    def addArticle(self,newTitle,newContent):

        print("Makale eklemek için giriş yapmanız gerekmektedir.")
        kullanıcıAdı = input("Kullanıcı Adı:")
        password = input("Şifre:")
        if self.username(kullanıcıAdı):
            self.login(kullanıcıAdı,password)
            
            dashboardPath = self.browser.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul[2]/li[1]/a")
            time.sleep(2)
            dashboardPath.click()
            addPath = self.browser.find_element(By.XPATH,"/html/body/div/a")
            time.sleep(2)
            addPath.click()

            title = self.browser.find_element(By.XPATH,"//*[@id='title']")
            content = self.browser.find_element(By.XPATH,"//*[@id='content']")
            time.sleep(2)

            title.send_keys(newTitle)
            content.send_keys(newContent)

            addButton = self.browser.find_element(By.XPATH,"/html/body/div/form/button")
            time.sleep(2)
            addButton.click()
        
        else:
            print("Kullanıcı adı ya da şifre hatalı!")
        
bot = Bot()

