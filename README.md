# Fracture Detection Application

This application detects bone fractures from X-ray images using a YOLOv8-based object detection model. It provides an API for uploading images and retrieving detection results. The results include a URL of the processed image uploaded to Cloudinary.

## Features

- **FastAPI Backend**: REST API for image detection.
- **YOLOv8 Model**: For detecting fractures in X-ray images.
- **Cloudinary Integration**: Upload and serve processed images.

---

## Getting Started

### Prerequisites

1. Python 3.8 or above installed.
2. Cloudinary account for image uploads.

---

### Setting Up the Backend

1. Clone this repository and navigate to the project folder:

   ```bash
   git clone https://github.com/your-repo/fracture-detection-app.git
   cd fracture-detection-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Navigate to the `backend` folder:

   ```bash
   cd backend
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run webserver and open `index.html` file in the `frontend` folder.

---

### Configuring Cloudinary

1. Create a `.env` file in the `backend` folder.
2. Add your Cloudinary credentials:
   ```plaintext
   CLOUD_NAME=your_cloud_name
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ```

---

### Running the Backend

1. Start the FastAPI development server:
   ```bash
   fastapi dev main.py
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

---

### Testing the API

1. Open your browser and navigate to the interactive API documentation:
   ```
   http://127.0.0.1:8000/docs
   ```
2. Use the `/detect/fracture` endpoint to upload an image and receive a processed image URL.

---

## Contributing

Feel free to submit issues and pull requests to improve the application.

---

## License

This project is licensed under the [MIT License](LICENSE).
