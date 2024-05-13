import logging  # noqa
import os  # noqa
import platform  # noqa
import sys  # noqa

import uvicorn
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

if __name__ == "__main__":
    logging.info("Application Architecton RUN ")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=1,
        log_config=log_config,
        reload_dirs=["./"],
        reload_excludes=["../tests/"],
        log_level="info",
        access_log=True,
    )
