# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.schemas import ArtistCreate
from app.models import Artist


async def create_artist(db: AsyncSession, data: ArtistCreate):
    artist_data = data.dict()

    # Convert HttpUrl fields to str
    if "profile_image_url" in artist_data:
        artist_data["profile_image_url"] = str(artist_data["profile_image_url"])
    if "audio_preview_url" in artist_data:
        artist_data["audio_preview_url"] = str(artist_data["audio_preview_url"])

    new_artist = Artist(**artist_data)
    db.add(new_artist)
    await db.commit()
    await db.refresh(new_artist)
    return new_artist   # ✅ fixed this


async def get_artists(db: AsyncSession):
    result = await db.execute(select(Artist))
    return result.scalars().all()
