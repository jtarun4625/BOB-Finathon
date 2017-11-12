from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(executable_path='C:/Users/jtaru/Desktop/chromedriver.exe', chrome_options=chrome_options)


#script for sending message
def fb_login() :
    #user Credentials
    user = browser.find_element_by_css_selector('#email')
    user.send_keys('bobfinathon@gmail.com')
    password = browser.find_element_by_css_selector('#pass')
    password.send_keys('Bobstt12@')
    try:
        login = browser.find_element_by_css_selector("#u_0_2")
        print("u_0_2")
    except Exception as e:
        try:
            login = browser.find_element_by_css_selector("#u_0_5")
            print("u_0_5")
        except:
            login = browser.find_element_by_css_selector("#u_0_3")
            print("u_0_3")


    if login.click() :
        return True

def open_facebook():
    browser.get("https://www.facebook.com/142996509764392")
    url = browser.current_url
    temp_url = url[url.find("m/")+1:]
    username = temp_url[temp_url.find("/")+1:]
    print(username)
    message = browser.find_element_by_xpath("//a[@href='/messages/t/"+username+"/']")
    print("Clicking Message")
    message.click()
    print("Shayad message Open")
    time.sleep(6)
    fc_day_contents = browser.find_element_by_xpath("//div[@class='fbNubFlyoutFooter']/div/div/div/span/div/div/div[2]/div")
    fc_day_contents.send_keys("Hello, This is Bot from Bank Of Baroda, To know about loan, account information, balance inquiry, queries, offers and facilities 'Like' the page and initiate the conversation with the bot. Also tweet the application on twitter. Link is as below :https://twitter.com/bobfinathon https://www.facebook.com/BotBob12/")
    fc_day_contents.send_keys(Keys.RETURN)


if __name__ == '__main__':
    browser.get("https://facebook.com")
    fb_login()
    print("Searching")
    open_facebook()

#now if customer is interested he can contact by clicking the link in message 