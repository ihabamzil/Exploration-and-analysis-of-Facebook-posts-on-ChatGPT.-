# Set up Driver
CHROME_DRIVER = "C:/Windows/chromedriver_win32.zip/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-hang-monitor")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-infobars") 
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")  

# Log into Facebook
driver = webdriver.Chrome(options=options,)
driver.get("http://www.facebook.com/login")
login = driver.find_element(By.CSS_SELECTOR,'#email')
login.send_keys('your_email')
password = driver.find_element(By.CSS_SELECTOR,'#pass')
password.send_keys('your_password')
password.send_keys(Keys.RETURN)
time.sleep(2)

driver.get("https://www.facebook.com/chatgpt4dotcom")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')

M=[]
for i in range(1,100):
    try:
        L = soup.find_all('div',{"style":"text-align: start;","dir":"auto"})
        for x in L:
            M.append(x.text)
    except Exception as e:
        print(i)


data = pd.DataFrame(M)
data.to_csv("fcb_posts")
