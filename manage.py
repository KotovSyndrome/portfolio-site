from utils import ssg, create_new_content_page
import sys

def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command == "build":
            ssg()
        elif command == "new":
            print("New page was requested")
            filename = input("What would you like to call your page? ")
            create_new_content_page(filename)
    else:
        sys.stderr.write("Usage:\n\tRebuild site: python manage.py build\n\tCreate new page: python manage.py new")

if __name__ == "__main__":
    main()