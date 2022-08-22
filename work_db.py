import psycopg2

class DB:
        def __init__(self, database, user, password):
                self.database = database
                self.user = user
                self.password = password
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)

        def create_db(self):
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        # cur.execute("""
                        #         DROP TABLE information;
                        #         DROP TABLE client
                        #         """)

                        cur.execute("""
                                CREATE TABLE IF NOT EXISTS client(
                                        client_id SERIAL PRIMARY KEY,
                                        first_name VARCHAR(40) NOT NULL,
                                        last_name VARCHAR(40) NOT NULL,
                                        email TEXT NOT NULL
                                );
                                """)

                        cur.execute("""
                                CREATE TABLE IF NOT EXISTS information(
                                        inf_id SERIAL PRIMARY KEY,
                                        phone_number TEXT UNIQUE,
                                        client_id INTEGER NOT NULL REFERENCES client(client_id)
                                );
                                """)

                        conn.commit()
                conn.close()

        def cli_id(self):
                first_name = str(input('Введите Имя: '))
                last_name = str(input('Введите Фамилию: '))
                email = str(input('Введите email: '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("SELECT client_id FROM client WHERE first_name = %s and last_name = %s and email = %s;", (first_name, last_name, email))
                        return cur.fetchone()[0]

        def new_client(self):
                first_name = str(input('Введите Имя: '))
                last_name = str(input('Введите Фамилию: '))
                email = str(input('Введите email: '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("INSERT INTO client(first_name, last_name, email) VALUES(%s, %s, %s)", (first_name, last_name, email))
                        conn.commit()
                conn.close()

        def inf_client(self):
                print('Введите данные пользователя которому хотите дать номер телефона\/')
                id_client = self.cli_id()
                phone_number = str(input('Введите номер(а) телофна(ов)(8..., +7...)) или введите "NULL"(чтобы не давать номер телефона): '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("INSERT INTO information(phone_number, client_id) VALUES(%s, %s)", (phone_number, id_client))
                        conn.commit()
                conn.close()

        def change_data(self):
                print('Введите данные пользователя которого хотите поменять\/')
                id_client = self.cli_id()
                print('Введите данные пользователя которые хотите сохранить\/')
                first_name = str(input('Введите Имя: '))
                last_name = str(input('Введите Фамилию: '))
                email = str(input('Введите email: '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("UPDATE client SET first_name = %s, last_name = %s, email = %s WHERE client_id = %s;", (first_name, last_name, email, id_client))
                        conn.commit()
                conn.close()

        def change_number(self):
                print('Введите данные пользователя у которого хотите поменять номер телефона\/')
                id_client = self.cli_id()
                print('Введите номер телефона который хотите сохранить\/')
                phone_number = str(input('Введите номер(а) телофна(ов)(8..., +7...)) или введите "NULL"(чтобы не давать номер телефона): '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("UPDATE information SET phone_number = %s WHERE client_id = %s;", (phone_number, id_client))
                        conn.commit()
                conn.close()

        def delete_phone(self):
                print('Введите данные пользователя у которого хотите удалить номер телефона\/')
                id_client = self.cli_id()
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("DELETE FROM information WHERE client_id = %s;", (id_client,))
                        conn.commit()
                conn.close()

        def delete_client(self):
                print('Введите данные пользователя которого хотите удалить\/')
                id_client = self.cli_id()
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        cur.execute("DELETE FROM information WHERE client_id = %s;", (id_client,))
                        cur.execute("DELETE FROM client WHERE client_id = %s;", (id_client,))
                        conn.commit()
                conn.close()

        def find_сlient(self):
                print('По каким критериям хотите найти клиента введите цифру\/')
                command = int(input('(1)По имени\n(2)По фамилии\n(3)По email\n(4)По номеру телефона\nВведите номер команды: '))
                conn = psycopg2.connect(database = self.database, user = self.user, password = self.password)
                with conn.cursor() as cur:
                        if command == 1:
                                first_name = str(input('Введите Имя: '))
                                cur.execute("SELECT first_name, last_name, email FROM client WHERE first_name = %s;", (first_name,))
                                print(cur.fetchall())
                        elif command == 2:
                                last_name = str(input('Введите Фамилию: '))
                                cur.execute("SELECT first_name, last_name, email FROM client WHERE last_name = %s;", (last_name,))
                                print(cur.fetchall())
                        elif command == 3:
                                email = str(input('Введите email: '))
                                cur.execute("SELECT first_name, last_name, email FROM client WHERE email = %s;", (email,))
                                print(cur.fetchall())
                        elif command == 4:
                                phone_number = str(input('Введите номер(а) телофна(ов)(8..., +7...)): '))
                                cur.execute("SELECT client_id FROM information WHERE phone_number = %s;", (phone_number,))
                                client_id = cur.fetchone()
                                cur.execute("SELECT first_name, last_name, email FROM client WHERE client_id = %s;", (client_id,))
                                print(cur.fetchall())
                        else:
                                print('Ошибка')
