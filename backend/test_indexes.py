
from app.database.connection import db, check_database_connection
from app.database.indexes import create_database_indexes


def main():
    try:
        check_database_connection()

        create_database_indexes()

        print("\nCreated indexes:")

        for collection_name in [
            "users",
            "farms",
            "plots",
            "sensor_readings",
            "soil_records",
            "crop_history",
            "recommendations",
        ]:
            indexes = db[collection_name].index_information()

            print(f"\n{collection_name}:")

            for index_name in indexes:
                print(f"  - {index_name}")

        print("\nAll database index tests completed successfully.")

    finally:
        from app.database.connection import close_database_connection
        close_database_connection()


if __name__ == "__main__":
    main()
