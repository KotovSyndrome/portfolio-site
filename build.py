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

    header = open("templates/top.html").read()
    footer = open("templates/bottom.html").read()

    for page in pages:
        old_page_contents = open(page["filename"]).read()
        new_contents = header + old_page_contents + footer
        open(page["output"], "w+").write(new_contents)

main()