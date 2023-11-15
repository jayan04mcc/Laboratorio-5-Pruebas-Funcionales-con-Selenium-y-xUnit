from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver(chrome_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def run_test(driver, url, input1, input2, expected_result):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cpar1"))).send_keys(input1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cpar2"))).send_keys(input2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "x"))).click()
        time.sleep(2)
        result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
        assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
        print("Prueba 1 exitosa!")
    except Exception as e:
        print(f"Error en la prueba 1: {str(e)}")
    # No cierra el navegador aquí para permitir la ejecución de run_test2
def run_test2(driver, url, input1, input2, expected_result):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c21par1"))).send_keys(input1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c21par2"))).send_keys(input2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[2]/table/tbody/tr/td[2]/input[2]'))).click()
        time.sleep(2)
        result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
        assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
        print("Prueba 2 exitosa!")
    except Exception as e:
        print(f"Error en la prueba 2: {str(e)}")
    # No cierra el navegador aquí para permitir la ejecución de run_test2
def run_test3(driver, url, input1, input2, expected_result):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c22par1"))).send_keys(str(input1))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c22par2"))).send_keys(str(input2))

   
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[3]/table/tbody/tr/td[2]/input[2]'))).click()
        time.sleep(2)
        result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
        assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
        print("Prueba 3 exitosa!")
    except Exception as e:
        print(f"Error en la prueba 3: {str(e)}")
    # No cierra el navegador aquí para permitir la ejecución de run_test2
def run_test4(driver, url, input1, input2, expected_result):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c23par1"))).send_keys(str(input1))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c23par2"))).send_keys(str(input2))

   
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[4]/table/tbody/tr/td[2]/input[2]'))).click()
        
        time.sleep(2)
        result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
        assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
        print("Prueba 4 exitosa!")
    except Exception as e:
        print(f"Error en la prueba 4: {str(e)}")
    # No cierra el navegador aquí para permitir la ejecución de run_test2
def run_test5(driver, url, input1, input2, expected_result):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c3par1"))).send_keys(input1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "c3par2"))).send_keys(input2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[5]/table/tbody/tr[3]/td/input[2]'))).click()
        time.sleep(2)
        result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
        assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
        print("Prueba 5 exitosa!")   
    except Exception as e:
        print(f"Error en la prueba 5: {str(e)}")
    finally:
        driver.quit()

chrome_path = './chromedriver-win64/chromedriver.exe'
driver = setup_driver(chrome_path)

try:
    ACTION_1="https://www.calculator.net/percent-calculator.html"
    run_test(driver, ACTION_1, "50", "200", "100")
    run_test2(driver, ACTION_1, "100", "20", "20")
    run_test3(driver, ACTION_1, "300", "15", "2000%")
    run_test4(driver, ACTION_1, "500", "10", "5000")
    run_test5(driver, ACTION_1, "100", "100", "0%")
except Exception as e:
    print(f"Error general: {str(e)}")
finally:
    # Cierra el navegador al finalizar ambas pruebas
    driver.quit()
