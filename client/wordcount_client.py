from http import HTTPStatus
import os
import sys
import time

import requests


def main():
    # Wait for the server to start up
    time.sleep(3)

    RUN_ON_CONTAINER = os.getenv('RUN_ON_CONTAINER', 'False') == 'True'
    host = 'backend' if RUN_ON_CONTAINER else 'localhost'
    endpoint = f'http://{host}:8000/api/v1/upload_file/'
    file_to_send = sys.argv[2]

    try:
        with open(file_to_send, 'rb') as f:
            files = {'file': f}
            response = requests.post(endpoint, files=files)
    except FileNotFoundError:
        print(f'Error: {file_to_send} not found.')
    else:
        if response.status_code == HTTPStatus.CREATED:
            words = response.json()
            {print(key, value) for (key, value) in words.items()}
        else:
            print('Something did not go as expected.')


if __name__ == '__main__':
    main()
