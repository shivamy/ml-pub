from __future__ import print_function

# Script to download publicly shared google doc
import requests
import sys

CHUNK_SIZE = 1024 * 32
URL = "https://docs.google.com/uc?export=download"

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_shared_file_id local_file")
    else:
        file_id = sys.argv[1]
        destination = sys.argv[2] # local file
        download_file_from_google_drive(file_id, destination)

