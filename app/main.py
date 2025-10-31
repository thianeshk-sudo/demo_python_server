from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Demo Python Server")


class NoteCreate(BaseModel):
    """Payload for creating a note."""

    content: str


class Note(NoteCreate):
    """Note representation returned to clients."""

    id: int


_notes: List[Note] = []
_next_id: int = 1


@app.get("/")
async def read_root():
    """Return a simple welcome message."""
    return {"message": "Welcome to the Demo Python Server!"}


@app.get("/health")
async def health_check():
    """Basic health-check endpoint."""
    return {"status": "ok"}


@app.get("/notes", response_model=List[Note])
async def list_notes():
    """Return all saved notes."""

    return _notes


@app.post("/notes", response_model=Note, status_code=201)
async def create_note(payload: NoteCreate):
    """Create a new note and return it."""

    global _next_id
    note = Note(id=_next_id, content=payload.content)
    _next_id += 1
    _notes.append(note)
    return note


@app.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: int):
    """Delete a note by its ID."""

    for index, note in enumerate(_notes):
        if note.id == note_id:
            _notes.pop(index)
            return
    raise HTTPException(status_code=404, detail="Note not found")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
