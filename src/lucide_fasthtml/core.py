import json
import os
import requests
from bs4 import BeautifulSoup, FeatureNotFound
from fastcore.parallel import threaded

ICONS_FILE = os.path.join(os.getcwd(), 'icons.py')

ICONS = {}

def fetch_icon(icon_name):
    url = f"https://unpkg.com/lucide-static@latest/icons/{icon_name}.svg"
    response = requests.get(url)
    if response.status_code == 200:
        return extract_path_content(response.text)
    else:
        raise Exception(f"Failed to download icon {icon_name}")
    
def extract_path_content(svg_content):
    safe_tags = ['path', 'ellipse', 'line', 'polygon', 'polyline', 'rect', 'circle']
    safe_attrs = {
        'path': ['d'],
        'ellipse': ['cx', 'cy', 'rx', 'ry'],
        'line': ['x1', 'y1', 'x2', 'y2'],
        'polygon': ['points'],
        'polyline': ['points'],
        'rect': ['x', 'y', 'width', 'height', 'rx', 'ry'],
        'circle': ['cx', 'cy', 'r']
    }
    soup = BeautifulSoup(svg_content, features='lxml')
    sanitized_tags = []
    for tag in soup.find_all(safe_tags):
        new_tag = soup.new_tag(tag.name)
        for attr, value in tag.attrs.items():
            if attr in safe_attrs.get(tag.name, []):
                new_tag[attr] = value
        sanitized_tags.append(str(new_tag))

    if sanitized_tags:
        return ''.join(sanitized_tags)
    return None

def load_icons():
    global ICONS
    if os.path.exists(ICONS_FILE):
        with open(ICONS_FILE, 'r') as f:
            content = f.read()
            if content.strip():
                # Use exec to load ICONS into the global variable
                exec(content, globals())
    else:
        with open(ICONS_FILE, 'w') as f:
            f.write('ICONS = {}')

def save_icons():
    with open(ICONS_FILE, 'w') as f:
        f.write(f'ICONS = {json.dumps(ICONS)}')

def get_icon(icon_name):
    global ICONS
    
    if not ICONS:
        load_icons()
    
    if icon_name in ICONS:
        return ICONS[icon_name], False
    
    @threaded
    def download_and_save():
        path_content = fetch_icon(icon_name)
        if path_content:
            ICONS[icon_name] = path_content
            save_icons()
    
    download_and_save()
    return f"https://unpkg.com/lucide-static@latest/icons/{icon_name}.svg", True