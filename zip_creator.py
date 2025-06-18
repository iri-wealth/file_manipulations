import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir) / "archive.zip"
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
        return dest_path

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)
    return dest_dir

if __name__ == "__main__":
    filepaths = ['file1.txt', 'file2.txt', 'file3.txt']
    dest_dir = '.'
    archive_path = make_archive(filepaths, dest_dir)
    print(f"Archive created at: {archive_path}")

    # Test extraction
    extract_dir = pathlib.Path('extracted_files')
    extracted_path = extract_archive(archive_path, extract_dir)
    print(f"Files extracted to: {extracted_path}")