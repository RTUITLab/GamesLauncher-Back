# GameCenter
### Start server

Install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/install/)

Rename `.env.example` to `.env` and change default values. 
If you want connect your postgres db fill  necessary variables in `.env`. 
Or you you can change `.env` file in `docker-compose.yml` on your own.

Run `docker-compose -f .\docker-compose.yml up`

Add `-d` in command for background run

------------

### Develop

##### Requirements install
1. Install python and pip: `sudo apt-get install python python-pip`

2. Install virtualenv: `pip install virtualenv`

3. Create venv: `python -m virtualenv env`

4. Activate venv: `source venv/bin/activate`   or    `.\venv\Scripts\activate`   for Windows Powershell

5. Install poetry: `pip install poetry`  

6. Install all requirements: `poetry install`  
