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

This is an opinionated way to start FastAPI:

- No ReDoc.
- Swagger is hosted at the `root_path`.
- Swagger UI oAuth2 redirect URL is `/oauth2-redirect`.
- Endpoint `/ping` responds with the plain text response "pong".
- Mounts static directory at `/static` (default).
- Title and site name in Swagger
- Assets (expects these files in the directory `./static/assets`):
  - Favicon - `favicon.ico`.
  - Swagger CSS - `swagger-ui.min.css`.
  - Swagger Bundle JS - `swagger-ui-bundle.min.js`.

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