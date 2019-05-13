# Yandex email list parser.  

This simple scripts makes a txt file with all emails, registered on your corporate domain.

### How to install

Python has to be installed on your system. Use pip (or pip3 if there is conflict with Python 2) to install dependences.
```
pip install -r requirements.txt
```
It is recommended to use virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) to isolate your project.  

Warning! Create `.env` file in your rpoject's folder and put in variable named 'pdd_token'. You can get token itself [here](https://pddimp.yandex.ru/api2/admin/get_token).

### Quickstart

Type into console:   
```
$python emails_yandex.py
```
### Project goals

It's handy script, which simplifies email administrative work.
