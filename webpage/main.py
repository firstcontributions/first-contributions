

from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime




app = Flask(__name__)


 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
date = datetime.datetime.now().year

@app.route('/')
def index():
    
    return render_template('index.html', date=date)


@app.route('/view-on-github')
def view_on_github():
    pass
@app.route('/contribution-guide')
def contribution_guide():
    pass




@app.route('/contributor_list')
def contributors():
  
    contributors = []
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://github.com/oponefrank44/first-contributions/blob/main/Contributors.md")
    
    for i in range(1,30):
      
        header=driver.find_element(By.XPATH, value='//*[@id="repo-content-pjax-container"]/react-app/div/div/div[1]/div/div/div[2]/div/div/div[3]/div[2]/div/div[3]/section/div/article/ul[1]/li['+str(i)+']')
     
        contributors.append(header.text)
        
   
    # Example: Extract contributor names (replace with actual logic as needed)
      # Placeholder, replace with actual parsing logic
    driver.quit()
    return render_template('contributors.html', contributors=contributors, date=date)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    
