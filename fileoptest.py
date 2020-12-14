from selenium import webdriver
import userDetails
import time
class delInstagram:
    notfollowers=[]
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.link = "http://instagram.com/"
        self.readFile()
        #
        # options = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=C:\\Users\\HULK\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        # self.browser = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=options)



        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.goInstagram()
    def readFile(self):
        f = open('notfollowers.txt')
        for line in f:
            self.notfollowers.append(line)
        f.close()
    def getNoFollowers(self):
        for i in self.notfollowers:
            print(i)
    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        self.login()
    def login(self):
        self.browser.find_element_by_name("username").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3)").click()
        time.sleep(3)
        self.delUsers()
    def delUsers(self):
        for username in self.notfollowers:
            self.delUser(username)
            print(username+"deleted.")
    def delUser(self,username):
        self.browser.get(self.link+username)
        time.sleep(18)
        self.browser.execute_script('document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div:nth-child(2) > button").click()')
        time.sleep(10)
        self.browser.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_").click()')
        time.sleep(7)


if __name__ == '__main__':
    d=delInstagram(userDetails.username,userDetails.password)