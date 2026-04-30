
from fastapi import FastAPI, UploadFile, File
from agents.orchestrator import run_pipeline
from utils.parser import parse_document
import tempfile

app = FastAPI(title="Compliance Sentinel")

@app.post("/audit")
async def audit_document(file: UploadFile = File(...)):
    suffix = file.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(await file.read())
        path = tmp.name

    text = parse_document(path)

    result = run_pipeline(text)

    return {
        "filename": file.filename,
        "result": result
    }
