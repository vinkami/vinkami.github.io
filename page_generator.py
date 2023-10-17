# This file is used to generate the static html pages for the website from jinja2 templates in the /.template/ folder.


from constants import URLS, RENDER_ARGS
from jinja2 import Environment, FileSystemLoader
import os


env = Environment(loader=FileSystemLoader("template/"))

if __name__ == '__main__':
    # Create /pages if it doesn't exist
    if not os.path.exists("pages"):
        os.mkdir("pages")
        print("Created /pages")

    # Walk through /pages and remove all files
    else:
        for root, dirs, files in os.walk("pages"):
            for f in files:
                os.remove(os.path.join(root, f))
        print("Removed all files in /pages")

    # Generate all pages
    for static_name, template_name in URLS.items():
        if template_name[0] == "-": continue
        template = env.get_template(template_name)
        # create missing folder
        if "/" in static_name:
            os.makedirs(os.path.dirname(f"pages/{static_name}"), exist_ok=True)

        with open(f"pages/{static_name}", "w", encoding="utf-8") as f:
            f.write(template.render(RENDER_ARGS))
    print("Generated all pages")
