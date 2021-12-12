import urllib.request as ul

try:
    website = ul.request.urlopen('http://pudim.com.br')
except ul.error.URLError:
    print('{}Website inaccessible{}'.format(
        '\033[1;31m', '\033[m'
    ))
else:
    print('{}Website accessible!{}'.format(
        '\033[1;32m', '\033[m'
    ))
