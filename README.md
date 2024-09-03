
# Music Genre Classification

This project is a web application that classifies music into different genres using a deep learning model. Users can upload music files, and the application will predict the genre of the music. The project uses a Convolutional Neural Network (CNN) model to classify the music genres.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction

Music Genre Classification is a project that aims to classify audio files into different genres using deep learning. The model has been trained on a dataset of music files and can classify genres such as pop, rock, classical, and jazz, among others.

## Features

- Upload music files in formats like `.mp3` and `.wav`.
- Predict the genre of the uploaded music using a pre-trained CNN model.
- View recently uploaded files and their predicted genres.

## Demo

![image](https://github.com/user-attachments/assets/3213ef8d-2db5-447d-8f1d-d1297f61ebc7)
![image](https://github.com/user-attachments/assets/8d4c4c5e-f94b-43d0-810f-1e5e9b6c5652)


## Technologies Used

- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, JavaScript
- **Model:** Convolutional Neural Network (CNN) with Keras
- **Database:** None (in-memory storage used for recent uploads)


## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yawarKhaplu/Music_Genre_Classification/
   cd Music_Genre_Classification
   ```

2. **Install dependencies:**

   Make sure you have Python 3 installed. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Git LFS (if not already done):**

   ```bash
   git lfs install
   git lfs track "*.keras"
   ```

4. **Run the application:**

   ```bash
   flask run
   ```

5. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Add Music:**

   - Navigate to the "Add Music" page.
   - Upload your music file.
   - The application will classify the music and display the predicted genre.

2. **View Recent Uploads:**

   - Recent uploads and their predicted genres can be viewed on the main page.

## Project Structure

```plaintext
Music_Genre_Classification/
│
├── static/
│   ├── css/
│   ├── js/
│   └── music/
│
├── templates/
│   ├── index.html
│   └── add_music.html
│
├── uploads/
│   └── (uploaded music files)
│
├── Music_Genre_Classification_Final_Model.keras
├── app.py
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.


## Acknowledgements

- This project was inspired by the growing need for automated music genre classification.
- Thanks to [Kaggle](https://www.kaggle.com/) for the dataset used in training the model.

