# Sample campus graph.
# Distances are illustrative, not actual campus measurements.

CAMPUS_GRAPH = {
    "Main Gate": {
        "Admin Block": 150,
        "Academic Block A": 250,
        "Parking Area": 100,
    },

    "Admin Block": {
        "Main Gate": 150,
        "Academic Block A": 100,
        "Auditorium": 200,
    },

    "Academic Block A": {
        "Main Gate": 250,
        "Admin Block": 100,
        "Academic Block B": 120,
        "Library": 180,
    },

    "Academic Block B": {
        "Academic Block A": 120,
        "Library": 100,
        "Computer Labs": 150,
    },

    "Library": {
        "Academic Block A": 180,
        "Academic Block B": 100,
        "Canteen": 130,
        "Hostel": 250,
        "Department Block": 120,
    },

    "Canteen": {
        "Library": 130,
        "Computer Labs": 180,
        "Sports Ground": 200,
        "Parking Area": 100,
        "Hostel": 200,
    },

    "Computer Labs": {
        "Academic Block B": 150,
        "Canteen": 180,
        "Auditorium": 160,
    },

    "Auditorium": {
        "Admin Block": 200,
        "Computer Labs": 160,
    },

    "Sports Ground": {
        "Canteen": 200,
        "Hostel": 170,
        "Seminar Hall": 120,
    },

    "Hostel": {
        "Library": 250,
        "Sports Ground": 170,
        "Canteen": 200,
        "Medical Center": 140,
    },

    "Medical Center": {
        "Hostel": 140,
        "Department Block": 100,
    },

    "Parking Area": {
        "Main Gate": 100,
        "Canteen": 100,
    },

    "Seminar Hall": {
        "Sports Ground": 120,
        "Department Block": 100,
    },

    "Department Block": {
        "Library": 120,
        "Medical Center": 100,
        "Seminar Hall": 100,
    },
}