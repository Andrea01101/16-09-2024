from database.DB_connect import DBConnect
from model.neighbours import Neightbours
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct `datetime`  
                   from sighting s """

        cursor.execute(query)

        for row in cursor:
            result.append(row["datetime"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllShapes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct shape 
                   from sighting s 
                   where shape != "" """

        cursor.execute(query)

        for row in cursor:
            result.append(row['shape'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *  
                   from state s"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(s, y, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.state1 as s1, n.state2 as s2, count(*) as tot
                   from sighting s, neighbor n, state s3 
                   where s.shape = %s and year(s.`datetime`) = %s
                   and s.state = s3.id and (n.state1 = s3.id or n.state2=s3.id)
                   and n.state1<n.state2
                   group by n.state1, n.state2"""

        cursor.execute(query, (s, y))

        for row in cursor:
            result.append(Neightbours(idMap[row["s1"]],
                                      idMap[row["s2"]],
                                      row["tot"]
                                      ))  # nodo1,nodo2,peso


        cursor.close()
        conn.close()
        return result
