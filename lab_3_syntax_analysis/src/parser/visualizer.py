from pathlib import Path

try:
    from graphviz import Digraph
except Exception:
    Digraph = None

from lab_3_syntax_analysis.src.parser.ast_builder import AST


def visualize_ast(root: AST, out_path: str = "report/screenshots/ast"):

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    if Digraph is None:
        Path(out_path + ".dot").write_text("// Graphviz не встановлено")
        print("Graphviz не встановлено — створено файл ast.dot")
        return None

    g = Digraph(comment="AST")

    def add_node(node):
        nid = str(id(node))
        label = node.kind if node.value is None else f"{node.kind}\\n{node.value}"
        g.node(nid, label, shape="box", style="rounded,filled", fillcolor="lightyellow")
        for child in node.children:
            g.edge(nid, add_node(child))
        return nid

    add_node(root)
    png_path = g.render(out_path, format="png", cleanup=True)
    print(f"AST збережено як {png_path}")
    return png_path