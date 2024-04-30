#! /usr/bin/python3

# Load mss.html and extract text.
with open('mss.html') as f:
    html = f.read()

# Clean up non-breaking spaces.
html = html.replace(' ', ' ')
html = html.replace(' ', ' ')

import re

# Replace weird line breaks after starting tags.
html = re.sub(r'<a \n', '<a ', html)

# Find text of the pattern "(<a id=\"x1-yyyy\"></a> ~" and eliminate the space.
html = re.sub(r'<a id="(x1-\d{4})"></a> ~', r'<a id="\1"></a>~', html)

# Find text of the pattern "~xxxxxx-xxxxxx" and mark it `<code>` where "x" are letters.
html = re.sub(r'~[a-zA-Z]{6}-[a-zA-Z]{6}', r'<code>\g<0></code>', html)

# Rework the footnote link to remove mss2.html from 'href="mss2.html#fn1x0"'.
html = re.sub(r'href="mss\d.html#fn(\d)x(\d)"', r'href="#fn\1x\2"', html)

# Each footnote link has an anchor tag after it.  We want to link back
# to it later, so we need to store a dict of the footnote to the anchor.

# Locate the term "footnote-mark", then extract the next two `<a>` tags.
# The first `<a>` tag is the footnote link, the second `<a>` tag is the anchor.
footnote_links = re.finditer(r'footnote-mark">', html)
print(footnote_links)
footnote_dict = {}
for footnote_link in footnote_links:
    # Find the next `<a>` tag with an href.
    footnote_id = re.search(r'<a href="#fn(\d)x(\d)">', html[footnote_link.end():])
    # Find the next `<a>` tag with an id.
    anchor_id = re.search(r'<a  id="x1-', html[footnote_link.end():])
    # Store the footnote link and anchor in a dict.
    start = footnote_link.end() + anchor_id.span()[0] + len(anchor_id.group(0)) - 3
    begin = html[start:].find('"')
    footnote_dict[footnote_id.group(0)[9:-2]] = html[start:start+begin]
print(footnote_dict)

# Load the footnotes in files "mss2.html" etc. and extract text.
footnote_html = []
for i in range(2, 100):
    try:
        with open(f'mss{i}.html') as f:
            # Extract only the contents of the `<body>` tag.
            contents = re.search(r'<body \n>(.*)</body>', f.read(), re.DOTALL).group(1)
            # Link back to the corresponding anchor tag of the form '<a  id="x1-6001f1">'.
            contents = re.sub(r'</p></div>', f'<a href=\"#{footnote_dict[f"#fn{i-1}x0"]}\">⤴</a></p></div>', contents)
            # Remove the `<body>` tag.
            print(f'<a href=\"#{footnote_dict[f"#fn{i-1}x0"]}\">⤴</a></p></div>')
            footnote_html.append(contents)
    except FileNotFoundError:
        break
    except KeyError:
        break

# Add a new section for the footnotes just before the closing body tag.
footnote_preamble = '''<h3 class="sectionHead"><a id="x1-65536"></a>Footnotes</h3><p class="noindent" >'''
footnote_section = '\n'.join(footnote_html)
html = re.sub(r'</body>', f'{footnote_preamble+footnote_section}\n</body>', html)

with open ('mss-test.html', 'w') as file:
    file.write(html)
