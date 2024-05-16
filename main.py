from fastapi import FastAPI

from routers.salaries import router as salaries_router
from routers.tokens import router as tokens_router
from routers.users import router as users_router

app = FastAPI()


app.include_router(router=users_router, prefix="/users")

app.include_router(router=tokens_router, prefix="/tokens")

app.include_router(router=salaries_router, prefix="/salaries")


@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в наш сервис просмотра текущей зарплаты и даты следующего повышения!"
    }
