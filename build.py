header = open("templates/top.html").read()
footer = open("templates/bottom.html").read()

contact = open("content/contact.html").read()
index = open("content/index.html").read()
projects = open("content/projects.html").read()

new_contact = header + contact + footer
new_index = header + index + footer
new_projects = header + projects + footer

open("docs/contact.html", "w+").write(new_contact)
open("docs/index.html", "w+").write(new_index)
open("docs/projects.html", "w+").write(new_projects)