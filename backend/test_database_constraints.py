
from uuid import uuid4
from pymongo.errors import DuplicateKeyError

from app.database.connection import db, check_database_connection


def main():
    owner_uid = f"test_{uuid4().hex}"
    farm_id = f"farm_{uuid4().hex}"

    try:
        check_database_connection()

        # Test 1: Create a farmer
        db.users.insert_one({
            "firebase_uid": owner_uid,
            "full_name": "Temporary Test Farmer"
        })
        print("PASS: Farmer account created")

        # Test 2: Only one farm per farmer
        db.farms.insert_one({
            "owner_uid": owner_uid,
            "name": "Test Farm"
        })

        try:
            db.farms.insert_one({
                "owner_uid": owner_uid,
                "name": "Second Test Farm"
            })
            raise AssertionError("A farmer was allowed to create two farms")
        except DuplicateKeyError:
            print("PASS: One farm per farmer enforced")

        # Test 3: Multiple plots in one farm
        db.plots.insert_one({
            "farm_id": farm_id,
            "name": "Plot A"
        })
        db.plots.insert_one({
            "farm_id": farm_id,
            "name": "Plot B"
        })
        print("PASS: Multiple plots per farm allowed")

        # Test 4: Duplicate plot names rejected
        try:
            db.plots.insert_one({
                "farm_id": farm_id,
                "name": "Plot A"
            })
            raise AssertionError("Duplicate plot name was allowed")
        except DuplicateKeyError:
            print("PASS: Duplicate plot names rejected")

        print("\nAll database constraint tests passed!")

    finally:
        # Remove temporary test records
        db.users.delete_many({"firebase_uid": owner_uid})
        db.farms.delete_many({"owner_uid": owner_uid})
        db.plots.delete_many({"farm_id": farm_id})

        from app.database.connection import close_database_connection
        close_database_connection()


if __name__ == "__main__":
    main()
