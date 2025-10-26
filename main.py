from pygetwindow import getWindowsWithTitle
from DrissionPage import ChromiumPage
from DrissionPage.common import Keys
from colorama import Fore
import colorama
import random

title = "Xem các video thịnh hành dành cho bạn | TikTok - Google Chrome"
page = 'https://www.tiktok.com/foryou?lang=vi-VN'

colors = [
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTRED_EX
]

colorama.init(autoreset=True)
def activateWindow():
    while True:
        try:
            window = getWindowsWithTitle(title)
            window[0].activate()
            window[0].restore()
            break
        except Exception:
            continue


def scroll_video(browser: ChromiumPage, index: int) -> object:
    try:
        ele_scroll = f'@data-scroll-index="{index}"'
        xpath_scroll = f'xpath://article[{ele_scroll}]'
        tab_video = browser.ele(xpath_scroll, timeout=5)
        tab_video.scroll.to_center()
        return tab_video
    except Exception:
        return object


def comment_video(tab_video: ChromiumPage, percent: int) -> object:
    try:
        if random.random() > percent / 100:
            return object

        xpath_icon = f'xpath://span[@data-e2e="comment-icon"]'
        tab_comment = tab_video.ele(xpath_icon, timeout=5)
        tab_comment.scroll.to_center()
        tab_comment.click()
        return tab_comment
    except Exception:
        return object


def comment_write(browser: ChromiumPage, text: str) -> object:
    try:
        xpath_input = f'xpath://div[@data-e2e="comment-text"]'
        tab_comment = browser.ele(xpath_input, timeout=5)
        tab_comment.scroll.to_center()
        tab_comment.click()
        tab_comment.input(text, clear=True)
        tab_comment.input(Keys.ENTER)
    except Exception:
        return object


def read_list(file_path: str) -> list:
    result = []
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            clean = line.strip()
            if clean:
                result.append(clean)
    return result

path_comment = 'static/comment'
comment_list = read_list(path_comment)

browser = ChromiumPage()
browser.get(page)

tab = browser.get_tab()
activateWindow()


for index in range(1, 1000):
    color = random.choice(colors)
    print(color + f"Video: {index}")

    tab_video = scroll_video(browser, index)
    browser.wait(random.randint(5, 9))
    comment_video(tab_video, 50)

    browser.wait(random.randint(5, 9))
    comment = random.choice(comment_list)
    comment_write(browser, comment)

    browser.wait(random.randint(5, 9))

browser.quit()