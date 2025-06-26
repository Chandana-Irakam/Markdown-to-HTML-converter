# Markdown-to-HTML-converter
📝 Markdown to HTML Converter
A simple Python command-line tool that converts a .md (Markdown) file into a clean .html file using standard Markdown syntax.

🚀 Features
Converts headers, bold, italics, lists, links, and inline code

Reads a .md file and writes a .html file

Lightweight and easy to use

Built using Python and the markdown module

📦 Requirements
Python 3.x

markdown module
Install it with:

bash
pip install markdown
▶️ How to Run
bash
py markdowntohtml.py input.md output.html
Example:
bash
py markdowntohtml.py markdowntohtml.md output.html
This reads from markdowntohtml.md and creates output.html.

📄 Sample Markdown (markdowntohtml.md)
markdown
# Hello World

This is **bold**, this is *italic*, and this is `inline code`.

- Item 1
- Item 2

[Visit OpenAI](https://openai.com)
✅ Output
The resulting output.html will contain:

html
<h1>Hello World</h1>
<p>This is <strong>bold</strong>, this is <em>italic</em>, and this is <code>inline code</code>.</p>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
<p><a href="https://openai.com">Visit OpenAI</a></p>
