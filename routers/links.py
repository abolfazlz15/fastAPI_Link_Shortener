from fastapi import APIRouter, HTTPException, Query, Request
from starlette.responses import RedirectResponse

from database import collection_name
from schemas.link_schema import CreateLink, LinkDetail, LinkList
from utils.link_converter import create_short_link_record

router = APIRouter()



@router.get('/links/', response_model=LinkList)
async def get_links(skip: int = Query(0, alias="page", description="Page number", ge=0), 
                    limit: int = Query(10, le=100, description="Number of items per page")):
    '''
    fech all items form database
    '''
    links = collection_name.find().skip(skip).limit(limit)
    return LinkList(links=[LinkDetail(**link) for link in links])


@router.post('/link/create')
async def create_link(link_address: CreateLink, request: Request):

    short_link = create_short_link_record(link_address.link)
    return {'result': f'http://{request.client.host}:8000/{short_link}'}

