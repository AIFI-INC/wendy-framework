from wendy import app


@app.get("/v1/addresses")
async def home():
    return {"message": "welcome"}
