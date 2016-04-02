from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint, re, os
from sets import Set

DIR_NAME = 'cached_pages/'
class BuiltInPage:
    def __init__(self, url):
        soup = BuiltInPage.import_built_in_post(url)
        self.company = soup.find('span', {'class': 'nc-fallback-title'}).text.strip()
        self.position = soup.find('span', {'class': 'nj-job-title'}).text.strip()
        self.post = soup.find('span', {'class': 'nj-job-body'}).prettify().encode('utf-8')

    def post_paragraphs(self):
        post = BeautifulSoup(self.post, 'html.parser').text.encode('utf-8').strip()
        post = re.sub(r'(\n+\s*)+', '\n', post)
        post_list = post.strip().split('\n')
        return post_list

    def extract_lists(self):
        pgs = page.post_paragraphs()
        headers = self.extract_headers()
        lists = {}
        header = None

        # get lists from paragraphs
        for pg in pgs:
            if is_header(pg): headers.add(headerify(pg))
            pot_header = headerify(pg)
            if pot_header in headers:
                header = pot_header
                lists[header] = []
            elif lists.has_key(header):
                lists[header].append(pg)

        # check for lists not separated by \n
        # messes up on single paragraphs below headers
        for key in lists.keys():
            if(len(lists[key]) == 1):
                lists[key] = lists[key][0].split(',')

        return lists

    # extracts headers from bold text in document
    def extract_headers(self):
        soup = BeautifulSoup(self.post, 'html.parser')
        bolds = soup.find_all('b')
        strongs = soup.find_all('strong')
        headers = Set()
        for b in bolds: headers.add(headerify(b.text))
        for s in strongs: headers.add(headerify(s.text))
        return map(lambda h: re.sub(self.company, 'company', h), headers)



    # takes a url and fetches if it has not already been chached
    # returns a soup object
    @classmethod
    def import_built_in_post(cls, url):
        file_name = DIR_NAME + url.split('/')[-1]
        if('.txt' not in url): file_name += '.txt'

        if os.path.exists(file_name):
            f = open(file_name, 'r')
            response = f.read().decode('utf-8')
            soup = BeautifulSoup(response, 'html.parser')
        else:
            print("HTTP REQUEST MADE")
            response = urlopen(url).read().decode('utf-8')
            soup = BeautifulSoup(response, 'html.parser')
            f = open(file_name, 'w')
            f.write(soup.prettify().encode('utf-8'))
        return soup

    @classmethod
    def all(cls):
        files = [f for f in os.listdir(DIR_NAME) if os.path.isfile(os.path.join(DIR_NAME, f))]
        pages = [BuiltInPage(p) for p in files]
        return pages

# tests a string for markers of being a header
def is_header(str):
    if len(str.split('.')) > 1: return False
    if str[-1] == ':': return True
    return False

def headerify(str):
    return str.strip().replace(':', '')
    