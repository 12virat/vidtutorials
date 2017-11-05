from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def fetch(keyword):
    try:
        driver.get('http://google.com')
        # Entering keyword in search box
        try:
            q = driver.find_element_by_name('q')
            q.send_keys(keyword)
        except NoSuchElementException:
            print('Query box not found')
        finally:
            sleep(2)

        try:
            btn_ok = driver.find_element_by_name('btnK')
            btn_ok.click()
        except NoSuchElementException:
            print('Search button not found')
        finally:
            sleep(3)

            # fetch the first link and store
            try:
                link = driver.find_element_by_css_selector('h3 > a')
                print(link.get_attribute('href'))
            except NoSuchElementException:
                print('Link element not found')
    except Exception as ex:
        print(str(ex))
    finally:
        driver.save_screenshot('google_result.png')


if __name__ == '__main__':
    driver = None
    driver = webdriver.Firefox()
    fetch('Web Scraping')
    if driver:
        driver.quit()
