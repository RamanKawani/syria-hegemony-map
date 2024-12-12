# Example static data or database query function
regional_data = {
    "Idlib": {
        "foreignState": "Turkey",
        "localGroup": "HTS",
        "influenceLevel": 80,
        "details": {"militaryPresence": "High", "politicalControl": "Partial"}
    }
}

def get_region_data(region_name):
    return regional_data.get(region_name, {})
