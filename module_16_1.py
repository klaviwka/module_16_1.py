from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Создание экземпляра приложения FastAPI
app = FastAPI()

# Маршрут для главной страницы
@app.get("/", tags=["default"])
async def Get_Main_Page():
    return JSONResponse(content={"message": "Главная страница"})

# Маршрут для страницы администратора
@app.get("/user/admin", tags=["default"])
async def Get_Admin_Page():
    return JSONResponse(content={"message": "Вы вошли как администратор"})

# Маршрут для страницы пользователя с параметром в пути
@app.get("/user/{user_id}", tags=["default"])
async def Get_User_Number(user_id: int):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"})

# Маршрут для получения информации о пользователе с параметрами в адресной строке
@app.get("/user", tags=["default"])
async def Get_User_info(username: str, age: int):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"})
