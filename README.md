
[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/wordcount-exercise/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/wordcount-exercise?branch=main)

# wordcount-exercise
Send a .txt file from the client to the server. The server will respond a .json, with the ocurrences amount of each word within the .txt file. Then the client will parse this response and print it to the console.

![alt text](https://i.imgur.com/kF3aIhK.png)
> The group of kanjis means Katana

## Structure

| Codebase               |      Summary              |
| :--------------------: | :-----------------------: |
| backend/               |      Django + DRF + numpy |
| client/                |      Python + requests    |

## Install & run
### 🐳 Using Docker
If you have [Docker](https://docs.docker.com/engine/install/) installed, this will be very easy:

#### Linux / MacOS
```sh
# On the root (This will install and immediately send a request)
make run
```

> If you are on Windows, check out how to run Makefile's or just take a look at our [Makefile](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/Makefile) and run the commands manually.

### 🐍 Using Python
#### Linux / macOS / Windows
If you don't want to use Docker you can go and use just Python. You will have to install the libraries for each codebase:
```sh
# Note: feel free to use pip instead of pipenv
# Go to the backend folder and install the dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Run the server
make run

# On a new tab, go to the client folder and install the dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Run the client
python wordcount_client.py -f document.txt
```
> There is also have a very useful [Makefile](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/backend/Makefile) for the backend.

