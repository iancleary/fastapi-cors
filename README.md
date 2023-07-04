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
| `ALLOW_ORIGINS` | ["http://localhost","http://localhost:3000"] | A list of origins that should be permitted to make cross-origin requests. E.g. ['https://example.org', 'https://www.example.org']. You can use ['*'] to allow any origin.  *These are the URLs clients can make requests from* |
| `ALLOWED_CREDENTIALS` | True | Indicate that cookies should be supported for cross-origin requests. Also, allow_origins cannot be set to ['*'] for credentials to be allowed, origins must be specified. |
| `ALLOWED_METHODS` | ["*"] | A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['*'] to allow all standard methods. You can use ['GET'] to reduce the list. |
| `ALLOWED_HEADERS` | ["Access-Control-Allow-Origin"] | A list of HTTP request headers that should be supported for cross-origin requests. You can use ['*'] to allow all headers. The Accept, Accept-Language, Content-Language and Content-Type headers are always allowed for [simple CORS requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) |

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