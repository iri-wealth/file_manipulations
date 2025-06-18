import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir) / "archive.zip"
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
        return dest_path

if __name__ == "__main__":
    filepaths = ['file1.txt', 'file2.txt', 'file3.txt']
    dest_dir = '.'
    archive_path = make_archive(filepaths, dest_dir)
    print(f"Archive created at: {archive_path}")
