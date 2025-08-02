# from fastapi import Depends
# from sqlalchemy.ext.asyncio import AsyncSession

# from database import LinkRepository, get_new_async_session
# from schemas import LinkCreate

# class LinkDep:

#     def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
#         self.link_repo = LinkRepository(
#             session=session
#         )

#     async def add_link(
#         self,
#         link: LinkCreate
#     ):
        

        