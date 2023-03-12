def describeStatus(networkStatus: int) -> str:
    """Describe network status since they're numeric and not informative"""
    statuses = {"0": "Link Down", "1": "Link Join", "2": "No IP found/assigned",
                "3": "Successfully Connected", "-1": "Fail",
                "-2": "No Network", "-3": "Failed Auth"}
    return statuses[str(networkStatus)]