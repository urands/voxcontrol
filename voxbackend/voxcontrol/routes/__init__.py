from fastapi import APIRouter
from .structure import router as structure_router
from .recognition import router as recognition_router
router = APIRouter()


router.include_router(structure_router, prefix='/structure')
router.include_router(recognition_router, prefix='/recognition')


