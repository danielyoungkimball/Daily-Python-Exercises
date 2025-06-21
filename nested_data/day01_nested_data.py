"""
🧩 Exercise 1: Normalize Nested User Records

Given a list of patient records from an API, each with nested fields for name
and appointment history,
write a function that flattens each record into a simpler format.

Each input patient looks like:
{
    "id": 1,
    "name": {"first": "Alice", "last": "Wong"},
    "appointments": [
        {"date": "2024-03-01", "status": "completed"},
        {"date": "2024-05-10", "status": "cancelled"},
    ]
}

✅ Your function should return:
[
    {'id': 1, 'name': 'Alice Wong', 'num_appointments': 2},
    ...
]

Function name: flatten_patients(patients)
"""


def flatten_patients(patients):
    flattened = []
    for p in patients:
        full_name = f"{p['name']['first']} {p['name']['last']}"
        count = len(p["appointments"])
        flattened.append({"id": p["id"], "name": full_name, "num_appointments": count})
    return flattened


def test_flatten_patients():
    print("Testing Flatten Patients:")
    patients = [
        {
            "id": 1,
            "name": {"first": "Alice", "last": "Wong"},
            "appointments": [
                {"date": "2024-03-01", "status": "completed"},
                {"date": "2024-05-10", "status": "cancelled"},
            ],
        },
        {
            "id": 2,
            "name": {"first": "Bob", "last": "Stevens"},
            "appointments": [
                {"date": "2024-03-07", "status": "completed"},
                {"date": "2024-05-20", "status": "cancelled"},
                {"date": "2024-05-21", "status": "cancelled"},
            ],
        },
        {
            "id": 3,
            "name": {"first": "Charlie", "last": "Garner"},
            "appointments": [
                {"date": "2024-03-14", "status": "completed"},
                {"date": "2024-03-21", "status": "completed"},
                {"date": "2024-05-30", "status": "cancelled"},
            ],
        },
    ]

    result = flatten_patients(patients)
    print(result)
    assert result == [
        {"id": 1, "name": "Alice Wong", "num_appointments": 2},
        {"id": 2, "name": "Bob Stevens", "num_appointments": 3},
        {"id": 3, "name": "Charlie Garner", "num_appointments": 3},
    ]


# 🧩 Exercise 2: Sort Patients by Number of Appointments
# -----------------------------------------------------
# Given the flattened list of patients from Exercise 1,
# write a function that returns the list sorted in descending order
# based on the number of appointments.

# Input:
# [
#     {'id': 1, 'name': 'Alice Wong', 'num_appointments': 2},
#     {'id': 2, 'name': 'Bob Smith', 'num_appointments': 4},
#     ...
# ]

# Output:
# [
#     {'id': 2, 'name': 'Bob Smith', 'num_appointments': 4},
#     {'id': 1, 'name': 'Alice Wong', 'num_appointments': 2},
#     ...
# ]

# Function name: sort_patients_by_appointments(patients)


def sort_patients_by_appointments(patients):
    flattened_patients = flatten_patients(patients)
    return sorted(flattened_patients, key=lambda p: p["num_appointments"], reverse=True)


def test_sort_patients_by_appointments():
    print("Testing Sort Patients By Appointments:")
    patients = [
        {
            "id": 1,
            "name": {"first": "Alice", "last": "Wong"},
            "appointments": [
                {"date": "2024-03-01", "status": "completed"},
                {"date": "2024-05-10", "status": "cancelled"},
            ],
        },
        {
            "id": 2,
            "name": {"first": "Bob", "last": "Stevens"},
            "appointments": [
                {"date": "2024-03-07", "status": "completed"},
                {"date": "2024-05-20", "status": "cancelled"},
                {"date": "2024-05-21", "status": "cancelled"},
            ],
        },
        {
            "id": 3,
            "name": {"first": "Charlie", "last": "Garner"},
            "appointments": [
                {"date": "2024-03-14", "status": "completed"},
                {"date": "2024-03-21", "status": "completed"},
                {"date": "2024-05-30", "status": "cancelled"},
            ],
        },
    ]

    sorted_patients = sort_patients_by_appointments(patients)
    print(sorted_patients)

    assert sorted_patients == [
        {"id": 2, "name": "Bob Stevens", "num_appointments": 3},
        {"id": 3, "name": "Charlie Garner", "num_appointments": 3},
        {"id": 1, "name": "Alice Wong", "num_appointments": 2},
    ]


# === MAIN ===
if __name__ == "__main__":
    test_flatten_patients()
    test_sort_patients_by_appointments()
