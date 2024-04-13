from db_connect import db

class Admin:
    #manage room booking

    #display all classes
    @staticmethod
    def displayAllClasses():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = 'SELECT * FROM grouptraining'
            cur.execute(query)
            classes = cur.fetchall()
            if classes:
                for i in classes:
                    print(i)
        except:
            print("Error fetching data")


    #monitor fitness equipment maintenance
    @staticmethod
    def displayAllEquipment():
        try:
            conn = db.get_conn()
            cur = conn.cursor()
            query = 'SELECT * FROM equipment'
            cur.execute(query)
            equipment = cur.fetchall()
            if equipment:
                for i in equipment:
                    print(i)
        except:
            print("Error fetching data")