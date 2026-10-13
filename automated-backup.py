from datetime import datetime
import os
from pathlib import Path
import shutil

def create_backup(source_dir, backup_dest_dir):
  source_path = Path(source_dir)
  dest_dir = Path(backup_dest_dir)

  # throw error if there's no existing path to backup
  if not source_path.exists() or not source_path.is_dir():
    print(f"Error: The source path '{source_dir}' is not a valid directory.")
    return
  
  # create backup if doesn't exist
  dest_dir.mkdir(parents=True, exist_ok=True)

  # generate timestamp in backup filename
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  archive_name = f"{source_path.name}_backup_{timestamp}"
  archive_path = dest_dir / archive_name

  print(f"\nPackaging '{source_path.name}' into a compressed zip file...")

  try:
    # compressed to zip file
    shutil.make_archive(
      base_name=str(archive_path), format="zip", root_dir=str(source_path)
    )
    print(f"Success! Backup safely stored at: {archive_path}.zip\n")
  except Exception as e:
    print(f"Error during backup: {e}")

if __name__ == "__main__":
  print("=== Automated Backup & Archive Tool ===")
  src_input = input("Enter the path of the folder you want to back up: ").strip()
  src_input = src_input.strip('"\'')

  dest_input = input("Enter destination folder for backups (press Enter for default './backups'): ").strip()
  dest_input = dest_input.strip('"\'')

  if not dest_input:
    dest_input = "./backups"

  if src_input:
    create_backup(src_input, dest_input)
  else:
    print("No source path provided. Exiting.")