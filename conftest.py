import shutil
import pytest
import os
from zipfile import ZipFile

from script_os import (
    FILES_DIR,
    FILES2_DIR,
    ARCHIVE_FILE
)


@pytest.fixture(scope="function", autouse=True)
def create_ziparchive_and_extract():
    if not os.path.exists(ARCHIVE_FILE):
        with ZipFile(ARCHIVE_FILE, 'w') as zip_file:
            for file in os.listdir(FILES_DIR):
                zip_file.write(os.path.join(FILES_DIR, file), file)

    if not os.path.exists(FILES2_DIR):
        os.mkdir(FILES2_DIR)

    with ZipFile(ARCHIVE_FILE, 'r') as zip_file:
        zip_file.extractall(FILES2_DIR)

    yield

    shutil.rmtree(FILES2_DIR)
