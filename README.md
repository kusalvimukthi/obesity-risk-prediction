# Obesity Risk Prediction Software

This software application predicts the obesity risk level of individuals based on various factors such as age, height, weight, eating habits, physical activity, and more. The prediction is made using a machine learning model (Random Forest) that has been trained on relevant data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository or Download the Files](#1-clone-the-repository-or-download-the-files)
  - [2. Create a New Python Environment](#2-create-a-new-python-environment)
  - [3. Install Required Libraries](#3-install-required-libraries)
  - [4. Place the Model File](#4-place-the-model-file)
- [Running the Application](#running-the-application)
  - [1. Start the Flask Web Server](#1-start-the-flask-web-server)
  - [2. Open the Application in a Browser](#2-open-the-application-in-a-browser)
- [Using the Application](#using-the-application)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.7+**
- **Anaconda** (Recommended for managing Python environments)
- **A code editor or IDE** (like VS Code, PyCharm)

## Setup Instructions

### 1. Clone the Repository or Download the Files

First, clone this repository to your local machine or download the ZIP file and extract it.

git clone https://github.com/kusalvimukthi/obesity-risk-prediction.git
cd obesity-risk-prediction


### 2. Create a New Python Environment
Using Anaconda, create a new environment to ensure all dependencies are correctly installed without affecting other projects.

conda create --name obesity_prediction_env python=3.9
conda activate obesity_prediction_env


### 4. Install Required Libraries

With the environment activated, install the necessary Python libraries. Run the following command in the Anaconda Prompt:

pip install flask pandas scikit-learn joblib


### 5. Place the Model File

Ensure that the trained model file (random_forest_model5.pkl) is located in the model directory within the project folder.



## Running the Application


### 1. Start the Flask Web Server

Run the following command in the Anaconda Prompt to start the Flask web server:

python app.py

If everything is set up correctly, you should see an output similar to:

Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


### 2. Open the Application in a Browser

http://127.0.0.1:5000/
