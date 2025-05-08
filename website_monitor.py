import requests
from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Website(Base):
    __tablename__ = "websites"
    url = Column(String, primary_key=True)
    is_active = Column(Boolean, default=True)

engine = create_engine("sqlite:///watch_bot.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_website(url: str):
    session = Session()
    website = Website(url=url)
    session.add(website)
    session.commit()
    return f"✅ Sitio {url} agregado para monitoreo."

def check_status():
    session = Session()
    websites = session.query(Website).all()
    return "\n".join([f"🌐 {w.url}: {'🟢 Activo' if w.is_active else '🔴 Inactivo'}" for w in websites])
