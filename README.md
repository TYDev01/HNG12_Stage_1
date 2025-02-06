# Number Classification API

## Overview
This is a FastAPI-powered **Number Classification API** that takes an integer as input and returns mathematical properties of the number along with a fun fact.

## Features
- Determines whether the number is **prime**.
- Checks if the number is an **Armstrong number**.
- Identifies if the number is **perfect**.
- Classifies the number as **odd** or **even**.
- Calculates the **sum of digits**.
- Retrieves a **fun fact** about the number from [Numbers API](http://numbersapi.com/).

## API Endpoint
### **GET** `/api/classify-number`
**Query Parameter:**
- `number` (integer) - The number to classify.

### **Example Requests & Responses**
#### ✅ **Successful Response (200 OK)**
**Request:**
```http
GET /api/classify-number?number=371
```
**Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### ❌ **Invalid Input (400 Bad Request)**
**Request:**
```http
GET /api/classify-number?number=abc
```
**Response:**
```json
{
    "number": "abc",
    "error": true
}
```

## Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/TYDev01/HNG12_Stage_1.git
cd HNG12_Stage_1
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API Locally
```bash
uvicorn main:app --reload
```

### 5️⃣ Test the API
Open your browser or use Postman to visit:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

## Deployment
To deploy this API, you can use **Render, Railway, Vercel, or DigitalOcean**. Ensure the API is **publicly accessible**.

## Technologies Used
- **Python** 🐍
- **FastAPI** 🚀
- **Uvicorn**
- **Numbers API**

## License
MIT License © 2025 [TYDev](https://github.com/TYDev01)

---
### 🚀 **Contributions & Issues**
Feel free to **fork**, submit PRs, or open issues if you have suggestions or find bugs! 🎉

