import uvicorn
from fastapi import FastAPI
import my_data
import logging

logging.basicConfig(
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s [%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)


app = FastAPI()

s = my_data.connection_data_base()
if s == -1:
    logger.info(11111111111111111)


@app.get("/")
async def root():
    return {"message":"hello user"}

@app.get("/select_all_damage_assessments")
async def select_all_damage_assessments():
    return my_data.select_all_damage_assessments()

@app.get("/select_all_attacks")
async def select_all_attacks():
    return my_data.select_all_attacks()

@app.get("/select_all_targets")
async def select_all_targets():
    return my_data.select_all_targets()

@app.get("/select_all_intel_signals")
async def select_all_intel_signals():
    return my_data.select_all_intel_signals()











if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
