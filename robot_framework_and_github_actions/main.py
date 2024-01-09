from subprocess import PIPE, Popen

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    output = Popen(["cowsay", "-t", "Hello World!"], stdout=PIPE).stdout.read()
    return {"message": output}


@app.get("/{text}")
async def say_hello(text: str):
    output = Popen(["cowsay", "-t", text], stdout=PIPE).stdout.read()
    return {"message": output}
