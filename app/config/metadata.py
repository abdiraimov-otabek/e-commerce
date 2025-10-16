"""This file contains Custom Metadata for your API Project.

Be aware, this will be re-generated any time you run the
'api-admin custom metadata' command!
"""

from app.config.helpers import MetadataBase

custom_metadata = MetadataBase(
    title="E-Commerce (IQ Tech)",
    name="E-Commerce",
    description="Full e-commerce API using FastAPI. By IQ Tech.",
    repository="https://github.com/abdiraimov-otabek/e-commerce.git",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    contact={
        "name": "IQ Tech",
        "url": "https://iq-tech.uz",
    },
    email="otabekabdiraimovv@gmail.com",
    year="2025",
)
