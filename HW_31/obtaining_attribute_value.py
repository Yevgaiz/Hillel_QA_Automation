with open('wiki_page.txt', 'r') as file:
    html_content = file.read()

href_values = []
start_pos = 0
while True:
    start_a_tag = html_content.find('<a ', start_pos)
    if start_a_tag == -1:
        break

    start_href = html_content.find('href="', start_a_tag)
    if start_href == -1:
        break

    start_value = start_href + len('href="')
    end_value = html_content.find('"', start_value)

    href_value = html_content[start_value:end_value]

    href_values.append(href_value)

    start_pos = end_value


for href in href_values:
    print(href)