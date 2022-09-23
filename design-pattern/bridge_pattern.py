import abc
import urllib.parse
import urllib.request

"""
    Bridge pattern : 다양한 specialized class를 구현할 때 추상화를 토해 구현부를 분리
    # abstraction / implementor    
"""

class ResourceContent:

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path):
        self._imp.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fetch(self, path):
        pass

class URLFetcher(ResourceContentFetcher):

    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page = response.read()
                print(page)

class LocalFileFetcher(ResourceContentFetcher):

    def fetch(self, path):
        with open(path) as f:
            print(f.read())

def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content("file.txt")


if __name__ == "__main__":
    main()