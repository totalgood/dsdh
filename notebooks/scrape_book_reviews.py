import urllib


tlds = ['com', 'co.uk', 'ca', 'de']
books = [
    '''https://www.amazon.com/Healthcare-Analytics-Made-Simple-Techniques-ebook/dp/B0721MVT3W''',
    ]


pages = []
for book in books:
    domain, null, site, title, dp, asin = book.split('/')
    print('-' * 40)
    print(title)
    for tld in tlds:
        url = f'http://www.amazon.{tld}/{title}/product-reviews/{asin}'
        print(url)

        # try:
        #     f = urllib.urlopen(url)
        #     page = f.read().lower()
        # except:
        #     page = ""
        # print('%s=%s' % (country, page.count('member-review')))
        # pages.append(page)
