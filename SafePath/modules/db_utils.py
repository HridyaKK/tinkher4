from config.db_config import get_connection


def fetch_high_risk_zones():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT latitude, longitude FROM high_risk_zones"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results