from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message, UserSchema, UserPublic

app = FastAPI(title='MinhaAPI')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello world'}
    # return Message(message='hello world')


@app.get('/page', response_class=HTMLResponse)
def read_page_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

@app.post('/users/', status_code=HTTPStatus.CREATED,
    response_model=UserPublic    
    )
def create_user(user: UserSchema):
    return user
