from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
from threading import Lock
from collections import deque
import io

app = FastAPI()
lock = Lock()
history_dict = {}
history_list = deque()
max_len = 3


@app.post("/compress_image")
async def compress_image(file: UploadFile = File(...), proportion: int = 50):
    file_flag = file.filename + str(proportion)
    with lock:
        if file_flag in history_dict:
            if len(history_list) >= max_len:
                history_list.popleft()
            history_list.append(file_flag)
            return StreamingResponse(io.BytesIO(history_dict[file_flag]["compressed_image"]), media_type="image/jpeg")
    
    if not file.content_type.startswith("image/"):
        return {"error": "File must be an image"}
    if proportion > 100 or proportion <= 0:
        return {"error": "Proportion should between 1 and 100"}
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=proportion)
        output.seek(0)
        output_bytes = output.getvalue()
        result = {
            "filename": file.filename,
            "proportion": proportion,
            "compressed_image": output_bytes,
        }
        with lock:
            if len(history_list) >= max_len:
                first_image = history_list[0]
                if first_image not in history_list:
                    del history_dict[first_image]
                history_list.popleft()
            
            history_list.append(file_flag)
            history_dict[file_flag] = result

        return StreamingResponse(output, media_type="image/jpeg")
    except Exception as e:
        return {"error": str(e)}


@app.get("/history")
def get_history():
    result = []
    for item in history_list:
        tmp = dict()
        tmp['filename'] = history_dict[item]['filename']
        tmp['proportion'] = history_dict[item]['proportion']
        result.append(tmp)
    return result