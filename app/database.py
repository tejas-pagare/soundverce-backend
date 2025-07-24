# database.py

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import ssl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get your Neon PostgreSQL URL from the .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing ")
# SSL context required for Neon
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create async engine for Neon with SSL
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    connect_args={"ssl": ssl_context},
    pool_recycle=1800,
)

# async_sessionmaker
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

async def get_db():
    async with async_session() as session:
        yield session



# Base class for your models
Base = declarative_base()
