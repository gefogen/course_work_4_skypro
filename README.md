# SkyPro Coursework 4

## ⚡ Quick Setup

### Windows
- Create venv and install requirements
    ```shell
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
- run script
    ```shell
    python run.py
    ```
- Open [http://127.0.0.1:25000/]()

### MacOS/Linux
- Create venv and install requirements
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
- run script
    ```shell
    python3 run.py
    ```
- Open [http://127.0.0.1:25000/]()

## 🔧 Settings

| Url|Methods|
|----|----|
|`/movies/`|`GET` params: status, page.|
|`/movies/<id>`|`GET`|
|`/genres/`|`GET` param: page|
|`/genres/<id>`|`GET`|
|`/directors/`|`GET` param: page|
|`/directors/<id>`|`GET`|
|`/auth/register`|`POST`|
|`/auth/login`|`POST`, `PUT`|
|`/user/`|`GET`, `PATCH`|
|`/user/password`|`PUT`|