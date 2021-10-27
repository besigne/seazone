import sqlalchemy

address = 'mysql+pymysql://root:123@localhost:3306/seazone'
engine = sqlalchemy.create_engine(address)

query = f'INSERT INTO core_superstructure (name, cnpj) VALUES ( "TestBuilding", "37293103000105")'
engine.execute(query)

query = f'INSERT INTO core_superstructure (name, cnpj) VALUES ( "TestBuilding2", "22823215000145")'
engine.execute(query)

query = f'INSERT INTO core_schedule (checkIn, checkOut, type, superstructure_id) VALUES (' \
    f'"2021-12-25 06:30:00", "2021-12-31 11:30:00", "Rent", 1)'
engine.execute(query)

query = f'INSERT INTO core_schedule (checkIn, checkOut, type, superstructure_id) VALUES (' \
    f'"2021-11-11 06:30:00", "2021-11-11 11:30:00", "Cleaning", 2)'
engine.execute(query)

query = f'INSERT INTO core_schedule (checkIn, checkOut, type, superstructure_id) VALUES (' \
    f'"2021-11-25 06:30:00", "2021-11-25 11:30:00", "Cleaning", 1)'
engine.execute(query)

query = f'INSERT INTO core_schedule (checkIn, checkOut, type, superstructure_id) VALUES (' \
    f'"2021-11-03 13:30:00", "2021-11-03 15:30:00", "Maintenance", 1)'
engine.execute(query)

query = f'INSERT INTO core_schedule (checkIn, checkOut, type, superstructure_id) VALUES (' \
    f'"2021-11-04 13:30:00", "2021-11-03 15:30:00", "Maintenance", 2)'
engine.execute(query)

query = f'INSERT INTO core_host (name, CPF) VALUES ("Host 1", "33669303065")'
engine.execute(query)

query = f'INSERT INTO core_host (name, CPF) VALUES ("Host 2", "33725416001")'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (1, 1)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (1, 2)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (1, 3)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (1, 4)'
engine.execute(query)


query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (1, 5)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (2, 1)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (2, 2)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (2, 3)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (2, 4)'
engine.execute(query)

query = f'INSERT INTO core_host_schedule(host_id, schedule_id) VALUES (2, 5)'
engine.execute(query)