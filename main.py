import os
from dotenv import load_dotenv
from render import count_winery_age, make_wine_database
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():

    load_dotenv()

    year_of_foundation = int(os.getenv("YEAR_OF_FOUNDATION", default=1920))
    path_to_database = os.getenv("PATH_TO_DATABASE", default='./wine.xlsx')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        time_of_life=count_winery_age(year_of_foundation),
        wine_database=make_wine_database(path_to_database),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()


