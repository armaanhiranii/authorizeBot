# authorizeBot

Python implementation of scraping the most recent settlements on Authorize.net with Selenium and returning the downloaded text file. <br />

I am currently working on two new features to the bot. One to read the text file into an existing Excel file, and another to grab a screenshot of the Authorize page to use as backup per company procedure.

There are currently three scripts:

"selenium_bot.py" to scrape Authorize.net and download a .txt file of the transactions <br />
"get_text_file.py" to return the file path of the downloaded file. <br />
"driver.py" used to call the functions and run the script. <br />
If you have a slow connection and you encounter code problems, try increasing the seconds of time.sleep () function <br />


What I used: <br />

Python 3.10.4 <br />
Selenium 4.3.0 <br />
Google Chrome 103.0.5060.114 <br />
ChromeDriver 103.0.5060.53 <br />
Visual Studio Code 1.68.1 <br />
mac OS Monterey <br />
