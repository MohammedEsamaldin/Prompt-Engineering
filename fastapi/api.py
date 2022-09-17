from fastapi import FastAPI
app = FastAPI()

@app.get('/bnewscore ')
def bnewscore():
    return{'Home':'Hello world'}

@app.get('/jdentities ')
def jdentities():
    return{'Home':'Hello world'}