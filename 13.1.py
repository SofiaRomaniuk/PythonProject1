import codecs
import re
import os

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_html= re.sub(r'<[^>]*>', '', html)

    lines = clean_html.splitlines()
    clean_html = re.sub(r'\s+', ' ', clean_html)
    final_text = clean_html.strip()

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(final_text)

delete_html_tags( r'C:\Users\sofia\Downloads\draft (3).html')