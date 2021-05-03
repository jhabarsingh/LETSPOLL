# [LETSPOLL](https://letpoll.herokuapp.com/) <img width="45px" src="https://github.com/jhabarsingh/LETSPOLL/blob/master/static/img/survey.png?raw=true" />


<details>
  <summary>:zap: TECH STACK</summary>
  <br/>
  <div style="display:flex;justify-content:space-around">
    <img  title="Django" src="https://icon-library.com/images/django-icon/django-icon-0.jpg" width="50px" height="50px" style="margin-right:5px;" />
    <img title="Heroku"  src="https://www.thedevcoach.co.uk/wp-content/uploads/2020/04/heroku.png" height="50px"  style="margin-right:5px;"/> 
    <img  title="Docker" src="https://pbs.twimg.com/profile_images/1273307847103635465/lfVWBmiW_400x400.png" height="50px" style="margin-right:5px;" />
    <img  title="Tailwind css" src="https://cms-assets.tutsplus.com/uploads/users/30/posts/34128/preview_image/tailwindcss-pre.png" height="50px" style="margin-right:5px;" />
  </div>
</details>

## About

![Website Demo](https://github.com/jhabarsingh/LETSPOLL/blob/master/static/img/home.gif?raw=true)
 
[**LETSPOLL**](https://letpoll.herokuapp.com/)  is an Open Source and Free Web App built using Django for creating Polls and Let you share the poll's result with others.
It has the following features:
  1. You can create a Poll once Registered.
  2. Generate Unique Url for every poll so that you can share It with others.
  3. Poll results are displayed using charts.
  4. You can search all the polls created by a user

## Project Setup On Desktop

### Using venv
```bash
git clone https://github.com/jhabarsingh/LETSPOLL.git 
cd LETSPOLL
python3 -m venv env # Python 3.6.9 or 3.7.0 version 
source env/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using conda
```bash
git clone https://github.com/jhabarsingh/LETSPOLL.git
cd LETSPOLL
conda create -n letspoll python==3.7 
conda activate letspoll
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py runserver
```

### Using Docker

```bash
sudo apt-get install docker docker-compose # Install docker, docker-compose on linux
git clone https://github.com/jhabarsingh/LETSPOLL.git
cd LETSPOLL
sudo docker-compose up
```


## [Want To Contribute](https://medium.com/mindsdb/contributing-to-an-open-source-project-how-to-get-started-6ba812301738)
### You can contribute to this project in many ways
 1. You can create an issue if you find any bug.
 2. You can work on an existing issue and Send PR.
 3. You can make changes in the design if it is needed.
 4. Even if you find any grammatical or spelling mistakes then also you can create an issue.

> *I would be glad to see a notification saying `User {xyz} created a Pull Request`.
I promise to review it.*
