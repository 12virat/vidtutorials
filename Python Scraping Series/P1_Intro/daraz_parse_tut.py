import requests
from  bs4 import BeautifulSoup

if __name__ == '__main__':
    title = '-'
    brand = '-'
    price = '-'
    features = '-'
    all_features = []
    record = []

    # Access the page
    r = requests.get('https://www.daraz.pk/solo-5-power-bank-10000-mah-white-romoss-mpg38013.html')

    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        # Title
        title_section = soup.find('h1')
        if title_section:
            title = title_section.text

        # Brand
        brand_section = soup.select('.sub-title > a')
        if brand_section:
            brand = brand_section[0].text

        # Features
        features_section = soup.select('.list ul > li')

        if features_section:
            for f in features_section:
                all_features.append(f.text)

            features = '|'.join(all_features)

        # Price
        price_section = soup.select('.price > span')
        if price_section and len(price_section) > 1:
            price = price_section[1].text.replace(',', '').strip()

        record.append(title)
        record.append(brand)
        record.append(price)
        record.append(features)

        # Store Data in CSV
        with open('result_data.csv', 'a+', encoding='utf-8') as file:
            file.write('Title,Brand,Price,Features\n')
            file.write(','.join(record))
