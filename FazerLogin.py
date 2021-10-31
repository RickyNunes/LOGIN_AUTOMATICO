import sched, time, threading, sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




#Tempo para carregar a página


while (True):
    navegador= webdriver.Chrome()
    navegador.get("https://www.facebook.com/")
    

    time.sleep(8) #Tempo para acessar a Página
    
    #Procurar o id ou então a classificação do login e da senha
    usuario = navegador.find_element_by_name("email")
    senha = navegador.find_element_by_name("pass")

    #Preencher o campo de login/senha
    usuario.send_keys("henrique_estrelas@hotmail.com")
    senha.send_keys("hen456987")
    
    time.sleep(8)#Tempo para carregar a Página
   
    #Localizar o botão de enviar e executar
    logar= navegador.find_element_by_xpath("//*[@type='submit']")
    logar.submit()

    time.sleep(15)
    
    navegador.close()
    break




    
    



    








