import zipfile


def read_zip_contents(zip_name):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        for file_info in zipf.infolist():
            with zipf.open(file_info.filename) as file:
                content = file.read()
                print(f"Содержимое файла {file_info.filename}:")
                print(content[:100])


if __name__ == "__main__":
    read_zip_contents('resources/example.zip')
