#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML using mistletoe library.

Usage:
  ./markdown2html.py [input_file] [output_file]

Arguments:
  input_file: the name of the Markdown file to be converted
  output_file: the name of the output HTML file

Example:
  ./markdown2html.py README.md README.html
"""

import mistletoe
from mistletoe import HTMLRenderer, InlineRenderer, BlockRenderer
from mistletoe.walkers import MarkdownWalker
import pathlib
import sys


class MyHTMLRenderer(HTMLRenderer):
    def heading(self, element):
        h_level = len(element.children[0].children)
        return f'<h{h_level}>{self.render(element.children)}</h{h_level}>'


def convert_md_to_html(input_file, output_file):
    """
    Converts markdown file to HTML file using mistletoe library
    """
    # Read the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_content = f.read()

    # Create a Markdown document
    md = mistletoe.markdown(md_content)

    # Render the Markdown document to HTML
    renderer = MyHTMLRenderer()
    walker = MarkdownWalker(md)
    html_content = walker.walk(renderer)

    # Write the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # Check if the input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    convert_md_to_html(args.input_file, args.output_file)

