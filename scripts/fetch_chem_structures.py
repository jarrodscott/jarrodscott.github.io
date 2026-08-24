import os
import requests
import time

# 1. Configuration
# Put your list of CIDs here (190=Adenine, 2244=Aspirin, 5793=Caffeine)
CID_LIST = [190, 2244, 5793]
IMAGE_SIZE = "1200x1200"

# Blowfish target directories
OUTPUT_IMG_DIR = "assets/chemistry/images/"
OUTPUT_SDF_DIR = "assets/chemistry/sdf/"

os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)
os.makedirs(OUTPUT_SDF_DIR, exist_ok=True)

PUG_REST_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

# CRITICAL FIX: Add a custom header so PubChem allows the connection
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_assets():
    for cid in CID_LIST:
        print(f"\n--- Fetching Compound ID: {cid} ---")
        
        img_url = f"{PUG_REST_BASE}/compound/cid/{cid}/PNG?image_size={IMAGE_SIZE}"
        sdf_url = f"{PUG_REST_BASE}/compound/cid/{cid}/SDF"
        
        # 1. Download High-Res Image
        try:
            img_res = requests.get(img_url, headers=HEADERS, timeout=15)
            if img_res.status_code == 200:
                img_path = os.path.join(OUTPUT_IMG_DIR, f"{cid}.png")
                with open(img_path, "wb") as f:
                    f.write(img_res.content)
                print(f" Success: Saved High-Res image -> {img_path}")
            else:
                print(f" Error: Image download failed for CID {cid} (Status: {img_res.status_code})")
        except Exception as e:
            print(f" Network exception on image fetch: {e}")

        # 2. Download Raw SDF Blueprint
        try:
            sdf_res = requests.get(sdf_url, headers=HEADERS, timeout=15)
            if sdf_res.status_code == 200:
                sdf_path = os.path.join(OUTPUT_SDF_DIR, f"{cid}.sdf")
                with open(sdf_path, "wb") as f:
                    f.write(sdf_res.content)
                print(f" Success: Saved Structural SDF -> {sdf_path}")
            else:
                print(f" Error: SDF download failed for CID {cid} (Status: {sdf_res.status_code})")
        except Exception as e:
            print(f" Network exception on SDF fetch: {e}")
            
        # Throttling protection to safeguard your IP from being banned
        time.sleep(0.5)

if __name__ == "__main__":
    fetch_assets()
