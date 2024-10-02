from plyer import notification
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

# from wakepy import keep

# with keep.running():

# Options = options()
# Options.add_argument('--headless')
# Options.add_argument('--disable-gpu')
saved_C = []
def program():
    import time
    class Person:
        def __init__(self, name, time):
            self.name = name
            self.time = time


    def Time(x):
        print(int(x / 3600), end=":")
        print(int((x % 3600) / 60), end=":")
        print((x % 3600) % 60)


    Try_time = 60
    # Wait for the page to load after login (you can adjust the wait time as needed)
    # Create a new instance of the WebDriver (in this case, Chrome)

    driver = webdriver.Chrome()
    driver.minimize_window()
    # Open Facebook login page
    driver.get("https://www.facebook.com/")

    # Find the email and password fields and enter your credentials
    email_field = driver.find_element(By.ID, "email")
    # password
    #
    email_field.send_keys("***@gmail.com") # enter your email

    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("***") # enter your account password

    # Press Enter key to submit the form
    password_field.send_keys(Keys.ENTER)


    while True:
        time.sleep(60)
        contact = driver.find_elements(By.XPATH,
                                       "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div")  # old xpath >> /html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div
        contact_N = []
        # print(contact)
        for i in range(len(contact)):
            contact_N.append(contact[i].text)
        # print(contact_N)
        contact_Nl = contact_N[0].split("\n")

        # print(contact_Nl)

        for i, val in enumerate(contact_Nl):
            #print(i)
            #if i == len(contact_Nl):
            #    break
            flag = 0
            if val == "Active":
                for k in range(len(saved_C)):
                    if contact_Nl[i + 1] == saved_C[k].name:
                        flag = 1
                        break
                if flag:
                    saved_C[k].time += Try_time

                else:
                    saved_C.append(Person(contact_Nl[i + 1], Try_time))

        for i in range(len(saved_C)):
            print(saved_C[i].name, " ")
            Time(saved_C[i].time)
            if ( saved_C[i].name == "******" ):  # notif if specific friend is online
                notification.notify(
                    title='i am online ',
                    message="",
                    app_icon=None,
                    timeout=40, )

        print("--------------------------------")

def handler():
    try:
        program()
    except:
        print("ops error ")
        time.sleep(60)

while(True):
    handler()