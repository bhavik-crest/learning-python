# 🐍 Learning Python

## Product CRUD App
This is a full-stack **Product CRUD** application built using:

- 🌐 **Frontend**: React.js  
- ⚙️ **Backend**: FastAPI (Python)

---

## 📁 Project Structure
```
product-crud-app/
├── backend/
│   └── main.py
├── frontend/
│   └── src/
│       └── ... (React code)
└── README.md
```

## 🛠️ Setup Instructions

### 📦 Frontend (React.js)

Navigate to the frontend directory and start the React development server:

```bash
cd frontend
npm install
npm start
```
This will run the frontend at: http://localhost:3000

### 🐍 Backend (FastAPI)
```bash
cd backend
python -m uvicorn main:app --reload`
```
This will run the backend at: http://localhost:8000

You can access the FastAPI interactive docs at: http://localhost:8000/docs
