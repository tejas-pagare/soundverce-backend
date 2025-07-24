from sqlalchemy import Column, Integer, String, Boolean, Enum, TIMESTAMP,Numeric
from database import Base 
import enum as py_enum
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID, ARRAY 




# Main SQLAlchemy model
class Artist(Base):
    __tablename__ = "form_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    profile_image_url = Column(String, nullable=True)
    tags = Column(ARRAY(String), nullable=True)  
    price = Column(Numeric, nullable=True)
    dna_visibility = Column(Enum("public", "private", "draft", name="visibility_enum"), default="public")
    tracks_visibility = Column(Enum("visible", "invisible", name="tracks_enum"), default="visible")
    become_partner = Column(Boolean, default=True)
    license_type = Column(String, nullable=True)
    audio_preview_url = Column(String, nullable=True)
    sensitivity = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
