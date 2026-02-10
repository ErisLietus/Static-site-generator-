from copystatic import copy_static
from gencontent import generate_pages_recursive

def main():
    static_path = "static"
    public_path = "public"
    copy_static(static_path, public_path)
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()

