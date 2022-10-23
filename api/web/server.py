"""Main entry point for the app."""

import uvicorn

from api.web import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
