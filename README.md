# Rental Price Prediction Application

This project is a machine learning application that predicts rental prices for studio and one-bedroom apartments in Manhattan based on building images and structured data. It combines a deep learning model with a FastAPI backend and a React-based frontend to provide an interactive user experience.

---

## Features

- **Image-based Predictions** - Predicts rental prices using building images processed through a pre-trained ResNet50 model
- **Structured Data Integration** - Incorporates structured features like square footage, number of bedrooms, and neighborhood information
- **User-Friendly Web Interface** - A React frontend allows users to upload images and receive predictions
- **FastAPI Backend** - Processes image and structured data to make predictions

---

## Technologies Used

- **Backend** - FastAPI, PyTorch
- **Frontend** - React.js
- **Data Preprocessing** - scikit-learn
- **Deployment** - Uvicorn for backend API, npm for frontend development server

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- Node.js and npm
- Anaconda (optional but recommended for managing Python environments)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rental-price-prediction.git
   cd rental-price-prediction
2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
3. Set up the frontend:
   ```bash
   cd ../frontend
   npm install

### Usage
#### Backend
1. Navigate to the backend directory:
   ```bash
   cd backend
2. Start the backend server:
   ```bash
   uvicorn app:app --reload
#### Frontend
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
2. Start the React development server:
   ```bash
   npm start
3. Open a web browser and visit:
   ```bash
   http://localhost:3000

### Model Details
#### Training
The model combines:
1. **Image Features** - Extracted using a pre-trained ResNet50
2. **Structured Data Features** - Scaled and one-hot encoded numerical and categorical data
#### Saved Artifacts
- price_estimator_model.pth - Trained PyTorch model weights
- scaler_price.pkl - MinMaxScaler used for scaling price values
- encoder_neighborhood.pkl - OneHotEncoder used for encoding neighborhood categories

