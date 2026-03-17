import mysql.connector
import logging
import json
from maps_data.DigitalHunter_map import plot_map_with_geometry

logging.basicConfig(
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s [%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)


def connection_data_base():
    try:
        mydb = mysql.connector.connect(
            host = "mysql",
            user = "root",
            password = "root",
            database = "digital_hunter"
        )
        return mydb
    except Exception as e:
        logger.info(e)
        return -1

mydb = connection_data_base()
if mydb == -1:
    logger.info("I'm sorry but there is no data base")
    Exception("I'm sorry but there is no data base")





def show_all_table():
    my_table = mydb.cursor()
    my_table.execute("SHOW TABLES;")
    result = my_table.fetchall()
    return result


def select_all_attacks():
    my_table = mydb.cursor()
    my_table.execute("SELECT * FROM attacks;")
    result = my_table.fetchall()
    return result

def show_all_attacks():
    my_table = mydb.cursor()
    my_table.execute("SHOW COLUMNS FROM attacks;")
    result = my_table.fetchall()
    return result



def select_all_damage_assessments():
    my_table = mydb.cursor()
    my_table.execute("SELECT * FROM damage_assessments;")
    result = my_table.fetchall()
    return result

def show_all_damage_assessments():
    my_table = mydb.cursor()
    my_table.execute("SHOW COLUMNS FROM damage_assessments;")
    result = my_table.fetchall()
    return result




def select_all_targets():
    my_table = mydb.cursor()
    my_table.execute("SELECT * FROM targets;")
    result = my_table.fetchall()
    return result

def show_all_targets():
    my_table = mydb.cursor()
    my_table.execute("SHOW COLUMNS FROM targets;")
    result = my_table.fetchall()
    return result




def select_all_intel_signals():
    my_table = mydb.cursor()
    my_table.execute("SELECT * FROM intel_signals;")
    result = my_table.fetchall()
    return result

def show_all_intel_signals():
    my_table = mydb.cursor()
    my_table.execute("SHOW COLUMNS FROM intel_signals;")
    result = my_table.fetchall()
    return result



def select_1():
    my_table = mydb.cursor()
    my_table.execute("SELECT entity_id, target_name, priority_level FROM targets WHERE priority_level IN (1,2)\
     AND movement_distance_km > 5;")
    result = my_table.fetchall()
    return result


def select_2():
    my_table = mydb.cursor()
    my_table.execute("SELECT signal_type, COUNT(*) AS count FROM intel_signals\
     GROUP BY signal_type ORDER BY count DESC;")
    result = my_table.fetchall()
    return result


def select_3():
    my_table = mydb.cursor()
    my_table.execute("SELECT entity_id, COUNT(*) AS count FROM intel_signals\
     WHERE priority_level = 99 GROUP BY entity_id ORDER BY count DESC LIMIT 3;")
    result = my_table.fetchall()
    return result


def select_4():
    my_table = mydb.cursor()
    my_table.execute("SELECT entity_id\
     FROM intel_signals GROUP BY entity_id\
      HAVING MAX(CASE WHEN HOUR(timestamp) BETWEEN 8 AND 19 THEN distance_from_last ELSE 0 END)=0\
       AND MAX(CASE WHEN HOUR(timestamp) < 8 or HOUR(timestamp) >=20 THEN distance_from_last ELSE 0 END)>10;")
    result = my_table.fetchall()
    return result


def return_list_entity_id():
    my_table = mydb.cursor()
    my_table.execute("SELECT entity_id FROM\
         intel_signals ORDER BY entity_id;")
    result = my_table.fetchall()
    return result

def select_5(entity_id):
    my_table = mydb.cursor()
    my_table.execute("SELECT entity_id, reported_lat, reported_lon FROM\
     intel_signals ORDER BY entity_id;")
    result = my_table.fetchall()
    list_coordinates_entity_id = []
    try:
        for index in range(len(result)):
            coordinates_and_entity_id_in_result = result[index]
            entity_id_in_result = coordinates_and_entity_id_in_result[0]
            if entity_id_in_result == entity_id:
                coordinates = (coordinates_and_entity_id_in_result[1],coordinates_and_entity_id_in_result[2])
                logger.info(coordinates)
                list_coordinates_entity_id.append(coordinates)
        logger.info(list_coordinates_entity_id)
        plot_map_with_geometry(list_coordinates_entity_id)
    except Exception as e:
        logger.info(e)
    return list_coordinates_entity_id




