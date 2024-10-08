class pgQueries:
    def __init__(self):
        self.select_blacklist = """ SELECT                                     
                                        CASE 
                                            WHEN preferred_email = true THEN personal_email 
                                            ELSE cuny_email 
                                        END AS email
                                    FROM people
                                    WHERE uid NOT IN (SELECT uid FROM blacklist)
                                """
        self.select_cabinet = """ SELECT 
                                    CASE 
                                        WHEN preferred_email = true THEN personal_email 
                                        ELSE cuny_email 
                                    END AS email
                                FROM people
                                WHERE uid IN (SELECT uid FROM cabinet);
                                """
        self.select_all_no_blacklist = """ SELECT 
                                            CASE 
                                                WHEN preferred_email = true THEN personal_email 
                                                ELSE cuny_email 
                                            END AS email
                                            FROM people 
                                           WHERE uid NOT IN (SELECT uid from blacklist) """
        self.select_all = """ SELECT                                     
                                CASE 
                                    WHEN preferred_email = true THEN personal_email 
                                    ELSE cuny_email 
                                END AS email
                             FROM people """

        self.select_people = """ SELECT * FROM PEOPLE WHERE LOWER(first_name) IN ({}) """
        self.select_active = """ SELECT                                     
                                    CASE 
                                        WHEN preferred_email = true THEN personal_email 
                                        ELSE cuny_email 
                                    END AS email
                                FROM people where active = true """

        self.remove_cabinet = """DELETE FROM cabinet WHERE uid in (%s)"""
        self.delete_person = """ DELETE FROM people WHERE uid in (%s) """

        self.mark_inactive = """ UPDATE people SET active = false WHERE uid in (%s) """
        self.mark_active = """ UPDATE people SET active = true WHERE uid in (%s) """
        self.mark_all_inactive = """ UPDATE people SET active = false WHERE uid not in (SELECT uid from cabinet); """

        self.add_blacklist = """ INSERT INTO blacklist (uid) VALUES (%s) """
        self.add_cabinet = """ INSERT INTO cabinet (uid) VALUES (%s) """
        self.add_person = """ INSERT INTO people (first_name, middle_name, last_name, 
                                personal_email, cuny_email, preferred_email,active, discord, emplid)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING uid"""
