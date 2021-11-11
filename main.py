from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from render import count_winery_age, make_wine_database, find_min_price


# reformat this with argparse

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        time_of_life=count_winery_age(YEAR_OF_FOUNDATION),
        wine_database=make_wine_database(),
        min_price=find_min_price()
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    YEAR_OF_FOUNDATION = 1920
    main()


