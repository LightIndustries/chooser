from typing import List, Union
from fastapi import APIRouter, Request, Body
from utils.utils import choose_list_element

router = APIRouter(prefix="/choice",
                   tags=["Choices"])

@router.get("/")
async def choice_from_values(vals: List[Union[str, int, float]]):
    choice = choose_list_element(vals)
    return {"vals":choice}