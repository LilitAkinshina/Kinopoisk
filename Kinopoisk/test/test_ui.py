from selenium.webdriver.common.by import By
from constants import Test_URL
import allure


@allure.title("Поиск фильма на кириллице ")
@allure.description("Тест поиск фильма на кириллице")
@allure.severity("Критический")
def test_search_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Начало")
    driver.find_element(By.ID, "suggest-item-film-447301").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Начало (2010)"


@allure.title("Поиск фильма на латинице")
@allure.description("Тест поиск фильма на латинице")
@allure.severity("Критический")
def test_search_english_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Inception")
    driver.find_element(By.ID, "suggest-item-film-447301").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Начало (2010)"


@allure.title("Поиск фильма на транслите")
@allure.description("Тест поиск фильма на транслите")
@allure.severity("Критический")
def test_search_translit_film(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Nachalo 2010")
    driver.find_element(By.ID, "suggest-item-film-447301").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Начало (2010)"


@allure.title("Поиск персоны на кириллице")
@allure.description("Тест поиск персоны на кириллице")
@allure.severity("Критический")
def test_search_person(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Эди Седжвик")
    driver.find_element(By.ID, "suggest-item-person-131243").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text == "Эди Седжвик"


@allure.title("Поиск персоны на латинице")
@allure.description("Тест поиск персоны на латинице")
@allure.severity("Критический")
def test_search_person_english(driver):
    driver.get(Test_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Edie Sedgwick")
    driver.find_element(By.ID, "suggest-item-person-131243").click()
    assert driver.find_element(
        By.CSS_SELECTOR, "h1[data-tid='f22e0093']").text == "Эди Седжвик"
