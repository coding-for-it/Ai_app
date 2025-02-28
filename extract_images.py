import streamlit as st
import fitz  # PyMuPDF
import os
import zipfile
from PIL import Image
from io import BytesIO
from pdf2image import convert_from_bytes


def extract_images_pymupdf(uploaded_file):
    image_list = []
    temp_dir = "temp_images"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Read PDF using PyMuPDF
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page_number in range(len(pdf_document)):
        for img_index, img in enumerate(pdf_document[page_number].get_images(full=True)):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            if base_image:
                image_bytes = base_image["image"]
                img_ext = base_image["ext"]

                # Convert image bytes to PIL Image
                image = Image.open(BytesIO(image_bytes))
                image_path = os.path.join(temp_dir, f"page_{page_number + 1}_img_{img_index + 1}.{img_ext}")
                image.save(image_path)
                image_list.append(image_path)

    return image_list


def extract_images_pdf2image(uploaded_file):
    image_list = []
    temp_dir = "temp_images"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Convert PDF to images using pdf2image
    images = convert_from_bytes(uploaded_file.read())
    for i, image in enumerate(images):
        image_path = os.path.join(temp_dir, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        image_list.append(image_path)

    return image_list


def zip_images(image_paths):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for img_path in image_paths:
            zipf.write(img_path, os.path.basename(img_path))
    zip_buffer.seek(0)
    return zip_buffer


def extract_images_page():
    st.title("🖼️ Extract Images from PDF")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        with st.spinner("Extracting images..."):
            # First, try PyMuPDF for image extraction
            image_paths = extract_images_pymupdf(uploaded_file)

            # If PyMuPDF found no images, fall back to pdf2image
            if not image_paths:
                st.warning("No images found with PyMuPDF. Trying pdf2image as a fallback...")
                uploaded_file.seek(0)  # Reset file pointer after PyMuPDF read
                image_paths = extract_images_pdf2image(uploaded_file)

        if image_paths:
            st.success(f"Extracted {len(image_paths)} images!")

            # Show extracted images
            for img_path in image_paths:
                st.image(img_path, caption=os.path.basename(img_path), use_container_width=True)


            # Create a ZIP file
            zip_buffer = zip_images(image_paths)

            # Provide a download button for the ZIP
            st.download_button(
                label="📥 Download All Images",
                data=zip_buffer,
                file_name="extracted_images.zip",
                mime="application/zip"
            )
        else:
            st.warning("No images were found in this PDF!")
