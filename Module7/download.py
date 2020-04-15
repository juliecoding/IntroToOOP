import requests

# Download a Powerpoint file
resp = requests.get("http://chuckallison.com/cs3240/Chapter%2010.pptx", headers={"User-Agent": "XY"})
with open("ch10.pptx","wb") as f:
    f.write(resp.content)

# Download a flag from the CIA
prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
fname = prefix+"us-lgflag.gif"
flag = requests.get(fname).content      # Note: No headers={...}
with open("us.gif","wb") as f:
    f.write(flag)
