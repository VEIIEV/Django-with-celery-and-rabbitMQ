import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

INPUTS = ['1', '1', '1@mail.ru', 1, 1, 1]


@pytest.fixture()
def get_cart_page():
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/shop/')
    driver.implicitly_wait(1)
    # assert 'Products' in driver.title
    elem2 = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[1]/a[2]', )
    elem2.click()
    add_to_cart = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/form/input[3]')
    add_to_cart.click()
    add_to_cart = driver.find_element(by=By.XPATH, value='//*[@id="content"]/p/a[2]')
    add_to_cart.click()
    form = driver.find_element(by=By.CLASS_NAME, value='order-form').find_elements(by=By.TAG_NAME, value='p')
    return form, driver


# first_name = driver.find_element(by=By.XPATH, value='//*[@id="id_first_name"]')
# first_name.clear()
# first_name.send_keys('1')
#
# last_name = driver.find_element(by=By.ID, value='id_last_name')
# last_name.clear()
# last_name.send_keys('1')
#
# email = driver.find_element(by=By.ID, value='id_email')
# email.clear()
# email.send_keys('1@mail.ru')
#
# address = driver.find_element(by=By.ID, value='id_address')
# address.clear()
# address.send_keys('1@mail.ru')
#
# postal_code = driver.find_element(by=By.ID, value='id_postal_code')
# postal_code.clear()
# postal_code.send_keys('1')
#
# city = driver.find_element(by=By.ID, value='id_city')
# city.clear()
# city.send_keys('1')


def test_create_order(get_cart_page):
    form = get_cart_page[0]
    driver = get_cart_page[1]
    counter = 0
    for element in form[:-1]:
        element = element.find_element(by=By.TAG_NAME, value='input')
        element.clear()
        element.send_keys(INPUTS[counter])
        counter += 1

    submit = driver.find_element(by=By.XPATH, value='//*[@id="content"]/form/p[7]/input')
    submit.click()
    assert driver.title == 'Thank you'
