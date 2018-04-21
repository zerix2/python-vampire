#!/home/mcdade1/anaconda3/bin/python3

"""
Regex practice.
"""

import re
import requests

sites = 'google yahoo cnn msn outlook'.split()
pattern = re.compile(r'<title>+(.*)</title>+')
for s in sites:
    print(f'Searching: {s}')
    p = requests.get(f'http://{s}.com')
    text = str(p.content)
    title = re.findall(pattern, text)
    print(title)
#print(re.split(r'(\s*)', 'here are some words'))

#print(re.split(r'[a-f][a-f]', 'lonasdonaonasdonbaofoijnkasdoLKJLKJSDFOOIHAS'))

#print(re.findall(r'\d{1,5}\s\w+\s\w+\.', 'kslkdf324 main st.lkjsfij'))

#print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', 'kjnbskdfjnsdfn10.101.2.125lklkjmsfoijrdoijdfgoijdfogij10.15.4.5eroijertojoeodoijdfoe255.124.8.1olkijegerg'))
