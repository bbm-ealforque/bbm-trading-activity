
from app.dto.PaginatorDTO import PaginatorDTO
from masoniteorm.query import QueryBuilder
from masoniteorm.query.QueryBuilder import LengthAwarePaginator


class PaginatorService:
   
  def __init__(self):
    pass

  def paginate(self, builder: QueryBuilder, dto: PaginatorDTO):
    return builder.paginate(dto.getPerPage(), dto.getPage())
