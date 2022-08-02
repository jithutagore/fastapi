import mysql.connector as connector


class DbHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="Jithutagore@123",
            database="fastapi"
        )

        query = """create table if not exists user(userid int(10)primary key,
                               username varchar(50),age int)"""
        cur = self.con.cursor()
        cur.execute(query)

    def insert_data(self, user_id, username, age):
        query = """insert into user(userid,username,age)
        values({}, '{}', {})""".format(user_id, username, age)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_all(self):
        query = """select * from user"""
        cur = self.con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        final_lst = []
        for each in result:
            dictionary = {
                "user_id": each[0],
                "user_name": each[1],
                "age": each[2]
            }
            final_lst.append(dictionary)
        print(final_lst)
        return final_lst

    def fetch_by_name(self, name):
        query = f"""Select * from user where username = '{name}'"""
        cur = self.con.cursor()
        cur.execute(query)
        for user in cur:
            return user

    def delete_user(self, userid):
        query = """delete from user where userid ={}""".format(userid)

        c = self.con.cursor()
        c.execute(query)
        self.con.commit()

    def update_user(self, user_id, username, age):
        query = """update user set username='{}',age={}
        where userid={}""".format(username, age, user_id)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
