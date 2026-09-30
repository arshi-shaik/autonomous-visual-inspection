import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.set_page_config(
    page_title="Autonomous Visual Inspection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Autonomous Visual Inspection System")
st.write("AI-powered PCB defect detection using YOLOv8.")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

uploaded_file = st.file_uploader(
    "Upload a PCB image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded PCB")
    st.image(
        image,
        caption="Input PCB Image",
        use_container_width=True
    )

    if st.button("🔍 Inspect PCB"):

        with st.spinner("Detecting defects..."):

            results = model(
                image,
                conf=0.25
            )

        result_image = results[0].plot()

        st.subheader("Inspection Result")

        st.image(
            result_image,
            caption="Detected PCB Defects",
            use_container_width=True
        )

        st.subheader("📋 Detected Defects")

        detections = results[0].boxes

        if len(detections) == 0:

            st.success("✅ No defects detected.")

        else:

            for box in detections:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = model.names[class_id]

                st.write(
                    f"🔴 **{class_name}** — "
                    f"{confidence * 100:.2f}% confidence"
                )
