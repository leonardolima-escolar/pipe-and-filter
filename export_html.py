from doctype import doctype

def export_html():
    with open('index.html', 'w+') as file:
        file.write(doctype())
