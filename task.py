from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# url samples for checking
url = {
    'hepsiburada': 'https://www.hepsiburada.com/skechers-claw-hammer-erkek-siyah-outdoor-ayakkabi-51595-bkgy-p-HBV000007I88B',
    'defacto' : 'https://www.defacto.com.tr/ekstra-slim-fit-chino-pantolon-2418068',
    'suwen' : 'https://www.suwen.com.tr/p/just-married-destekli-sutyen-bordo-st3900609a102-2927',
}

# webdriver setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# just use the url you want to check from the url dictionary    
driver.get(url["hepsiburada"])
driver.implicitly_wait(5)


# get the title of the page from h1 tag. 
# Html structure can be change, but for my thinkings, for SEO purposes, 
# it is better to use h1 tag as a product title
title = driver.find_element(By.TAG_NAME, "h1")

# just for the finding price section, I used the parent section of the title section
# because the price section is inside the parent section in all three websites
parent_section = title.find_element(By.XPATH, "../..")
pageSource = parent_section.get_attribute("innerText")


# get the parent section html structure and write it to a file
with open("page_source.txt", "w") as file:
    file.write(pageSource)
    file.close()

# finding price
with open("page_source.txt", "r") as file:
    Lines = file.readlines()
    for line in Lines:
        if "%" in line:
            continue
        elif "TL" in line[-3:] or "," in line:
            price = line.replace("\n", "")
            break

print()
print(f'Product name : {title.text}')
print(f'Product price : {price}')

driver.quit()