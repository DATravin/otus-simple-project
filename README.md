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
