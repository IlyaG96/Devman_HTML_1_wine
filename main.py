import os
from dotenv import load_dotenv
from render import count_winery_age, make_wine_database
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():

    load_dotenv()
    YEAR_OF_FOUNDATION = int(os.getenv("YEAR_OF_FOUNDATION", default=1920))
    PATH_TO_DATABASE = os.getenv("PATH_TO_DATABASE", default='/wine.xlsx')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        time_of_life=count_winery_age(YEAR_OF_FOUNDATION),
        wine_database=make_wine_database(PATH_TO_DATABASE),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()


