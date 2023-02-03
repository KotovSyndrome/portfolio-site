import glob
import os
from jinja2 import Template

def init_pages_dict(html_files):
    pages = []
    
    for file in html_files: 
        file_name = os.path.basename(file) # ex. index.html
        title, extension = os.path.splitext(file_name) 
        title = str(title).capitalize() # ex. Index
        output = "docs/" + file_name # ex. "docs/index.html"
        pages.append({
            "filepath": file, # "content/index.html"
            "filename": file_name,
            "title": title,
            "output": output,
        })

    return pages

def create_page(page_contents, template, all_pages, current_page):
    new_html = template.render(
        content      = page_contents,
        pages        = all_pages,
        current_page = current_page,
    )
    return new_html

def main():    
    all_html_files = glob.glob('content/*.html')
    pages = init_pages_dict(all_html_files)
    template_html = open("templates/base.html").read()
    template = Template(template_html)

    for page in pages:
        page_contents = open(page["filepath"]).read()
        new_contents = create_page(page_contents, template, pages, page["title"])        
        open(page["output"], "w+").write(new_contents)


if __name__ == "__main__":
    main()