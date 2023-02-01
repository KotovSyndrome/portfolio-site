import glob
import os
from jinja2 import Template

def init_page_object(html_files):
    pages = []
    
    for file in html_files: 
        file_name = os.path.basename(file) # ex. index.html
        title, extension = os.path.splitext(file_name) # ex. Index
        title = str(title).capitalize()
        output = "docs/" + file_name # ex. "docs/index.html"
        pages.append({
            "filename": file,
            "title": title,
            "output": output,
            "navbar": {
                "index": "- Bio -" if file_name == "index.html" else "Bio",
                "projects": "- Projects -" if file_name == "projects.html" else "Projects",
                "contact": "- Contact -" if file_name == "contact.html" else "Contact",
            }
        })

    return pages

def create_page(page_contents, template, page):
    # new_html = template.replace("{{content}}", page_contents).replace("{{title}}", page["title"]).replace("{{navbar1}}", page["navbar"]["index"]).replace("{{navbar2}}", page["navbar"]["projects"]).replace("{{navbar3}}", page["navbar"]["contact"])
    new_html = template.render(
        content=page_contents,
        title=page["title"],
        navbar1=page["navbar"]["index"],
        navbar2=page["navbar"]["projects"],
        navbar3=page["navbar"]["contact"],
    )
    return new_html

def main():    
    all_html_files = glob.glob('content/*.html')
    pages = init_page_object(all_html_files)
    template_html = open("templates/base.html").read()
    template = Template(template_html)

    for page in pages:
        print(page)
        page_contents = open(page["filename"]).read()
        new_contents = create_page(page_contents, template, page)        
        open(page["output"], "w+").write(new_contents)


if __name__ == "__main__":
    main()