# fastapi-cors

A simply scoped abstraction to provide CORS settings via environment variables to a Fastapi application.

## Usage

```python
from fastapi import FastAPI

# import (fastapi_cors.env) will read environment variables from .env
from fastapi_cors import CORS 

app = FastAPI()

CORS(app)
```

## Opinions

A health check route is optionally added that displays these (but not other) environment variables.


*If you want to disable it, use the code below*

```python
from fastapi_cors import CORS 

app = FastAPI()

CORS(app, include_health_check=False)
```

## Config

Configure FastAPI as usual. Extra arguments (that can be accessed from `app.extra`):

| Name | Default | Description |
| --- | --- | --- |
| `HOST` | 0.0.0.0 | Displayed in the Swagger title, with `app.title`. |
| `PORT` | 8000 | Where to mount the static directory. Disabled if value is falsy. |
| `LOG_LEVEL` | info | log level. |
| `ALLOW_ORIGINS` | ["http://localhost","http://localhost:3000"] | Client URLs that are allowed to make requests |
| `ALLOWED_CREDENTIALS` | True |  |
| `ALLOWED_METHODS` | ["*"] | List of HTTP methods to allow |
| `ALLOWED_HEADERS` | ["Access-Control-Allow-Origin"] | List of headers to allow |

> See the [FastAPI documentation on CORS](https://fastapi.tiangolo.com/tutorial/cors/?h=cors) for more information

### Example Env

```env
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=info
ALLOW_ORIGINS=http://localhost,http://localhost:3000
ALLOWED_CREDENTIALS=True
ALLOWED_METHODS=["*"]
ALLOWED_HEADERS

```

*Note, this is not required unless you are changing a default or want to declare them all*