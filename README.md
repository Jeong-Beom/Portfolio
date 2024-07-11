# Portfolio
----------------------
> - 프로젝트 소개: 나만의 Portfolio 사이트 만들기
> - 개발기간: 2024.07.01~2024.07.11
> - 기술스택
>> Environment
>>> <img src ="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=for-the-badge&logo=Ubuntu&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/visualstudiocode-007ACC.svg?&style=for-the-badge&logo=visualstudiocode&logoColor=white"/>
>>><img src ="https://img.shields.io/badge/git-F05032.svg?&style=for-the-badge&logo=git&logoColor=white"/>
>>><img src ="https://img.shields.io/badge/github-181717.svg?&style=for-the-badge&logo=github&logoColor=white"/>
>> Development
>>> <img src ="https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/html5-E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/css3-1572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/bootstrap-7952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/>
>> Deployment
>>> <img src ="https://img.shields.io/badge/microsoftazure-0078D4.svg?&style=for-the-badge&logo=microsoftazure&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/amazonwebservices-232F3E.svg?&style=for-the-badge&logo=amazonwebservices&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/nginx-009639.svg?&style=for-the-badge&logo=nginx&logoColor=white"/>
>>> <img src ="https://img.shields.io/badge/gunicorn-499848.svg?&style=for-the-badge&logo=gunicorn&logoColor=white"/>

----------------------------------------------------------------------------

### 코드 변경시 적용 기본 사항
1. git push
2. git pull
3. sudo systemctl restart portfolio.service
4. sudo systemctl restart nginx

----------------------------------------------------------------------------

### 시작 가이드
#### Installation(11번 부터는 운영 서버에서만 진행)
1. Install git
```bash
sudo apt-get install git
```
2. Install curl
```bash
sudo apt-get install curl
```
3. Install pyenv
```bash
curl https://pyenv.run | bash
```

4. Install packages
```bash
sudo apt-get update;
sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget llvm liblzma-dev \
libncurses-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev \
libffi-dev python3-tk
``` 

5. Change Time zone
```bash
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

6. PATH 등록(~/.bashrc 또는 ~/.bash_profile에 등록)
```
# pyenv path add
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# pyenv-virtualenv add
eval "$(pyenv virtualenv-init -)"
```

7. python 설치 및 가상환경 생성
```bash
# Install python on pyenv
pyenv install 3.12.4

# Create virtual env
pyenv virtualenv 3.12.4 venv_portfolio
```

8. git clone
```bash
git clone https://github.com/Jeong-Beom/Portfolio.git
```

9. 가상환경 진입 후 requirements.txt 내용으로 필요 패키지 설치
```bash
# 개발서버에서 진입시 사용
. enter_local.sh

# 운영서버에서 진입시 사용
. enter_prod.sh
```
```python
pip install wheel # 해당 패키지는 운영 서버에서만 설치

pip install -r requirements.txt
```

10. Create .env file(+ migrate)
```bash
sudo nano .env
```
``` bash
# 개발환경
SECRET_KEY={Django Secret Key}
DEBUG=True

# 운영환경
SECRET_KEY={Django Secret Key}
IP={IP 주소}
DEBUG=False
DOMAIN={Domain 주소}
DJANGO_SETTINGS_MODULE=config.settings.prod
```
```python
# Django 운영시 필요한 파일들 생성(.gitignore에 위치하여 없는 파일들 대상)
python manage.py migrate
```
----------------------------------------------------------------------------
11. Install gunicorn(WSGI), nginx(Web Server)
```python
pip install gunicorn
```
```bash
sudo apt install nginx
```

12. Move to '/etc/systemd/system/' and create service file.
- check user, group info
```bash
id
```
- create service file
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=imadmin
Group=imadmin
WorkingDirectory=/home/imadmin/Portfolio
EnvironmentFile=/home/imadmin/Portfolio/.env
ExecStart=/home/imadmin/.pyenv/versions/venv_portfolio/bin/gunicorn \
        --workers 2 \
        --bind unix:/tmp/gunicorn.sock \
        config.wsgi:application

[Install]
WantedBy=multi-user.target
```
- execute portfolio.service and check error.
```bash
sudo systemctl daemon-reload
sudo systemctl start portfolio.service
sudo systemctl status portfolio.service
sudo systemctl enable portfolio.service
```

13. Move to '/etc/nginx/sites-available/' and create file for nginx.
- create portfolio file
```bash
sudo nano portfolio
```
```
# portfolio - if it doesn't exist domain. it is needed to open 80 port. it is needed to change as environment.
server {
       listen 80;
       server_name {IP 주소};

       location = /favicon.ico { access_log off; log_not_found off; }

       location /static {
               alias /home/imadmin/Portfolio/static;
       }

       location / {
               include proxy_params;
               proxy_pass http://unix:/tmp/gunicorn.sock;
       }
}

# portfolio - if it exists domain. it is needed to open 80, 443 port. it is needed to change as environment.
server {
       listen 80;
       server_name {도메인 명칭};
       rewrite ^https://$server_name$request_uri? permanent;
}

server {
       listen 443 ssl;
       server_name {도메인 명칭};

       ssl_certificate /etc/letsencrypt/live/{도메인 명칭}/fullchain.pem; # managed by Certbot
       ssl_certificate_key /etc/letsencrypt/live/{도메인 명칭}/privkey.pem; # managed by Certbot
       include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot

       location = /favicon.ico { access_log off; log_not_found off; }

       location /static {
               alias /home/imadmin/Portfolio/static;
       }

       location / {
               include proxy_params;
               proxy_pass http://unix:/tmp/gunicorn.sock;
       }
}
```
- move to '/etc/nginx/sites-enabled/' and delete default. create portfolio(link)
```bash
sudo rm default
sudo ln -s /etc/nginx/sites-available/portfolio
```
- check error and restart nginx
```bash
sudo nginx -t
sudo systemctl restart nginx
```

14. Move to project directory(~/Portfolio/) and execute commands.
```python
python manage.py collectstatic
sudo systemctl restart portfolio.service
```