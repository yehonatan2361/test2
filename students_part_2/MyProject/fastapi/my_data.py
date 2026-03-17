import mysql.connector
import logging

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
    logger.info("no data base")





def select_all_attacks():
    mytabol = mydb.cursor()
    mytabol.execute("SELECT * FROM attacks")
    myresult = mytabol.fetchall()
    return myresult

def select_all_damage_assessments():
    mytabol = mydb.cursor()
    mytabol.execute("SELECT * FROM damage_assessments")
    myresult = mytabol.fetchall()
    return myresult


def select_all_targets():
    my_table = mydb.cursor()
    my_table.execute("SELECT * FROM targets")
    result = my_table.fetchall()
    return result


def select_all_intel_signals():
    mytabol = mydb.cursor()
    mytabol.execute("SELECT * FROM intel_signals")
    myresult = mytabol.fetchall()
    return myresult
