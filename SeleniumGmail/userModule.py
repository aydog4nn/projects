import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class User():

    def username(self,username):


        if len(username) < 2:
            print("Kullanıcı adınızın uzunluğu yetersiz.")
            time.sleep(3)
            return False
        elif len(username) > 25:
            return False
        else:
            return username

    def name(self,name):
        
        if name.isalpha() == True:
            return name
        else:
            print("Yanlış tuşlama yaptınız!\nTekrar giriniz.")
            time.sleep(3)
            return False

    def mail(self,mail):

        if mail.endswith("@gmail.com"):
            return mail
        else:
            print("Lütfen düzgün bir mail giriniz.")
            return False

    def password(self,password,confirm):

        if password == confirm:
            return password
        else:
            print("Parolalar eşleşmiyor.")
            return False

    def login(self,username,password):

        return username,password


