''' links.py

    Illustrates finding embedded links.

    This is a naive implementation. Assumes only one spce
    after "href" and no spaces in href="...".
    Normally, one uses regular expressions in the re module.

Output:
======
$ python3 links.py "http://chuckallison.com/cs1410/inx.html"
Link: https://uvu.edu
$ python3 links.py "http://freshsources.com/page1.html"
Link: http://freshsources.com/page2.html
Link: http://freshsources.com/page5.html
'''

import sys

def main(url):
    import requests

    resp = requests.get(url, headers={"User-Agent": "XY"})
    if resp:
        # Find links
        href = "<a href"                # Note: lower case
        html = resp.text.casefold()     # casefold converts Unicode to lowercase
        start = 0
        while start < len(html):
            # Search for link
            start = html.find(href,start)
            if start == -1:
                break
            quote1 = html.find('"',start)
            if quote1 == -1:
                print("Missing opening quote")
                break
            quote2 = html.find('">',quote1+1)
            if quote2 == -1:
                print('Missing closing ">')
                break

            # Extract URL
            url = html[quote1+1:quote2]
            print("Link:",url)
            start = quote2+2

if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1])
    # main("http://chuckallison.com/cs1410")