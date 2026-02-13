from abc import ABC, abstractmethod


# --- Interface ---
class IDocumentReader(ABC):

    @abstractmethod
    def unlock_pdf(self, file_path: str, password: str):
        pass


# --- Real Object ---
class RealDocumentReader(IDocumentReader):

    def unlock_pdf(self, file_path: str, password: str):
        print(f"[RealDocumentReader] Unlocking PDF at: {file_path}")
        print(f"[RealDocumentReader] PDF unlocked successfully with password: {password}")
        print("[RealDocumentReader] Displaying PDF content...")


# --- User Class ---
class User:
    def __init__(self, name: str, premium_membership: bool):
        self.name = name
        self.premium_membership = premium_membership


# --- Proxy Class (Protection Proxy) ---
class DocumentProxy(IDocumentReader):

    def __init__(self, user: User):
        self.user = user
        self._real_reader = RealDocumentReader()

    def unlock_pdf(self, file_path: str, password: str):
        if not self.user.premium_membership:
            print("[DocumentProxy] Access denied. Only premium members can unlock PDFs.")
            return

        # Forward request to real object
        self._real_reader.unlock_pdf(file_path, password)


# --- Client Code ---
if __name__ == "__main__":

    user1 = User("Darakhshan", False)   # Non-premium user
    user2 = User("Naheed", True)   # Premium user

    print("== Darakhshan (Non-Premium) tries to unlock PDF ==")
    doc_reader = DocumentProxy(user1)
    doc_reader.unlock_pdf("protected_document.pdf", "secret123")

    print("\n== Naheed (Premium) unlocks PDF ==")
    doc_reader = DocumentProxy(user2)
    doc_reader.unlock_pdf("protected_document.pdf", "secret123")
