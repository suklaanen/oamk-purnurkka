from subprocess import PIPE, Popen

from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/")
async def root():
    output = "<html><head><title>Cowsay</title></head><body><pre style='font-family:monospace;'>"
    output += Popen(["cowsay", "-t", "Hello World!"], stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "<br>")
    output += "</pre></html>"
    response = Response(content=output, media_type="text/html")
    return response


@app.get("/{text}")
async def say_hello(text: str):
    output = "<html><head><title>Cowsay</title></head><body><pre style='font-family:monospace;'>"
    output += Popen(["cowsay", "-t", text], stdout=PIPE).stdout.read().decode('utf-8').replace("\n", "<br>")
    output += "</pre></html>"
    response = Response(content=output, media_type="text/html")
    return response
