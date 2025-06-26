import argparse
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"❌ Error: File '{input_file}' not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    html = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Converted '{input_file}' to '{output_file}' successfully.")

def main():
    parser = argparse.ArgumentParser(description="Markdown to HTML Converter")
    parser.add_argument("input", help="Path to the input .md file")
    parser.add_argument("output", help="Path to the output .html file")
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)

if __name__ == "__main__":
    main()
