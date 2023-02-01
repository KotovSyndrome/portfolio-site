#metadata
pages = [
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Form",
        "navbar1": "Bio",
        "navbar2": "Projects",
        "navbar3": "- Contact -"
    },
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Homepage",
        "navbar1": "- Bio -",
        "navbar2": "Projects",
        "navbar3": "Contact"
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects",
        "navbar1": "Bio",
        "navbar2": "- Projects -",
        "navbar3": "Contact"
    }
]

def main():
    template = open_read_stream("templates/base.html")

    for page in pages:
        page_contents = open_read_stream(page["filename"])
        new_contents = create_page(page_contents, template, page["title"], page["navbar1"], page["navbar2"], page["navbar3"])
        open_write_stream(page["output"], new_contents)

def create_page(page, template, title, navbar1, navbar2, navbar3):
    new_html = template.replace("{{content}}", page).replace("{{title}}", title).replace("{{navbar1}}", navbar1).replace("{{navbar2}}", navbar2).replace("{{navbar3}}", navbar3)
    return new_html

def open_read_stream(stream):
    return open(stream).read()

def open_write_stream(stream, data):
    return open(stream, "w+").write(data)

if __name__ == "__main__":
    main()