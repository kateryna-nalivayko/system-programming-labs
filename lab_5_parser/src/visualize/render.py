import os
import subprocess

from lab_5_parser.src.visualize.to_dot import DotGenerator

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def render_ast(ast, filename="ast"):
    """
    Генерує .dot і .png файли в visualize/output/
    filename — ім'я файлу без розширення
    """

    dot = DotGenerator().generate(ast)

    dot_path = os.path.join(OUTPUT_DIR, f"{filename}.dot")
    png_path = os.path.join(OUTPUT_DIR, f"{filename}.png")

    with open(dot_path, "w") as f:
        f.write(dot)

    # Викликаємо graphviz
    subprocess.run(["dot", "-Tpng", dot_path, "-o", png_path])

    print(f"Файли збережено:\n - {dot_path}\n - {png_path}")