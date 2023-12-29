from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a = input("Input the URL or string you want to search for:")
a = a.replace(' ', '+')

b = 'C:/path/to/chromedriver.exe'

c = webdriver.ChromeOptions()
c.add_argument(f'--webdriver-path={b}')

d = webdriver.Chrome(options=c)
d.get("https://www.google.com")

e = d.find_element("name", "q")
e.send_keys(a)
e.send_keys(Keys.RETURN)


input("Press Enter to close the browser...")

d.quit()
