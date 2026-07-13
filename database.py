from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base
data = "mysql+pymysql://root:%40Phamquocanh15072007@localhost/class_section_db"

engine = create_engine(data)

localsesson = sessionmaker(
    bind= engine,
    autoflush= False,
    expire_on_commit= False
)

Base = declarative_base()

def get_db() :
    db = localsesson()
    try :
        yield db
    finally :
        db.close()


