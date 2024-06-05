# XTractor

## Overview
XTractor is an application that allows users to upload PDF documents and ask questions about the content of those documents. It consists of a React frontend and a FastAPI backend, leveraging NLP models for question answering.

## Technologies Used

- **Frontend**:
  - React
  - Axios (for API requests)

- **Backend**:
  - FastAPI
  - Transformers (Hugging Face Transformers library for NLP processing)
  - PyMuPDF (for extracting text from PDF files)

- **NLP Model**:
  - `deepset/roberta-base-squad2` (Hugging Face model for question answering)

## How It Works

1. **Upload PDF Document**:
   - Users can upload a PDF document with a specified title through the frontend interface.
   - The frontend sends the document to the backend via an Axios POST request.

2. **Store and Process Document**:
   - The backend receives the document, saves it, and processes it to extract text.

3. **Ask Questions**:
   - Users can ask questions about the content of the uploaded document.
   - The frontend sends the question and the file path of the uploaded document to the backend.

4. **NLP Processing**:
   - The backend uses the Hugging Face `deepset/roberta-base-squad2` model to find the answer to the question based on the document content.
   - The backend returns the answer to the frontend.

5. **Display Answer**:
   - The frontend displays the answer to the user.

![image](https://github.com/prem-karanwal/XTractor/assets/113821428/b5bb8745-aeac-4853-9f68-1f5f6f41a574)
![image](https://github.com/prem-karanwal/XTractor/assets/113821428/870abf62-4948-4f82-b227-5d74281307d2)
![image](https://github.com/prem-karanwal/XTractor/assets/113821428/2c66c84d-b53d-4b87-b84f-6ab1a4db33da)

 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 👋 Hey there, I'm Prem Karanwal!

Passionate about coding, creating, and exploring the endless possibilities in the tech realm. Currently on a journey to transform ideas into reality as a Computer Science undergraduate at [Indian Institute Of Information Technology, Kota](https://www.iiitkota.ac.in/).

## 🚀 About Me

🎓 **Education:** Pursuing a Bachelor of Technology in Computer Science.

👨‍💻 **Skills:**
- **Languages:** C, C++, Python, JavaScript, HTML/CSS
- **Computer Vision:** OpenCV, Image Processing, Object Detection, Image Segmentation, Feature Extraction
- **Machine Learning**: Tensorflow, Scikit-learn
- **Miscellaneous:** Numpy, Pandas, Matplotlib, MySQL

### Skills Proficiency:

- **HTML/CSS:** █████████ 90%
- **JavaScript:** ████████ 80%
- **C/C++:** ████████ 80%
- **Python:** ████████ 80%
- **OpenCV:** ███████ 75%
- **MindAR:** ████████ 80%
- **Tableau:** ██████ 70%



Ready to connect, collaborate, and contribute to the next wave of technological innovations. Let's code the future together! 🚀

Connect with me on [LinkedIn](https://linkedin.com/in/prem-karanwal/) or check out my coding adventures on [GitHub](https://github.com/prem-karanwal).

Feel free to explore my projects and drop a ⭐ if anything sparks your interest! ✨



