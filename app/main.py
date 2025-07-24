from fastapi import FastAPI, Depends
from app.database import get_db
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import  AsyncSession


from app.schemas import  Artist,ArtistCreate
from app.crud import create_artist,get_artists

app = FastAPI()

# Optional: Allow CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


        

# Route to submit form data
@app.post("/artists", response_model=Artist)
async def submit_orm(data: ArtistCreate, db: AsyncSession = Depends(get_db)):
    return await create_artist(db=db, data=data)
    

# Route to get all artist form entries
@app.get("/all-artists", response_model=list[Artist])
async def get_all_artists(db: AsyncSession = Depends(get_db)):
    return await get_artists(db=db)


@app.get("/")
async def get_all_artists():
    return {"Message":"Server Started"}

