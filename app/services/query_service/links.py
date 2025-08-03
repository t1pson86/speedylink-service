from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete


from database import LinksModel
from schemas import LinkCreate



class LinksRequests:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_link(
        self,
        link: LinkCreate,
        user_id: int
    ):

        new_link = LinksModel(
            long_url=str(link.long_url),
            short_url='7777777777',
            user_id=user_id
        )

        self.session.add(new_link)
        await self.session.commit()

        html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI HTML</title>
        </head>
        <body>
            <h1>Hello from FastAPI!</h1>
        </body>
    </html>
        """
        return HTMLResponse(content=html_content, status_code=200)