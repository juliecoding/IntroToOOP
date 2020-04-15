''' links.py

    Illustrates finding embedded links. Uses regular expressions.

Output:
======
$ python3 links2.py "http://chuckallison.com/cs1410/inx.html"
Link: https://uvu.edu
$ python3 links2.py "http://freshsources.com/page1.html" 
Link: http://freshsources.com/page2.html
Link: http://freshsources.com/page5.html
'''

import sys

def main(url):
    import re, requests

    resp = requests.get(url, headers={"User-Agent": "XY"})
    if resp:
        # Find links
        html = resp.text.casefold()
        pat = re.compile(r'<a\s+href\s*=\s*"(https{0,1}://[^"]+).*?>')
        for url in (anchor.group(1) for anchor in re.finditer(pat,html)):
            print("Link:",url)
 
if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1])   