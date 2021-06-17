
[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/wordcount-exercise/badge.svg?branch=main)](https://coveralls.io/github/jalvaradosegura/wordcount-exercise?branch=main)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

# wordcount-exercise
Send a .txt file from the client to the server. The server will respond a .json, with the ocurrences amount of each word within the .txt file. Then the client will parse this response and print it to the console.

![alt text](https://i.imgur.com/kF3aIhK.png)
> The group of kanjis means Katana

## Structure
It's worth mentioning that the are 3 Makefiles within the project. Each of them show you the most common commands used by each codebase. Press on the codebases of the following table to see their respective Makefile:

| Codebase                                                                                                   |      Summary              |
| :--------------------------------------------------------------------------------------------------------: | :-----------------------: |
| [backend/](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/backend/Makefile)               |      Django + DRF + numpy |
| [client/](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/client/Makefile)                 |      Python + requests    |
| [./](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/Makefile)                             |      docker-compose       |

## Install & run
### 🐳 Using Docker
If you have [Docker](https://docs.docker.com/engine/install/) installed, this will be very easy:

```sh
# Option 1
# On the root of the project (This will install and immediately send a request)
docker-compose up --build

# Option 2
# If you are using Linux or macOS you can also run the project by using the Makefile (On the root of the project as well)
make run
```

> If you are on Windows and you want to use the Makefile, check out [how to run a Makefile](https://stackoverflow.com/questions/2532234/how-to-run-a-makefile-in-windows) or just take a look at our [Makefile](https://github.com/jalvaradosegura/wordcount-exercise/blob/main/Makefile) and run the commands manually.

### 🐍 Using Python
If you don't want to use Docker you can go and use just Python. You will have to install the libraries for each codebase:
```sh
# Note: feel free to use pip instead of pipenv
# Go to the backend folder and install the dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Run the server
python manage.py runserver

# On a new tab, go to the client folder and install the dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Run the client
python3 wordcount_client.py -f document.txt
```
> Each codebase has a requirements.txt in case you want to use pip instead of pipenv. So you can execute: pip install -r requirements.txt
