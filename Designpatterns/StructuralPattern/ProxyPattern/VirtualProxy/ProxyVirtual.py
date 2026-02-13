from abc import ABC, abstractmethod


# --- Interface ---
class IImage(ABC):

    @abstractmethod
    def display(self):
        pass


# --- Real Object ---
class RealImage(IImage):

    def __init__(self, filename):
        self.filename = filename
        # Heavy operation
        print(f"[RealImage] Loading image from disk: {self.filename}")

    def display(self):
        print(f"[RealImage] Displaying {self.filename}")


# --- Proxy Class ---
class ImageProxy(IImage):

    def __init__(self, filename):
        self.filename = filename
        self.real_image = None   # not loaded yet

    def display(self):
        # Lazy loading
        if self.real_image is None:
            self.real_image = RealImage(self.filename)

        self.real_image.display()


# --- Main ---
if __name__ == "__main__":
    image1 = ImageProxy("radiant.jpg")

    # Real image loads only when display is called
    image1.display()
