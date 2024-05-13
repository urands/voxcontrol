import json
import logging
from voxcontrol.models.structure import structure, Structure
from fastapi import APIRouter, Request

router = APIRouter(tags=["General route"])



@router.post("")
async def post_structure(request : Request):
    global structure
    body = await request.json()

    structure = await Structure.create(
        structure = body
    )

    return {
        "sessionId" : structure.id
    }