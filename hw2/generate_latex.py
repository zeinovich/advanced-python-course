from typing import List


def generate_latex_table(
    data: List[List[str]], caption="Example Table"
) -> str:
    if not data or not all(isinstance(row, list) for row in data):
        raise ValueError("Input must be a non-empty list of lists")

    col_count = len(data[0])
    if any(len(row) != col_count for row in data):
        raise ValueError("All rows must have the same number of columns")

    latex = "\\begin{table}[h]\n\\centering\n"
    latex += "\\begin{tabular}{|" + " c |" * col_count + "}\\hline\n"

    # Add rows
    for i, row in enumerate(data):
        latex += " & ".join(map(str, row)) + " \\\\ \hline\n"

    latex += f"""\\end{{tabular}}\n\\caption{{{caption}}}\n\\label{{tab:example}}\n\\end{{table}}"""

    return latex


def add_latex_image(image_path: str, caption="Example Image") -> str:
    return rf"""
    \begin{{figure}}[h]
        \centering
        \includegraphics[width=0.8\textwidth]{{{image_path}}}
        \caption{{{caption}}}
        \label{{fig:image}}
    \end{{figure}}
    """
