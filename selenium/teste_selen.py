import time  
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.alert import Alert  
  
# Configurar o caminho para o driver do Chrome  
caminho_driver = r"..\\selenium\\chromedriver-win64\\chromedriver.exe"  
  
# Configurar as opções do ChromeDriver  
options = Options()  
options.add_argument("--no-sandbox")  
  
# Criar uma instância do Service  
service = Service(caminho_driver)  
  
# Criar uma instância do driver do Selenium usando o ChromeDriver e as opções configuradas  
driver = webdriver.Chrome(service=service, options=options)
  
# Executar o teste 3 vezes  
for i in range(3):  
    print(f"Executando teste {i+1}...")  
      
    # Configurar a porta para cada instância do Chrome  
    porta_debug = 9222 + i  
    options.add_argument(f"--remote-debugging-port={porta_debug}")  
  
    # Criar uma instância do Service  
    service = Service(caminho_driver)  
  
    # Criar uma instância do driver do Selenium usando o ChromeDriver e as opções configuradas  
    driver = webdriver.Chrome(service=service, options=options)  
  
    #Escrever seu teste usando os métodos e classes fornecidos pelo Selenium  
    try:  
        # Abrir a página no navegador  
        driver.get("http://127.0.0.1:5500/sample-exercise.html")  
        time.sleep(5)  # Pausa de 5 segundo 
    
        # Clicar no botão "generate"  
        botao_generate = driver.find_element(By.NAME, "generate")  
        botao_generate.click()  
        time.sleep(5)  # Pausa de 5 segundo 
    
        # Capturar o código gerado  
        codigo_gerado = driver.find_element(By.ID, "my-value").text  
    
        # Preencher o campo de texto com o código gerado  
        campo_texto = driver.find_element(By.ID, "input")  
        campo_texto.clear()  
        campo_texto.send_keys(codigo_gerado)  
    
        # Clicar no botão "test"  
        botao_test = driver.find_element(By.NAME, "button")  
        botao_test.click()  
        time.sleep(5)  # Pausa de 5 segundo 

    
        # Aceitar o alerta  
        alert = Alert(driver)  
        alert.accept()  
        time.sleep(5)  # Pausa de 5 segundo 

    
        # Capturar a mensagem exibida  
        mensagem = driver.find_element(By.ID, "result").text  
    
        # Verificar se a mensagem está correta  
        mensagem == "It works! " + codigo_gerado + "!"
    
    finally:  
        # Fechar o navegador e encerrar o driver  
        driver.quit()  

print(f"Teste {i+1} concluído.")