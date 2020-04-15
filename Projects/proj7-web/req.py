''' req.py

    Illustrates using the requests module.
    
    Use the "headers" option below for my website,
    and for other sites that give you an error. It
    is normally not needed, and you shouldn't need
    it for Project 7

Output:
======
<Response [200]>
<html>
    <body>
        <h1>Hello CS 1410!</h1>
        <a href="https://uvu.edu">UVU Site</a>
    </body>
</html>
'''

import requests

url = "https://chuckallison.com/cs1410/index.html"
resp = requests.get(url, headers={"User-Agent": "XY"})
if resp:
    print(resp)
    print(resp.text)
else:
    print("Error:", resp)
