from sshtunnel import SHHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

with SSHTunnelForwarder(
	('hdslab.hcde.washington.edu', 22),
	ssh_username="espen1",
	ssh_password="sushi650",
	remote_bind_address=('127.0.0.1', 3306)
	) as server:
	
	local_port = str(server.local_bind_port)
	engine = create_engine('mysql://fanfictiondrg:fanfictiondrg2016@HCDE127.0.0.1:'
		+ local_port + '/fanfictiondrg201701')
	Session = sessionmaker(bind=engine)
	session = Session()

	result = session.execute("SELECT * FROM story limit 100")
	for row in result:
		print(row[0])

	session.close()