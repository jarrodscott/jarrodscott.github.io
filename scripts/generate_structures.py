import argparse
import os
import subprocess
import time
import urllib.error
import urllib.request


def download_single_sdf_native(cid, output_dir):
    """Downloads an individual SDF file using Python's native urllib stack to bypass 503 limits."""

    # Breaking down the domain string to safeguard the code block layout
    d1, d2, d3, d4, d5 = "pubchem", "ncbi", "nlm", "nih", "gov"
    base_domain = f"{d1}.{d2}.{d3}.{d4}.{d5}"

    # Reconstruct your exact target path format
    url = f"https://{base_domain}/rest/pug/compound/cid/{cid}/record/SDF"
    sdf_path = os.path.join(output_dir, f"{cid}.sdf")

    # Native browser-mimicking headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    # Extended cooldown delay between separate network calls to clear the gateway firewall
    time.sleep(3.5)

    max_retries = 3
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=headers)

            # Open connection using native socket wrapper
            with urllib.request.urlopen(req, timeout=20) as response:
                html_content = response.read().decode("utf-8")

                with open(sdf_path, "w", encoding="utf-8") as file:
                    file.write(html_content)

                print(f"[✓] Preserved file: {cid}.sdf")
                return sdf_path

        except urllib.error.HTTPError as e:
            if e.code == 503:
                # Deep cooldown backoff to completely clear server-side traffic buckets
                wait_time = 15 * (attempt + 1)
                print(
                    f"[!] Server 503 throttle on CID {cid}. Waiting {wait_time}s for native connection reset..."
                )
                time.sleep(wait_time)
            else:
                print(f"[X] Request rejected for CID {cid}. HTTP Status: {e.code}")
                return None
        except Exception as e:
            print(f"[X] Native socket layer failed for CID {cid}: {e}")
            return None

    print(f"[X] Skipped CID {cid} after native retry limits.")
    return None


def convert_sdf_to_png(sdf_path, cid, output_dir, image_resolution):
    """Feeds the local SDF file directly to Open Babel using format-specific sizing options."""
    png_path = os.path.join(output_dir, f"{cid}.png")

    # FIXED COMMAND STRUCTURE:
    # -xw <pixels> specifies the image width parameter
    # -xh <pixels> specifies the image height parameter
    command = [
        "obabel",
        sdf_path,
        "-isdf",
        "-opng",
        "-d",
        f"-O{png_path}",
        f"-xw", f"{image_resolution}",
        f"-xh", f"{image_resolution}",
    ]

    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"[✓] Generated high-res graphic ({image_resolution}x{image_resolution}): {cid}.png")
        return png_path
    except FileNotFoundError:
        print("[X] Execution Error: 'obabel' command line utility not found.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[X] Open Babel failed for {cid}.sdf: {e.stderr}")
        return None


def main():
    # Setting up command line argument parsing
    parser = argparse.ArgumentParser(
        description="Download PubChem SDF files and convert to high-res PNG structures."
    )
    parser.add_argument(
        "--cids",
        nargs="+",
        type=int,
        required=True,
        help="Space-separated list of PubChem Compound IDs (CIDs).",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory path where output files will be saved.",
    )
    args = parser.parse_args()

    cid_list = args.cids
    output_dir = args.output_dir
    
    # ADJUST THIS VALUE FOR SHARPER RENDER OUTPUTS (e.g., 2000, 3000, 4000)
    image_resolution = 2000  

    os.makedirs(output_dir, exist_ok=True)

    print(f"Beginning individual processing loop for {len(cid_list)} items...")

    for cid in cid_list:
        # Step 1: Download and store separate individual molecule structure using native stack
        sdf_file = download_single_sdf_native(cid, output_dir)

        # Step 2: Pass that local independent file straight to Open Babel
        if sdf_file and os.path.exists(sdf_file):
            convert_sdf_to_png(sdf_file, cid, output_dir, image_resolution)

    print("\nBatch task completed.")
    print("Files successfully saved to:", os.path.abspath(output_dir))


if __name__ == "__main__":
    main()
