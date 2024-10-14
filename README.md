# OTUS simple project


# Запуск проекта

## окружение

python -m venv venv
venv\Scripts\activate.bat


python.exe -m pip install --upgrade pip

pip install -r requirments-dev.txt
pip install -r requirments-lint.txt
pip install -r requirments-test.txt
pip install -r requirments.txt

## подцепить kernel
Python: Select Interpreter
В Select Interpreter выберите Enter interpreter path..., а затем Find...
найти python.exe

Project Description

## Запуск тестов

в git bash прописать путь
export PYTHONPATH=$(pwd)

в cmd
pytest --cov=src

# запуск трейн
в bash
python src/train.py

поднимаем UI
streamlit run src/app.py --server.port 8501


Для подключения к серваку:
установили клиент yc
https://yandex.cloud/ru/docs/cli/quickstart#linux_1

причем установил в bash терминал и powershell.
Потом поднялся сервак только в bash

для запуска VM (в баш терминале)

bash create_vm.sh otus-prod
заранее прописал все в metadata
yc compute instance list

Для гита
Делаем папку .github
внутри workflows
там main.yml

pip install pyyaml

заход по ключу (только через bash)

ssh -o IdentitiesOnly=yes -o IdentityFile=/c/Users/lenovo/.ssh/otus/otus-key-rsa ubuntu@51.250.14.125

заход для cmd и powershell
ssh -o IdentitiesOnly=yes -o IdentityFile=C:\Users\lenovo\.ssh\otus\otus-key-rsa ubuntu@51.250.14.125
