import os

description = """
Voxcontrol backend API. 🚀 This is common microservice collected all routes in one.
"""

db_user = os.getenv("DB_USER", "voxcontrol")
db_pass = os.getenv("DB_PASS", "voxcontrol")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5439")
db_name = os.getenv("DB_NAME", "voxcontrol")

db_url = f"postgres://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

TORTOISE_ORM = {
    "connections": {
        "default": db_url,
    },
    "apps": {
        "models": {
            "models": ["voxcontrol.models"],  # , "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "timezone": "UTC",
}


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
    "http://voxcontrol.site",
    "https://voxcontrol.local",
    "https://voxcontrol.site",
    "https://www.voxcontrol.site",
    "https://192.168.10.162",
    "https://192.168.56.1",
]