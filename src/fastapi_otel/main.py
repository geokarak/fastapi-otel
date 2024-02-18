import time

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)


app = FastAPI()


@app.get("/")
def root():
    return {
        "msg": "Hello from my dummy instrumented API!",
        "author": "The G",
    }


@app.get("/io_task")
def io_task():
    count = 1
    while count <= 3:
        with tracer.start_as_current_span(f"loop-count-{count}"):
            count += 1
            time.sleep(1)
    return "I/O-bound task finished"


@app.get("/error_test")
async def error_test():
    raise ValueError("Value error!")
