#!/home/mcdade1/anaconda3/bin/python3

"""
Another file to play with regex
"""
import requests
import re

#page = requests.get('https://www.talosintelligence.com/reputation_center/lookup?search=206.212.61.144')
#page_cookies = page.cookies
#page2_url = 'https://www.talosintelligence.com/sb_api/query_lookup?query=%2Fapi%2Fv2%2Frelated_ips%2Fip%2F&query_entry=206.212.61.144&offset=0&order=ip+asc'
#page2 = requests.get(page2_url, cookies=page.cookies)

page = requests.Session()
#response = page.get('https://www.talosintelligence.com/reputation_center/lookup?search=206.212.61.144')
response = page.get('http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php')

check = str(response.content)

bits = re.findall(r'<div\s+\w</div>+', check)
#getit = re.findall('<td>.*', strchange)
print(bits)
