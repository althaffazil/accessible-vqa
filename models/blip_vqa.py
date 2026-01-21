import torch
from transformers import BlipProcessor, BlipForQuestionAnswering

class BLIPVQA:
    def __init__(self, model_name="Salesforce/blip-vqa-base"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForQuestionAnswering.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, image, question):
        inputs = self.processor(
            images=image,          # ✅ correct key
            text=question,         # ✅ correct key
            return_tensors="pt"
        )

        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            output_ids = self.model.generate(**inputs)

        answer = self.processor.decode(
            output_ids[0],
            skip_special_tokens=True
        )

        return answer