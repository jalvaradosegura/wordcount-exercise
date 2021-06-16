from http import HTTPStatus
import sys

import requests


def main():
    file_to_send = sys.argv[2]
    endpoint = 'http://localhost:8000/api/v1/upload_file/'

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
