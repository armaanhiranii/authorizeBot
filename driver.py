from selenium_bot import authorize_bot
from get_text_file import get_text
from text_to_excel import text_to_funstuff

def main():
    authorize_bot('/Users/armaanhirani/Desktop/authorizeBot/chromedriver')
    text_to_funstuff(get_text("/Users/armaanhirani/Downloads/*.*"), '/Users/armaanhirani/Downloads/FUN STUFF V2 (3).xlsx')

    print("Excel File has been written!")
    
main()