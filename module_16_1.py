from fastapi import FastAPI

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Маршрут для главной страницы
@app.get("/", tags=["default"])
async def get_main_page():
    return "Главная страница"

# Маршрут для страницы администратора
@app.get("/user/admin", tags=["default"])
async def get_admin_page():
    return "Вы вошли как администратор"

# Маршрут для страницы пользователя с параметром в пути
@app.get("/user/{user_id}", tags=["default"])
async def get_user_number(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут для получения информации о пользователе с параметрами в адресной строке
@app.get("/user", tags=["default"])
async def get_user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
