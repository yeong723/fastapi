from playwright.sync_api import sync_playwright
import time


def open_browser():

    print("브라우저를 열고 있어요.")
    with sync_playwright as p:
        browser = p.cheomium.launch(headless=False, slow_mo=1000)

        page = browser.new_page()
        page.goto("https://www.google.com")
        print("브라우저가 열렸습니다")
        print("10 초 후에 자동으로 닫힙니다.")

        time.sleep(10)

        browser.close()
        print("브라우저가 닫혔습니다.")


if __name__=="__main__":
    open_browser()