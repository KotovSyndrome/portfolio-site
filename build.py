#metadata
pages = [
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Info"
    },
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Homepage"
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects"
    }
]

def main():
    template = open_read_stream("templates/base.html")

    for page in pages:
        page_contents = open_read_stream(page["filename"])
        new_contents = create_page(page_contents, template)
        open_write_stream(page["output"], new_contents)

def create_page(page, template):
    new_html = template.replace("{{content}}", page)
    return new_html

def open_read_stream(stream):
    return open(stream).read()

def open_write_stream(stream, data):
    return open(stream, "w+").write(data)

if __name__ == "__main__":
    main()