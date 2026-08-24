import os
import sys
import re
import pubchempy as pcp

def generate_hugo_gallery(directory, gallery_name):
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Extract the name of the folder from the path (e.g., '/path/to/my_photos' -> 'my_photos')
    folder_name = os.path.basename(os.path.normpath(directory))

    # Find all PNG files in the specified directory
    files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]
    
    # Sort files numerically by CID
    def get_sort_key(filename):
        match = re.match(r'^(\d+)\.png$', filename, re.IGNORECASE)
        return (0, int(match.group(1))) if match else (1, filename)
    
    files.sort(key=get_sort_key)

    lines = []
    lines.append("{{< gallery >}}")

    for filename in files:
        match = re.match(r'^(\d+)\.png$', filename, re.IGNORECASE)
        if not match:
            continue
            
        cid = int(match.group(1))
        
        try:
            comp = pcp.Compound.from_cid(cid)
            caption = comp.synonyms[0] if comp.synonyms else f"CID {cid}"
        except Exception:
            caption = f"CID {cid}"

        # Dynamically inject the folder name into the src attribute
        line = f'  {{{{< lightbox src="{folder_name}/{filename}" gallery="{gallery_name}" caption="{caption}" >}}}}'
        lines.append(line)

    lines.append("{{< /gallery >}}")
    print("\n".join(lines))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_gallery.py <directory_path> <gallery_name>")
        sys.exit(1)
        
    dir_path = sys.argv[1]
    gal_name = sys.argv[2]
    generate_hugo_gallery(dir_path, gal_name)
