from fastapi import FastAPI

from routers.salaries import router as salaries_router
from routers.tokens import router as tokens_router
from routers.users import router as users_router

description = """
REST - сервис на FastAPI для просмотра текущей зарплаты и даты следующего повышения


Это приложение может:
1. Показать базовую информацию о приложении;
2. Получить список всех пользователей;
3. Зарегистрировать нового пользователя;
4. Получить информацию о текущем пользователе по токену;
5. Создать новый токен для пользователя;
6. Получить информацию о текущей зарплате и дате следующего повышения для пользователя;
7. Добавить или обновить информацию о зарплате для пользователя.
"""

tags = [{"name": "Допустимые операции"}]


app = FastAPI(
    title="Сервис для просмотра текущей зарплаты и даты следующего повышения",
    description=description,
    openapi_tags=tags,
    contact={
        "name": "Асташов И. В.",
        "url": "https://github.com/igorastashov",
    },
)


@app.get("/", tags=["1. Показать базовую информацию о приложении"])
async def root():
    return {
        "message": "Добро пожаловать в наш сервис просмотра текущей зарплаты и даты следующего повышения!"
    }


app.include_router(router=users_router, prefix="/users")

app.include_router(router=tokens_router, prefix="/tokens")

app.include_router(router=salaries_router, prefix="/salaries")
