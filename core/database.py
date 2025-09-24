# arquivo de banco de dados

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.config import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncEngine = sessionmaker(
    autocommit = False, # evita quecommite coisa não permitidas, como erros
    autoflush = False,
    expire_on_commit = False, # so vai expirar como fechar o banco
    class_ = AsyncSession,
    bind = engine
)