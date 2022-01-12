import sched, time, threading, sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def AcessarSite():
    while (True):
        
        #OPTIONS EXECUTA OS COMANDOS EM MODO HEADLESS
        #PARA DESABILITAR E PODER VER TODOS OS PROCESSOS BASTA UTILIZAR APENAS O COMANDO  - navegador= webdriver.Chrome() - ELIMINANDO AS LINHAS DE OPTIONS.
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        navegador= webdriver.Chrome(chrome_options=options)
        
    
        #navegador= webdriver.Chrome()
        
        navegador.get("https://app.pontomaisweb.com.br/#/acessar")
        time.sleep(8)
        return navegador
    

                        #Preencher o campo de login/senha
    
def Login(navegador):
    usuario = navegador.find_element_by_name("login")   #Procurar o id ou então a classificação do login e da senha
    senha = navegador.find_element_by_name("password")
    usuario.send_keys("50691152861")
    senha.send_keys("Sup#R1CKY041620")
    time.sleep(3)

                        #Localizar o botão de enviar e executar
    
def RegistrarPonto(navegador):
    logar= navegador.find_element_by_xpath("//*[@type='submit']")
    logar.submit()
    time.sleep(15)
    log= navegador.find_element_by_css_selector("i.mr4.icon-pontomais-clock-in-out").click()
    time.sleep(8)


                        #fechar o brownser
    
def FecharBrowser(navegador):   
    navegador.close()


Navevagor= AcessarSite()
Login(Navevagor)
RegistrarPonto(Navevagor)
FecharBrowser(Navevagor)
    
    



    












    
    



    








