from wendy import *
from fastapi import status
from wendy.utilities import messages


@app.get('/', response_model=ResponseModel, status_code=status.HTTP_200_OK)
async def home():
    return ResponseModel(
        message=messages.MSG_200_OK
    )
