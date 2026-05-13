
with open(r'c:\Users\feeld\OneDrive\Desktop\homepage\homepage\fseq.html', 'r', encoding='utf-8') as f:
    content = f.read()

showcase_start = content.find('<section id="video-showcase"')
showcase_end = content.find('<section id="system-requirements"')
showcase_content = content[showcase_start:showcase_end]

open_divs = showcase_content.count('<div')
close_divs = showcase_content.count('</div>')

print(f"Open divs: {open_divs}")
print(f"Close divs: {close_divs}")

# Check individual video items
items = showcase_content.split('video-page-item')
print(f"Number of video items: {len(items) - 1}")

for i, item in enumerate(items[1:], 1):
    o = item.count('<div')
    c = item.count('</div>')
    print(f"Item {i}: Open={o}, Close={c}")
