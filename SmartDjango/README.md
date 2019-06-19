# Smart

Website feito para o trabalho da disciplina PROJETO DE DESENVOLVIMENTO DE SISTEMAS.

Alunos: Osmar Fagundes; Pedro Henrique; Marco Aurélio

## Para Instalar

Para instalar as dependências do projeto, executar:

```bash
python --version
```

```bash
sudo apt-get install python python3
```


**OBS: É viavel a criação de uma virtualenv para isolar sua maquina ao instalar dependencias da aplicação, para que assim
possamos ter um ambiente voltado ao projeto sem interferir o seu sistema.

Na pasta do projeto (No caso SmartDjango) executa-se o comando abaixo para cirar sua virtualenv:

```bash
python -m venv NOMEVIRTUALENV
```
Após sua criação execute:

```bash
cd NOMEVIRTUALENV
```
para ativar sua virtualenv:

```bash
source NOMEVIRTUALENV/bin/activate
```
no caso do windows:

```bash
NOMEVIRTUALENV\Scripts\activate
```
Após sua ativação, proxiga instalando as dependencias do projeto:

```bash
pip3 install -U Django
```

```bash
pip3 install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python3 manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python3 manage.py migrate
```

Criando SUPERUSER para acesso à aplicação:

```bash
python3 manage.py createsuperuser
```

## Para Executar

```bash
python3 manage.py runserver
```
