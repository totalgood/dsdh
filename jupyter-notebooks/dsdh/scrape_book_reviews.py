import urllib


def download_pages(
        urls=(
            'https://www.amazon.com/Healthcare-Analytics-Made-Simple-Techniques-ebook/dp/B0721MVT3W',
            ),
        tlds=('com', 'co.uk', 'ca', 'de')):
    pages = []
    for url in urls:
        domain, null, site, title, dp, asin = url.split('/')
        print('-' * 40)
        print(title)
        for tld in tlds:
            url = f'http://www.amazon.{tld}/{title}/product-reviews/{asin}'
            print(url)
            try:
                f = urllib.urlopen(url)
                pages.append(f.read())
            except:
                page = ""
            print('%s=%s' % (country, page.count('member-review')))
    return pages


def extract_reviews(pages):
    raise NotImplementedError("Use BS to extract <div class=member-review>")


if __name__ == '__main__':
    pages = download_pages()
    reviews = extract_reviews(pages)
