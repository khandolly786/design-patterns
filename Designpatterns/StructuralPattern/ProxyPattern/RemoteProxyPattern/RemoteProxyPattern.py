from abc import ABC, abstractmethod


# --- Interface ---
class IDataService(ABC):

    @abstractmethod
    def fetch_data(self) -> str:
        pass


# --- Real Service (Simulating Remote Server) ---
class RealDataService(IDataService):

    def __init__(self):
        # Simulate heavy remote connection setup
        print("[RealDataService] Initialized (simulating remote setup)")

    def fetch_data(self) -> str:
        return "[RealDataService] Data from server"


# --- Remote Proxy ---
class DataServiceProxy(IDataService):

    def __init__(self):
        self._real_service = None  # Lazy initialization

    def fetch_data(self) -> str:
        print("[DataServiceProxy] Connecting to remote service...")

        if self._real_service is None:
            self._real_service = RealDataService()

        return self._real_service.fetch_data()


# --- Client Code ---
if __name__ == "__main__":
    data_service = DataServiceProxy()
    print(data_service.fetch_data())
