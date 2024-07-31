# Flask Image Processing Web App

A simple web application for image processing using Flask and HTML. This app allows users to upload images, preview them, apply basic processing (like converting to grayscale), and download the processed images.

## Features

- **Upload Image:** Users can upload images from their computer.
- **Image Preview:** Uploaded images can be displayed on the web page.
- **Image Processing:** Basic operations like grayscale conversion.
- **Download Processed Image:** Users can download the processed image.
- **Upload History:** Displays the history of uploaded and processed images.

## Project Structure

```
image_processing_app/
├── app/
│ ├── static/
│ │ ├── css/
│ │ ├── images/
│ │ └── js/
│ ├── templates/
│ │ ├── index.html
│ │ └── result.html
│ ├── init.py
│ ├── routes.py
│ └── utils.py
├── instance/
│ └── uploads/
├── .gitignore
├── README.md
├── config.py
├── requirements.txt
└── run.py
```


## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/yourusername/image_processing_app.git
   cd image_processing_app
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
    - Windows:

    ```sh
    venv\Scripts\activate
    ```

    - MacOS/Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install dependencies:**
    ```pip install -r requirements.txt```


5. **Run the application:**
    ```python run.py```

6. Open your web browser and go to http://127.0.0.1:5000/ to see the application.

### Usage

- Go to the home page.
- Click on the "Choose File" button to upload an image.
- Click "Upload" to upload the image.
- The uploaded image will be displayed.
- Click "Process Image" to apply the grayscale conversion.
- Download the processed image.

### .gitignore
Make sure to ignore the virtual environment folder by adding the following line to your .gitignore file:

```venv/```

### License
This project is licensed under the MIT License - see the LICENSE file for details.