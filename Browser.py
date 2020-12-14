from selenium import webdriver
import time

class LastPost:
    def __init__(self,username,date):
        self.username=username
        self.date=date
        self.bool=int(date[-4:])<2020

class Browser:
    following=[]
    followers=[]
    lastpost=[]
    notFollower=[]
    notFollowing=[]
    def __init__(self,username,password):
        self.link="http://instagram.com"
        self.browser=webdriver.Chrome(executable_path="chromedriver.exe")
        self.username=username
        self.password=password
        self.goInstagram()
    def goInstagram(self):
        self.browser.get("http://instagram.com")
        time.sleep(2)
        self.login()
    def login(self):
        self.browser.find_element_by_name("username").send_keys(self.username)
        self.browser.find_element_by_name("password").send_keys(self.password)
        self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3)").click()
        time.sleep(5)
        self.getFollowers()
        self.getFollowing()
        # for follow in self.following:
        #     self.lastPost(follow)
        self.notFollower()
        self.notFollowing()
    def getFollowers(self):
        self.browser.get("http://instagram.com/" + self.username)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        self.scrollTo()
        followers=self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        for follower in followers:
            self.followers.append(follower.text)
        print(len(self.followers)," takipçin var")


    def getFollowing(self):
        self.browser.get("http://instagram.com/" + self.username)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        self.scrollTo()
        following=self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        for follow in following:
            self.following.append(follow.text)
        print(len(self.following)," takip ediyorsun ")


    def scrollTo(self):
        jsCommand="""
        page=document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        var pageEnd=page.scrollHeight;
        return pageEnd
        """
        pageEnd=self.browser.execute_script(jsCommand)
        while True:
            end=pageEnd
            time.sleep(1)
            pageEnd=self.browser.execute_script(jsCommand)
            if end==pageEnd:
                break

    def notFollower(self):
        notFollower=list(set(self.following)-set(self.followers))
        print("Seni takip etmeyen takip ettiklerin")
        i=1
        for item in notFollower:
            print(item)
            i=i+1
    def notFollowing(self):
        notFollowing=list(set(self.followers)-set(self.following))
        print("Senin takip etmediğin takipçilerin")
        i = 1
        for item in notFollowing:
            print(item)
            i = i + 1
    def lastPost(self,username):
        uname="https://www.instagram.com/"+username+"/"
        self.browser.get(uname)
        time.sleep(1)
        if self.browser.find_elements_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a"):
            self.browser.find_elements_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1) > a")[0].click()
            time.sleep(1)
            date=self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time").get_attribute("title")
            lastpost=LastPost(username,date)
            self.lastpost.append(lastpost)
            print(lastpost.username," ",lastpost.date," ",lastpost.bool)
        else:
            print(username," gönderi yok.")

