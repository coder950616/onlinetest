# Description

A image compression system based on FastAPI which supports compressing images and checking history.

## Features

* Compress images uploaded by customers with different proportions.
* Check the history of compressed images.
* Support multiple users.

# How to Run

## Environment Requirements

* Python 3.8.5+
* FastAPI
* PIL

## Setup
1. Clone the project
2. Create Virtual Enviroment(Recommended but not mandatory)

```
# 1. install virtual environment 
python -m venv venv
# 2. activate virtual environment
source venv/bin/activate
# 3. installl necessary python libraries
pip install fastapi pillow
```

3. Start the service
By running this command, the service will at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```
uvicorn main:app --reload
```

# How to Test
### Compress Image
1. Open the service in browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Click **Try it out** on /compress_image
3. Check **choose file** to upload image
4. Input **proportion**, default value is 50.
5. Click **Execuate**, then you can get compressed image

### Check History
1. Open the service in browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Click **Try it out** on /check_history
3. Click **Execuate**, then you can get history of compressed images
