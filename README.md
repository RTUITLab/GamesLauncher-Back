# GameCenter
### Deploy

1. Install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/install/)

2. Rename `.env.example` to `.env` and change default values. 
If you want connect your postgres db fill  necessary variables in `.env`. 
Or you you can change `.env` file in `docker-compose.yml` on your own.

3. Run `docker-compose up`

------------

### Develop

##### Requirements install
1. Install python and pip: `sudo apt-get install python python-pip`

2. Install virtualenv: `pip install virtualenv`

3. Create venv: `python -m virtualenv env`

4. Activate venv:

    Linux:`source venv/bin/activate`   
    Windows Powershell:  `.\venv\Scripts\activate` 

5. Install poetry: `pip install poetry`  

6. Install all requirements: `poetry install`  
