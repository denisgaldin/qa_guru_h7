import zipfile
import os


def create_zip(zip_name, file_names):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_names:
            zipf.write(file, os.path.basename(file))


if __name__ == "__main__":
    files_to_zip = [
        'resources/example.pdf',
        'resources/example.xlsx',
        'resources/example.csv'
    ]
    create_zip('resources/example.zip', files_to_zip)
    print("ZIP архив создан: resources/example.zip")
