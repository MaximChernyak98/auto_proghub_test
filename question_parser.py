from selenium import webdriver
import os


def main():
    current_dir = os.getcwd()
    paths_to_webdriver = os.path.join(current_dir, 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=paths_to_webdriver)


if __name__ == "__main__":
    main()
