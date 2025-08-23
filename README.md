# 📝 Quotes API

A simple **RESTful API** built with Flask that allows users to manage a collection of quotes.  
This project demonstrates the basics of API design, CRUD operations, and JSON handling in Flask.  

---

## 📖 Features
- **GET /quotes** → Retrieve a list of all quotes  
- **POST /quotes** → Add a new quote (accepts JSON payload)  
- **DELETE /quotes/<id>** → Delete a quote by its ID  
- Stores quotes in a **Python list of dictionaries** (no database required)  
- Tested with **Postman**  

---

## 🛠 Tech Stack
- **Backend:** Python, Flask  
- **Data Storage:** Python list (in-memory)  
- **Testing:** Postman  

---

## 📂 Project Structure
quotes-api/
├── app.py # Flask app entry point
├── requirements.txt # Python dependencies
├──quotes.json #json file for storing quotes
├──render.yaml
└── README.md # Project documentation
