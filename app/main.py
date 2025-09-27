from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "ok": True,
        "msg": "hello from devsec-fastapi-demo",
        "version": "1.0.1",
        "status": "workflows-tested",
    }
