from urllib2 import urlopen
from bs4 import BeautifulSoup
from built_in_page import BuiltInPage as bip
import json
import parsedatetime

BASE = "http://www.builtinchicago.org"
QUERY = "/jobs?category=developer-engineer-78"
AJAX_BASE = "http://www.builtinchicago.org/apachesolr_ajax/ajax/search"

def get_json():
    url = AJAX_BASE + QUERY
    f = open('json.txt', 'r')
    jsn = json.loads(f.read())
    rows = BeautifulSoup(jsn['results']['data'], 'html.parser').contents[0].find_all('div', {'class': 'views-row'})
    jobs = map(lambda row: {'url': extract_url(row), 'date': extract_date(row)}, rows)
    return jobs

def extract_url(tag):
    return tag.find('a')['href']

def extract_date(tag):
    text = tag.find('span', {'class': 'posted-date'}).text
    cal = parsedatetime.Calendar()
    return cal.parse(text)

def get_paths():
    url = BASE + QUERY
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    job_titles = soup.find_all('div',{"class": "job-title"})
    paths = [BASE + job.find('a')['href'] for job in job_titles]
    return paths

def scrape():
    paths = get_paths()
    pages = map(bip, paths)
    return pages