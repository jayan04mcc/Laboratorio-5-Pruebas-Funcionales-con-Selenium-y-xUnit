import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Especifica la ruta al ejecutable de ChromeDriver
        chrome_path = './chromedriver-win64/chromedriver.exe'

        # Configura el controlador de Chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Opcional: maximizar la ventana al inicio

        # Inicializa el navegador Chrome
        service = Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def tearDown(self):
        # Cierra el navegador al finalizar
        self.driver.quit()
    
    def test_run_test(self):
        self.run_test("https://www.calculator.net/percent-calculator.html", "50", "200", "100")

    def test_run_test2(self):
        self.run_test_2("https://www.calculator.net/percent-calculator.html", "100", "20", "20")

    def test_run_test3(self):
        self.run_test_3("https://www.calculator.net/percent-calculator.html", "300", "15", "2000%")

    def test_run_test4(self):
        self.run_test_4("https://www.calculator.net/percent-calculator.html", "500", "10", "5000")
        
    def test_run_test5(self):
        self.run_test_5("https://www.calculator.net/percent-calculator.html", "100", "100", "0%")

    def run_test(self, url, input1, input2, expected_result):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "cpar1"))).send_keys(input1)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "cpar2"))).send_keys(input2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "x"))).click()
            time.sleep(2)
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
            self.assertEqual(result, expected_result, f"El resultado esperado no coincide. Resultado actual: {result}")
            print("Prueba 1 exitosa!")
        except Exception as e:
            print(f"Error en la prueba 1: {str(e)}")

    def run_test_2(self, url, input1, input2, expected_result):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c21par1"))).send_keys(input1)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c21par2"))).send_keys(input2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[2]/table/tbody/tr/td[2]/input[2]'))).click()
            time.sleep(2)
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
            self.assertEqual(result, expected_result, f"El resultado esperado no coincide. Resultado actual: {result}")
            print("Prueba 2 exitosa!")
        except Exception as e:
            print(f"Error en la prueba 2: {str(e)}")

    def run_test_3(self, url, input1, input2, expected_result):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c22par1"))).send_keys(str(input1))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c22par2"))).send_keys(str(input2))

    
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[3]/table/tbody/tr/td[2]/input[2]'))).click()
            time.sleep(2)
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
            assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
            print("Prueba 3 exitosa!")
        except Exception as e:
            print(f"Error en la prueba 3: {str(e)}")
        
    def run_test_4(self, url, input1, input2, expected_result):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c23par1"))).send_keys(str(input1))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c23par2"))).send_keys(str(input2))

    
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[4]/table/tbody/tr/td[2]/input[2]'))).click()
            
            time.sleep(2)
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
            assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
            print("Prueba 4 exitosa!")
        except Exception as e:
            print(f"Error en la prueba 4: {str(e)}")
        
    def run_test_5(self, url, input1, input2, expected_result):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c3par1"))).send_keys(input1)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "c3par2"))).send_keys(input2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form[5]/table/tbody/tr[3]/td/input[2]'))).click()
            time.sleep(2)
            result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "b"))).text
            assert result == expected_result, f"El resultado esperado no coincide. Resultado actual: {result}"
            print("Prueba 5 exitosa!")   
        except Exception as e:
            print(f"Error en la prueba 5: {str(e)}")
        finally:
            self.driver.quit()
     
if __name__ == "__main__":
    unittest.main()
