from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import bool_router, int_router, float_router, index_router

with open("README.md", "r") as file:
    description = file.read()

API = FastAPI(
    title='FortranRNG API',
    description=description,
    version='1.0.2',
    docs_url='/',
)

API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

for router in (bool_router, int_router, float_router, index_router):
    API.include_router(router.Router)
