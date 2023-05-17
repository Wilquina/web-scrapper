import requests
import headers
from lxml import html

htmlHeaders = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

urlSeed = "https://www.wikipedia.org/"

response = requests.get(urlSeed, headers=headers.HEADERS)

parser = html.fromstring(response.text)
englishElem = parser.get_element_by_id("js-link-box-en")
englishText = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

print(englishElem.text_content())
print(englishText)


languages = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for lang in languages:
    print(lang)

languages2 = parser.find_class('central-featured-lang')
for lang in languages2:
    print(lang.text_content())


