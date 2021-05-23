import pywhatkit as ps
from selenium import webdriver


def message():
    phone = input("Enter The Phone Number(Without Country Code) : ")

    mess = input('Enter The Message : ')

    hour = int(input('Enter Hour And Minute To Send Message : '))
    minute = int(input('Minute : '))

    country = '+91'
    num = country + phone

    ps.sendwhatmsg(num, mess, hour, minute)


def spammer():
    oper =int(input('Enter 1 For Windows 2 For Linux : '))
    if oper == 1:
        path = "chromedriver.exe"  # Location of the webdriver file
    else:
        print("its2")
        path = "chromedriver"

    driver = webdriver.Chrome(path)
    driver.implicitly_wait(15)
    driver.get('https://web.whatsapp.com')
    driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
    input_string = input("Enter message to send: ")
    i = 0
    lim = int(input("Enter The Number Of Messages:"))
    while i < lim:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(input_string)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        if i == lim:
            break
        i += 1


def choice(i):
    switcher = {
        1: lambda: message(),
        2: lambda: spammer()
    }
    func = switcher.get(i, lambda: 'Invalid')
    print(func())


if __name__ == "__main__":
    print("1 To Send A Message At Specific Time")
    print("2 To Spam A Message To Friend")
    arg = int(input("Enter Your Choice : "))
    print(choice(arg))