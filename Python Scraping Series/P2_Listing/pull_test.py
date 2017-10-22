import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def parse(url):
    print('Parsing..' + url)
    return 'Parsed..' + url


def pull(category_url):
    total_pages = 0
    total_links = []
    try:
        print('Processing...' + category_url)
        r = requests.get(category_url, headers=headers, timeout=5)
        if r.status_code == 200:
            html = r.text.strip()
            soup = BeautifulSoup(html, 'lxml')
            # Find total pages
            pagination_section = soup.select('.pagination li > a')
            if pagination_section:
                # -2 because the last is NEXT button
                total_pages = int(pagination_section[len(pagination_section) - 2].text)

            links = soup.select('.products .link')
            # results = [parse(l['href']) for l in links]
            for l in links:
                total_links.append(l['href'])
            for x in range(2, total_pages + 1):
                sleep(2)
                cat_url = 'https://www.daraz.pk/mens-smart-watches/?page={0}'.format(x)
                print('Processing...' + cat_url)
                r = requests.get(category_url, headers=headers, timeout=5)
                if r.status_code == 200:
                    links = soup.select('.products .link')
                    [total_links.append(l['href']) for l in links]
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
    except KeyboardInterrupt:
        print("Someone closed the program")
    finally:
        # Save links into file
        if len(total_links) > 0:
            with open('links.txt', 'a+', encoding='utf=8') as f:
                f.write('\n'.join(total_links))


if __name__ == '__main__':
    cat_url = 'https://www.daraz.pk/mens-smart-watches/'
    pull(cat_url)
    with open('links.txt',encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            parse(l)
