from typing import List

from app.api import crud
from app.api.models import PersonDB, PersonSchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=PersonDB, status_code=201)
async def create_person(payload: PersonSchema):
    person_id = await crud.post(payload)

    response_object = {
        "id": person_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.get("/{id}/", response_model=PersonDB)
async def read_person(id: int = Path(..., gt=0),):
    person = await crud.get(id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@router.get("/", response_model=List[PersonDB])
async def read_all_persons():
    return await crud.get_all()


@router.put("/{id}/", response_model=PersonDB)
async def update_person(payload: PersonSchema, id: int = Path(..., gt=0),):
    person = await crud.get(id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    person_id = await crud.put(id, payload)

    response_object = {
        "id": person_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object


@router.delete("/{id}/", response_model=PersonDB)
async def delete_person(id: int = Path(..., gt=0)):
    person = await crud.get(id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")

    await crud.delete(id)

    return person
