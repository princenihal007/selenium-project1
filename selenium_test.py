from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(r"file:///C:/Users/princ/OneDrive/ドキュメント/Companies Assignments/frugal testing assignment/index.html")

print(driver.title)
print(driver.current_url)

time.sleep(1)

driver.find_element(By.ID, "fname").send_keys("John")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")
driver.find_element(By.ID, "phone").send_keys("+919876543210")

driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "cpassword").send_keys("Password123")
driver.find_element(By.ID, "terms").click()

driver.find_element(By.ID, "fname").click()
time.sleep(1)

driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("error-state.png")


driver.refresh()
time.sleep(1)

driver.refresh()
time.sleep(1)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(r"file:///C:/Users/princ/OneDrive/ドキュメント/Companies Assignments/frugal testing assignment/index.html")
time.sleep(3)

def trigger():
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.TAB)
    time.sleep(0.3)

print(driver.title)
print(driver.current_url)

# ---------- NEGATIVE SCENARIO ----------
driver.find_element(By.ID, "fname").send_keys("John")
trigger()

driver.find_element(By.ID, "email").send_keys("john@gmail.com")
trigger()

driver.find_element(By.ID, "phone").send_keys("+919876543210")
trigger()

driver.find_element(By.XPATH, "//input[@value='Male']").click()
trigger()

driver.find_element(By.ID, "password").send_keys("Password123")
trigger()

driver.find_element(By.ID, "cpassword").send_keys("Password123")
trigger()

driver.find_element(By.ID, "terms").click()
trigger()

time.sleep(1)
driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("error-state.png")

# ---------- POSITIVE SCENARIO ----------
driver.refresh()
time.sleep(3)

driver.find_element(By.ID, "fname").send_keys("John")
trigger()

driver.find_element(By.ID, "lname").send_keys("Doe")
trigger()

driver.find_element(By.ID, "email").send_keys("john@gmail.com")
trigger()

driver.find_element(By.ID, "phone").send_keys("+919876543210")
trigger()

driver.find_element(By.XPATH, "//input[@value='Male']").click()
trigger()

driver.find_element(By.ID, "password").send_keys("Password123")
trigger()

driver.find_element(By.ID, "cpassword").send_keys("Password123")
trigger()

driver.find_element(By.ID, "terms").click()
trigger()

time.sleep(1)
driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("success-state.png")

# ---------- LOGIC VALIDATION ----------
driver.refresh()
time.sleep(3)

driver.find_element(By.ID, "country").send_keys("India")
trigger()

driver.find_element(By.ID, "state").send_keys("Telangana")
trigger()

driver.find_element(By.ID, "city").send_keys("Hyderabad")
trigger()

driver.find_element(By.ID, "password").send_keys("123")
trigger()

driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("StrongPass123")
trigger()

driver.find_element(By.ID, "cpassword").send_keys("WrongPass")
trigger()

print(driver.find_element(By.ID, "submitBtn").is_enabled())
driver.save_screenshot("logic-validation.png")

time.sleep(2)
driver.quit()

driver.find_element(By.ID, "fname").send_keys("John")
driver.find_element(By.ID, "lname").send_keys("Doe")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")
driver.find_element(By.ID, "phone").send_keys("+919876543210")

driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "cpassword").send_keys("Password123")
driver.find_element(By.ID, "terms").click()

driver.find_element(By.ID, "fname").click()
time.sleep(1)

driver.find_element(By.ID, "submitBtn").click()
driver.save_screenshot("success-state.png")


driver.refresh()
time.sleep(1)

driver.find_element(By.ID, "country").send_keys("India")
time.sleep(1)
driver.find_element(By.ID, "state").send_keys("Telangana")
time.sleep(1)
driver.find_element(By.ID, "city").send_keys("Hyderabad")

driver.find_element(By.ID, "password").send_keys("123")
time.sleep(1)
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("StrongPass123")

driver.find_element(By.ID, "cpassword").send_keys("WrongPass")

print(driver.find_element(By.ID, "submitBtn").is_enabled())
aaA
driver.save_screenshot("logic-validation.png")

time.sleep(2)
driver.quit()
