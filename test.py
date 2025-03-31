from pathlib import Path

DATA_DIR = Path.home() / "3DCityDB-Importer-Exporter/3d-web-map-client/data/Tiles/0/0"
REPO_DIR = Path(__file__).parent

# loop through all files in the dir that end with .gltf, also in subdirectories
gltf_files = DATA_DIR.rglob("*.gltf")

for file in gltf_files:
    # copy to REPO_DIR

    new_file = REPO_DIR / file.name
    if not new_file.exists():
        print(f"Copying {file} to {new_file}")
        new_file.write_text(file.read_text())
    else:
        print(f"{new_file} already exists, skipping.")
