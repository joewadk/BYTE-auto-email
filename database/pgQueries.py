class pgQueries:
    def __init__(self):
        self.select_blacklist = """SELECT *
                                FROM people
                                WHERE uid NOT IN (SELECT uid FROM blacklist);
                                """
        self.select_cabinet = """SELECT *
                                FROM people
                                WHERE uid IN (SELECT uid FROM cabinet);
                                """
        self.select_all = """ SELECT * FROM PEOPLE """
        self.add_cabinet = """ INSERT INTO cabinet (uid) VALUES (%s) """
        self.add_blacklist = """ INSERT INTO blacklist (uid) VALUES (%s) """
        self.delete_person = """ DELETE FROM people WHERE uid = (%s) """
