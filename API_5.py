import uvicorn
from fastapi import FastAPI, Response
from fastapi .params import Body
app = FastAPI(debug=True)
@app.get("/")
def root():
    return {"message": "Hello world"}
@app.get("/hello/{name}")
def hello_by_name(name: str):
    return {"message": f"Hello {name}"}
@app.get("/parametrs")
async def get_parametrs(name:str, age:int = 18, message: str | None = None):
    print(name)
    print(age)
    # message(message)
    return {"user": {"name": name, "age": age, "message": message}}
@app.get("/various-data")
async def get_var_data(payload: dict = Body(...)):
    return {"all_transmited_data"}
if __name__ == "__main__":
    uvicorn.run(app, port=8000)