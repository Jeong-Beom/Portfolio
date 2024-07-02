# Portfolio
### 시작 가이드
#### Installation
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

8. requirements.txt 내용으로 필요 패키지 설치