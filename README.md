# TIF-Splitter
Splits large .TIF files into squares of 1024x1024 and converts them into .PNG for easier image annotation. Users can then download all of the squares at once in a .zip file.

## How To Use

### Frontend

1. Install [Node.js](https://nodejs.org/) if you haven't already.
2. Navigate to the `frontend` folder.
3. Run `npm install` to install the required packages.
4. Run `npm start` to start the development server.

### Backend

1. Install [Python 3](https://www.python.org/downloads/) if you haven't already.
2. Navigate to the `backend` folder.
3. Create a virtual environment with `python3 -m venv venv`.
4. Activate the virtual environment with `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows).
5. Run `pip install -r requirements.txt` to install the required packages.
6. Run `export FLASK_APP=app` (Linux/Mac) or `set FLASK_APP=app` (Windows) to set the Flask app environment variable.
7. Run `flask run` to start the development server.

## Usage

1. Open your web browser and navigate to `http://localhost:3000` (frontend) and `http://localhost:5000` (backend).
2. Upload a GEOTIFF file using the "Upload" button.
3. Wait for the processing to complete.
4. Download the .zip file containing the 1024x1024 PNG tiles using the "Download" button.

## License

This project is licensed under the MIT License.
