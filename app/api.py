from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import bool_router, int_router, float_router

with open("README.md", "r") as file:
    description = file.read()

API = FastAPI(
    title='FortranRNG API',
    description=description,
    version='0.0.4',
    docs_url='/',
)

API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

for router in (bool_router, int_router, float_router):
    API.include_router(router.Router)
