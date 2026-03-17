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



@app.get("/")
async def root():
    return {"message":"hello user"}

@app.get("/show_all_table")
async def show_all_table():
    data = my_data.show_all_table()
    logger.info(data)
    return data

@app.get("/select_all_damage_assessments")
async def select_all_damage_assessments():
    data = my_data.select_all_damage_assessments()
    # logger.info(data)
    return data

@app.get("/show_all_damage_assessments")
async def show_all_damage_assessments():
    data = my_data.show_all_damage_assessments()
    logger.info(data)
    return data

@app.get("/select_all_attacks")
async def select_all_attacks():
    data = my_data.select_all_attacks()
    # logger.info(data)
    return data

@app.get("/show_all_attacks")
async def show_all_attacks():
    data = my_data.show_all_attacks()
    # logger.info(data)
    return data


@app.get("/select_all_targets")
async def select_all_targets():
    data = my_data.select_all_targets()
    # logger.info(data)
    return data

@app.get("/show_all_targets")
async def show_all_targets():
    data = my_data.show_all_targets()
    # logger.info(data)
    return data


@app.get("/select_all_intel_signals")
async def select_all_intel_signals():
    data = my_data.select_all_intel_signals()
    # logger.info(data)
    return data

@app.get("/show_all_intel_signals")
async def show_all_intel_signals():
    data = my_data.show_all_intel_signals()
    # logger.info(data)
    return data



@app.get("/select_1")
async def select_1():
    data = my_data.select_1()
    # logger.info(data)
    return data



@app.get("/select_2")
async def select_2():
    data = my_data.select_2()
    # logger.info(data)
    return data

@app.get("/select_3")
async def select_3():
    data = my_data.select_3()
    # logger.info(data)
    return data

@app.get("/select_4")
async def select_4():
    data = my_data.select_4()
    logger.info(data)
    return data


@app.get("/select_5")
async def select_5():
    list_all_coordinates_and_entity_id = []
    list_coordinates_and_entity_id = []
    list_entity_id = my_data.return_list_entity_id()
    for entity_id in list_entity_id:
        coordinates = my_data.select_5(entity_id)
        list_coordinates_and_entity_id.append(coordinates)
        list_coordinates_and_entity_id.append(entity_id)
        list_all_coordinates_and_entity_id.append(list_coordinates_and_entity_id)
    return list_all_coordinates_and_entity_id





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
