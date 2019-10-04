class FileCreator:

    def __init__(self, file: str):
        self.file = file

    def create(self) -> None:
        with open(self.file, 'w+') as f:
            f.write('Hello, PuPPy!')
        return
