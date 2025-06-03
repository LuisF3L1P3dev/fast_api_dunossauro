dentro da pasta fastapi_zero:
<poetry shell>
em fastapi_zero/fastapi_zero:
<poetry run fastapi dev app.py>

ruff check . # para checar  
ruff format . # para formatar  
fastapi dev fast_zero/app.py # para rodar a aplicação  
pytest --cov=fast_zero -vv # teste  
coverage html # cobertura  