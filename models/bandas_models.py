from core.config import settings
from sqlalchemy import Column, Integer, String, Float, Boolean

class BandasModel(settings.BDBaseModel):
    __tablename__ = 'bandas'
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    qtd_integrantes: int = Column(Integer())
    tipo_musical: str = Column(String(256))
