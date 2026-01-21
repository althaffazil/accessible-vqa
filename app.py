import streamlit as st

from services.inference import VQAService
from services.confidence import estimate_confidence
from services.tts import TextToSpeech
from utils.image_utils import load_image
from utils.question_utils import normalize_question

st.set_page_config(
    page_title="Accessible Visual Question Answering",
    layout="centered"
)

st.title("Accessible Visual Question Answering")
st.caption("Ask complex questions about images using Vision-Language AI")

vqa_service = VQAService()
tts = TextToSpeech()

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

question = st.text_input(
    "Ask a question about the image",
    placeholder="e.g., What color is the car on the left?"
)

read_aloud = st.checkbox("Read answer aloud (Accessibility Mode)")

if uploaded_image and question:
    image = load_image(uploaded_image)
    normalized_question = normalize_question(question)

    st.image(image, use_column_width=True)

    with st.spinner("Analyzing image and reasoning..."):
        answer = vqa_service.answer(image, normalized_question)
        confidence = estimate_confidence(answer)

    st.success(f"Answer: {answer}")
    st.info(f"Model Confidence: {confidence}%")

    if confidence < 60:
        st.warning(
            "The model is not fully confident. The image may not clearly show the requested detail."
        )

    if read_aloud:
        tts.speak(answer)
