
from pymongo import ASCENDING, DESCENDING

from app.database.connection import db


def create_database_indexes():
    """Create indexes for AgriSmart AI collections."""

    # User identity
    db.users.create_index(
        [("firebase_uid", ASCENDING)],
        unique=True,
        name="unique_firebase_uid"
    )

    # One farm per farmer account
    db.farms.create_index(
        [("owner_uid", ASCENDING)],
        unique=True,
        name="one_farm_per_user"
    )

    # Plot identification within a farm
    db.plots.create_index(
        [
            ("farm_id", ASCENDING),
            ("name", ASCENDING)
        ],
        unique=True,
        name="unique_plot_name_per_farm"
    )

    # Agricultural history and sensor data
    db.sensor_readings.create_index(
        [
            ("owner_uid", ASCENDING),
            ("plot_id", ASCENDING),
            ("timestamp", DESCENDING)
        ],
        name="sensor_history_lookup"
    )

    db.soil_records.create_index(
        [
            ("owner_uid", ASCENDING),
            ("plot_id", ASCENDING),
            ("created_at", DESCENDING)
        ],
        name="soil_history_lookup"
    )

    db.crop_history.create_index(
        [
            ("owner_uid", ASCENDING),
            ("plot_id", ASCENDING),
            ("season", DESCENDING)
        ],
        name="crop_history_lookup"
    )

    db.recommendations.create_index(
        [
            ("owner_uid", ASCENDING),
            ("plot_id", ASCENDING),
            ("created_at", DESCENDING)
        ],
        name="recommendation_history_lookup"
    )

    print("AgriSmart AI: Database indexes created successfully")
