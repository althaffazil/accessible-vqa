from models.blip_vqa import BLIPVQA

class VQAService:
    def __init__(self):
        self.model = BLIPVQA()

    def answer(self, image, question):
        return self.model.predict(image, question)
