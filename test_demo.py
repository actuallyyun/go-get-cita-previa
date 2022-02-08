# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDemo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # Enter the cita previa page
        self.driver.get(
            "https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus")
        self.driver.set_window_size(1452, 1018)
        # Add scroll if selenium didn't record it
        self.driver.execute_script("window.scrollTo(0,807)")
        self.driver.find_element(By.ID, "submit").click()

        # Select your province and enter the page
        self.driver.find_element(By.ID, "form").click()
        dropdown = self.driver.find_element(By.ID, "form")
        dropdown.find_element(By.XPATH, "//option[. = 'Tarragona']").click()
        self.driver.find_element(By.ID, "btnAceptar").click()

        # Choose the police station
        # Add scroll if selenium didn't record it
        self.driver.execute_script("window.scrollTo(0,807)")
        self.driver.find_element(By.ID, "sede").click()
        dropdown = self.driver.find_element(By.ID, "sede")
        dropdown.find_element(
            By.XPATH, "//option[. = 'CNP Comisaría Local de Reus, General Moragues, 54']").click()
        self.driver.find_element(By.ID, "tramiteGrupo[0]").click()

        # Choose which category
        dropdown = self.driver.find_element(By.ID, "tramiteGrupo[0]")
        dropdown.find_element(
            By.XPATH, "//option[. = 'POLICIA-TOMA DE HUELLAS (EXPEDICIÓN DE TARJETA) Y RENOVACIÓN DE TARJETA DE LARGA DURACIÓN']").click()
        self.driver.find_element(By.ID, "btnAceptar").click()
        # Add scroll if selenium didn't record it
        self.driver.execute_script("window.scrollTo(0,1000)")
        self.driver.find_element(By.ID, "btnEntrar").click()

        # Enter your personal info
        self.driver.find_element(By.ID, "txtIdCitado").click()
        self.driver.find_element(By.ID, "txtIdCitado").send_keys("Y7602240H")
        self.driver.find_element(By.ID, "txtDesCitado").send_keys("YOURNAME")
        self.driver.find_element(By.ID, "txtPaisNac").click()
        dropdown = self.driver.find_element(By.ID, "txtPaisNac")
        dropdown.find_element(By.XPATH, "//option[. = 'ALEMANIA']").click()
        self.driver.find_element(By.ID, "txtFecha").click()

        # Better type in the date-time
        self.driver.find_element(By.ID, "txtFecha").send_keys("21/05/2022")
        self.driver.find_element(By.CSS_SELECTOR, "#divFecha span").click()
        self.driver.find_element(By.ID, "btnEnviar").click()
        self.driver.find_element(By.ID, "btnEnviar").click()
        self.driver.execute_script("window.scrollTo(0,201)")
        # Sometimes you have to tell it to scroll more, feel free to add another line
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);")

        self.driver.find_element(By.ID, "txtTelefonoCitado").click()
        self.driver.find_element(
            By.ID, "txtTelefonoCitado").send_keys("657177588")
        self.driver.find_element(By.ID, "emailUNO").send_keys(
            "this.jiyu@gmail.com")
        self.driver.find_element(By.ID, "emailDOS").send_keys(
            "this.jiyu@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".fld:nth-child(5)").click()
        self.driver.find_element(By.ID, "btnSiguiente").click()

        # If no cita, driver quits and starts again
        if "En este momento no hay citas disponibles." in self.driver.page_source:

            self.driver.find_element(By.ID, "btnSubmit").click()
            self.driver.close()

        # If there is cita, driver waits
        else:
            time.sleep(6000)
