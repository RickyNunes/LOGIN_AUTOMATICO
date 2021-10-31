import sched, time, threading, sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




#Tempo para carregar a página


while (True):
    navegador= webdriver.Chrome()
    navegador.get("INSIRA O LINK DO SITE EX: https://www.facebook.com/")
    

    time.sleep(8) #Tempo para acessar a Página
    
    #Procurar o id ou então a classificação do login e da senha
    usuario = navegador.find_element_by_name("INSIRA O NAME DO CAMPO")
    senha = navegador.find_element_by_name("INSIRA O NAME DO CAMPO")

    #Preencher o campo de login/senha
    usuario.send_keys("INSIRA O SEU USURÁRIO")
    senha.send_keys("INSIRA A SUA SENHA")
    
    time.sleep(8)#Tempo para carregar a Página
   
    #Localizar o botão de enviar e executar
    logar= navegador.find_element_by_xpath("//*[@type='submit']")
    logar.submit()

    time.sleep(15)
    
    navegador.close()
    break




    
    



    








