from fastapi import FastAPI
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler

app = FastAPI()

class CrawlRequest(BaseModel):
    url: str

@app.post("/crawl")
async def crawl_page(req: CrawlRequest):
    crawler = AsyncWebCrawler()
    result = await crawler.arun(url=req.url)

    return {
        "url": req.url,
        "markdown": result.markdown,
        "html": result.html,
        "text": result.text
    }
