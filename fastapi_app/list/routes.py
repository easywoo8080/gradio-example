from fastapi import APIRouter
# from service import list_boards as list_boards_service

router = APIRouter(prefix="/api/list")

@router.get("/")
def board_list(name: str):
    print('Hello'+name)
    return {"message": f"Hello, {name}!"}
    return list_boards_service()
