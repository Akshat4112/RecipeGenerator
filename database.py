import logging

from db import get_connection

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    with get_connection() as conn:
        logger.info("Database initialized successfully.")
        cursor = conn.execute("SELECT COUNT(*) FROM history")
        count = cursor.fetchone()[0]
        logger.info("History table has %d rows.", count)
