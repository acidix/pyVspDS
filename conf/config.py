"""Configuration file for pyVspDS
"""

__config__ = {
            "racktables":
                {
                    "apiurl": "http://racktables/api.php",
                    "username": "admin",
                    "password": "secret"
                },
            "vsphere":
                {
                    "server": "vsphere",
                    "username": "root",
                    "password": "secret"
                },
            "general":
                {
                    "objtype_id": "1504",
                    "linkparent": "25",
                    "dnssuffix": ".mycompany.lan",
                    "force": False,
                    "forceattrs": ["17", "10000", "14"]
                }
}
