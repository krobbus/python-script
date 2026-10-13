from pathlib import Path
import shutil

directory_map = {
  "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
  "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
  "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
  "Code": [".py", ".js", ".html", ".css", ".json", ".sql", ".ts"],
  "Installers": [".exe", ".msi", ".dmg", ".pkg"]
}

def organize_folder(target_path):
  # validating path
  target_dir = Path(target_path)

  if not target_dir.exists() or not target_dir.is_dir():
    print(f"Error: The path '{target_path}' is not a valid directory.")
    return

  print(f"\nScanning directory: {target_dir.resolve()}...\n")

  moved_count = 0
  # snapshot and grab folder contents, store in a list
  items = list(target_dir.iterdir())

  for item in items:
    # skip subfolders and look for file extension
    if item.is_dir() or not item.exists():
      continue

    file_extension = item.suffix.lower()
    moved = False

    for category, extensions in directory_map.items():
      if file_extension in extensions:
        category_dir = target_dir / category
        # create destination folder if doesnt exist
        category_dir.mkdir(exist_ok=True)
        destination = category_dir / item.name

        # add "_duplicate" to the filename if there's same filename inside the destination folder
        if destination.exists():
          destination = category_dir / f"{item.stem}_duplicate{item.suffix}"

        # move the file to the destination
        if item.exists():
          shutil.move(str(item), str(destination))
          print(f"Moved: {item.name} -> {category}/")
          moved_count += 1
          moved = True
        break

    # instead throwing an error if there's no matching file ext, throw the file in "Others" folder
    if not moved and item.exists():
      others_dir = target_dir / "Others"
      others_dir.mkdir(exist_ok=True)
      destination = others_dir / item.name

      if destination.exists():
        destination = others_dir / f"{item.stem}_duplicate{item.suffix}"

      if item.exists():
        shutil.move(str(item), str(destination))
        print(f"Moved: {item.name} -> Others/")
        moved_count += 1

  print(f"\nDone! Successfully organized {moved_count} files.\n")

if __name__ == "__main__":
  print("=== Automated File & Folder Organizer ===")
  path_input = input("Enter the full path of the folder you want to organize: ").strip()
  path_input = path_input.strip('"\'')

  if path_input:
    organize_folder(path_input)
  else:
    print("No path provided. Exiting.")