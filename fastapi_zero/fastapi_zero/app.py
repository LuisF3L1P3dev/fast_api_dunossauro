from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import (
    Message,
    UserCreate,
    UserDB,
    UserList,
    # UserPublic,
    UserResponse,
    UserSchema,
)

app = FastAPI(title='MinhaAPI')

database = []


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
        <h1> hello world </h1>
      </body>
    </html>"""


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserResponse
)
def create_user(user: UserCreate):
    user_with_id = UserDB(
        **user.model_dump(),
        id=len(database) + 1,
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserResponse,
)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(
        **user.model_dump(),
        id=user_id,
    )

    database[user_id - 1] = user_with_id

    return user_with_id
