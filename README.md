# KICKS Web Store

This repository contains a Django sneakers web store  application that can be built and run using both a virtual environment (venv) and Docker. Below are the steps to set up and run the application using both methods.

## Content

- Installation
- Running with a Virtual Environmrnt
- Running with Docker
- Credit
- Repository URL


## Installations

Before getting started, ensure you have the following softtware installed on your system:

- Python 3.x
- Docker
- Git

## Running with a Virtual Environment

1. Open your CMD shell and clone the repository with this prompt:

        git clone https://github.com/PN-Ghub/shoe-store.git

2.  Navigate to the file directory where you want to run the app using prompt: 

        cd path\to\directory
   
3. Create virtual environment using: 

        python3 -m venv env-name

4. Activate your venv using: 

        venv\Scripts\activate (windows) or venv\bin\activate (Mac & Linux)

5. Install dependencies using: 

        pip install -r requirements.txt

6. Apply database migrations using: 

        python manage.py migrate

7. Run the development server using: 

        python manage.py runserver

8. Open your web browser of choice and run: http://localhost:8000

9. To stop the server from running press: 

        ctrl (cmd) + c

10. To deactivate the venv run: 

        deactivate 

## Running with Docker

1. Open your CMD shell and clone the repository with this prompt:

        git clone https://github.com/PN-Ghub/shoe-store.git

2.  Navigate to the file directory where you want to run the app using prompt: 

        cd path\to\directory

3. Ensure that docker is properly installed and build the docker image using:

        docker build -t shoe-store ./

4. Run the Docker Container:

        docker run --publish 8000:8000 shoe-store

5. Open your web browser of choice and run: http://localhost:8000

6. To stop and remove the Docker container, run:

        docker stop shoe-store
        docker rm shoe-store

## Credit
Philisani ([PN-Ghub](https://github.com/PN-Ghub))

## Repository URL
https://github.com/PN-Ghub/shoe-store.git