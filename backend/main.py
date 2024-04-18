from fastapi import FastAPI  # Corrected import statement

import time
from connection import ConnectServer

app = FastAPI()  # Corrected FastAPI capitalization


@app.post("/")
async def hello():
    return {"message": "Hello World"}


@app.post("/new")
async def send_request():
    RETRIEVE (

        # Target the CSEBase itself
        to                      = cseBaseName,

        # Request Parameters
        originator              = defaultOriginator,  # Set the originator
        requestIdentifier       = '123',              # Unique request identifier
        releaseVersionIndicator = '3',                # Release version indicator
    )


if __name__ == "__main__":
    try:
        con = ConnectServer()
        con.start_cse()
        time.sleep(4)  # Introduce a delay of 3 seconds
        con.start_introduction()
        time.sleep(4)  # Introduce a delay of 3 seconds
        con.start_notification_server()
    except Exception as e:
        print(f"An error occurred: {e}")
