import click
import latextools

from .generate_latex import generate_latex_table, add_latex_image


_HEADER = r"""\documentclass{article}
\usepackage{booktabs, graphicx}
\begin{document}
"""


@click.command()
@click.option(
    "--output_path",
    default="example.tex",
    help="Path to save the generated LaTeX file.",
)
@click.option(
    "--image_path",
    default=None,
    help="Path to the image to be included in LaTeX.",
)
def main(output_path: str, image_path: str):
    example_data = [
        ["Name", "Type", "Params"],
        ["model", "TransformerResnet", "10.5 M"],
        ["criterion", "CosineEmbeddingLoss", "0"],
        ["F1 score", "BinaryF1Score", "0"],
        ["AP score", "BinaryAveragePrecision", "0"],
        ["PR Curve", "BinaryPrecisionRecallCurve", "0"],
    ]

    latex_code = (
        _HEADER
        + generate_latex_table(example_data)
        + "\n"
        + (add_latex_image(image_path) if image_path else "")
        + "\n\\end{document}"
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(latex_code)

    print(f"Saved .tex to {output_path}")

    pdf = latextools.render_snippet(latex_code)

    pdf.save("example.pdf")


if __name__ == "__main__":
    main()
