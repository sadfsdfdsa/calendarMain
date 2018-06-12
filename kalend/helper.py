from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
engine = create_engine('sqlite:///:memory:', echo=True)


"INSERT INTO data VALUES ("+data.day+", '"+data.month+", "+data.year+", '"+data.add+"')"