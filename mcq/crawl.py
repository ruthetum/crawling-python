import requests
from bs4 import BeautifulSoup


urls = [
    'https://www.sanfoundry.com/cyber-security-questions-answers-generic-steps-security-1/',
]

for url in urls:
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    questions = soup.select('.entry-content > p')

