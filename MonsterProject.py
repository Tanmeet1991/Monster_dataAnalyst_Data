from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logindetails
from bs4 import BeautifulSoup
import pandas as pd


class Web:
    def __init__(self):
        ''' This will initiate ony browser with required website, which is Monster.com in our case.
        '''
        self.driver = webdriver.Chrome(executable_path="d:\\Python Practice tests\\Web scraping\\chromedriver.exe")
        self.driver.get('https://www.monsterindia.com/')
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(2)
        
class Login_Monster(Web):
    def login(self):
        '''This function will do the login process, with email id and password, and will print 'Login into Monster site:- Successful.',
        else it will the error if any.
        '''
        try:
            self.login_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/header/header/div[2]/div[2]/div/div[2]/ul/li[1]/a/span")
            self.login_button.click()
            time.sleep(3)    
            self.email = self.driver.find_element(By.XPATH, "//*[@id='signInName']")
            self.email.send_keys(logindetails.login.get_email())
            time.sleep(2)
            self.password = self.driver.find_element(By.XPATH, "//*[@id='password']")
            self.password.send_keys(logindetails.login.get_password())
            self.signIn = self.driver.find_element(By.XPATH, "//*[@id='signInbtn']")
            self.signIn.click()
            print('Login into Monster site:- Successful.')
            time.sleep(3)
        except Exception as e:
            print(e, ":There is an error.")
        return
    
class Job_description(Login_Monster):
    profile = 'Data Analyst'
    location_1 = 'Gurugram'
    def Job_profile(self):
        ''' Job profile function will hlp in searching for the required profile and location, wherever you need and whatever you are looking
        for. You can hanfe location and profile, under profile = ''. and location_1 = ''. 
        '''
        self.search = self.driver.find_element(By.XPATH, "//input[@class= 'input search-bar home_ac']")
        self.search.click()
        self.search.send_keys(self.profile)
        time.sleep(2)
        self.location = self.driver.find_element(By.XPATH, "//input[@class= 'input location_ac']")
        self.location.send_keys(self.location_1)
        self.search_btn = self.driver.find_element(By.XPATH, "//input[@class='btn']")
        self.search_btn.click()
        time.sleep(3)
        
        return

class Data(Job_description):
    def job_postings(self):
        ''' Job Postings function will scrape all the postings and all required details regarding the searched job profile,
        such as, Job title, salary, requirements, etc. also it will scrape all the data and convert all it into csv file.
        '''
        self.df = pd.DataFrame({'Job_Title':[''], 'Company':[''], 'Experience':[''], 'Salary':[''], 'Job_Description':[''], 'Post_Date':[''], 'Link':['']})
        
        while True:
            self.scroll_down_1 = self.driver.execute_script('window.scrollTo(0, 2000)')
            time.sleep(3)

            self.scroll_down_2 = self.driver.execute_script('window.scrollTo(2000, 3300)')
            time.sleep(3)
            self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
            self.postings = self.soup.find_all('div', class_='cardContainer')
            for self.post in self.postings:
                try:
                    try:
                        self.job_title = self.post.find('div', class_='jobTitle').text.strip()
                    except:
                        print("job_title_error")
                    try:
                        self.company = self.post.find('div', class_='companyName').text.strip()
                    except:
                        print("company_name_error")
                    try:
                        self.experience_r = self.post.find('i', class_='mqfisrp-briefcase').text.strip()
                    except:
                        self.experience_r = 'N/A'

                    try:
                        
                        self.post_date = self.post.find('p', class_='timeText').text.strip()
                    except:
                        print("post_date_error")
                    self.df = self.df.append({'Job_Title':self.job_title, 'Company':self.company, 'Experience':self.experience_r, 'Post_Date':self.post_date}, ignore_index=True)
                except Exception as e:
                    print(e, 'There is an Error:')
            try:
                self.next_page = self.driver.find_element(By.CLASS_NAME, 'mqfisrp-right-arrow')
                self.next_page.click()
                time.sleep(4)
            except:
                break
            self.postings = self.soup.find_all('div', class_='cardContainer')  
            self.df.to_csv('D:\\Monster Project\\Monster_Data_Anayst.csv')

login_M = Data()
login_M.login()
print(login_M.login.__doc__)
login_M.Job_profile()
print(login_M.Job_profile.__doc__)
login_M.job_postings()
print(login_M.job_postings.__doc__)
        
