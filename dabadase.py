from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class IpEvent(Base):
    __tablename__ = 'ip_events'

    id = Column(Integer, primary_key=True)
    ip_address = Column(String(15))
    event_type = Column(Enum('Failure', 'Recovery'))
    date_ = Column(String(50))  # Changement de nom de colonne
    recovery_time = Column(Integer, nullable=True)

engine = create_engine('mssql+pyodbc://MSI:x0we80/gh@DESKTOP-6D9B7GC\\SQLEXPRESS/IpWatchman?driver=ODBC Driver 17 for SQL Server')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_ip_event(ip_address: str, event_type: str, date_: str, recovery_time: int = None) -> IpEvent:
    ip_event = IpEvent(ip_address=ip_address, event_type=event_type, date_=date_, recovery_time=recovery_time)
    session.add(ip_event)
    session.commit()
    print(f"Event added: {event_type} for IP {ip_address} at {ip_event.date_}")
    if recovery_time:
        print(f"Recovery time: {recovery_time} seconds")
    return ip_event

if __name__ == "__main__":
    # Exemple d'utilisation : insérer un événement IP avec un timestamp en tant que chaîne de caractères
    add_ip_event(ip_address="192.1.9.9.9", event_type="Failure", date_="2024-07-11 10:00:00")
