from fastapi import APIRouter, Request, Form
from models.note import Note
from config.db import conn
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas.note import noteEntity, notesEntity
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({}).sort("_id", -1)
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    conn.notes.notes.insert_one(dict(formDict))
    return RedirectResponse(url="/", status_code=303)

@note.post("/delete")
async def delete_note(request: Request):
    form = await request.form()
    note_id = form.get("id")
    if note_id:
        conn.notes.notes.delete_one({"_id": ObjectId(note_id)})
    return RedirectResponse(url="/", status_code=303)