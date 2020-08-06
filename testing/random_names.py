import requests
from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'

r = requests.get(url)

text = r.text

individual_words = text.split()

random_number = randint(0, len(individual_words))
print(individual_words[random_number] + str(random_number))