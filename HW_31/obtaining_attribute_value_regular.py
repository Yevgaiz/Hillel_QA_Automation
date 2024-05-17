import re

with open('wiki_page.txt', 'r') as file:
    html_content = file.read()

href_pattern = r'<a[^>]*href="([^"]*)"[^>]*>'

href_values = re.findall(href_pattern, html_content)

for href in href_values:
    print(href)