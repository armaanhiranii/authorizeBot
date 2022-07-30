from selenium_bot import authorize_bot
from get_text_file import get_text
from text_to_excel import text_to_funstuff

def main():
    authorize_bot()
    text_to_funstuff(get_text(), r"C:\Users\conf.asst5\Desktop\test.xlsx")

    print("Excel File has been written!")
    
main()