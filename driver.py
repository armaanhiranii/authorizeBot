from selenium_bot import authorize_bot
from get_text_file import get_text

if __name__ == "__main__":
    authorize_bot()
    print(get_text())
    print('done')