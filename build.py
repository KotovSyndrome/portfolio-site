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
    template = open("templates/base.html").read()

    for page in pages:
        page_contents = open(page["filename"]).read()
        new_contents = template.replace("{{content}}", page_contents)
        open(page["output"], "w+").write(new_contents)

main()