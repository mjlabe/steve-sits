import importlib
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def render_page(post_data, template):
    print(f"Rendering {post_data} page to static file.")
    output_name = str(template).replace('.py', '.html')
    with open(Path().absolute() / 'html' / output_name, 'w+') as file:
        html = template.render(
            page=post_data,
        )
        file.write(html)


def render_posts():
    file_path = Path().absolute() / 'posts'
    env = Environment(loader=FileSystemLoader('templates'))
    if file_path.is_dir():
        posts = list(x for x in file_path.iterdir() if x.is_file())
        for post_file in posts:
            module_name = Path(post_file).parent.stem
            module_file = Path(post_file).stem
            post_module = importlib.import_module(f'{module_name}.{module_file}')
            post_data = post_module.page()
            print(post_data)
            render_page(post_data=post_data, template=env.get_template('post.html'))


if __name__ == "__main__":
    render_posts()
