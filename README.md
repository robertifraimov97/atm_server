📌 Flask-Based Banking API

📄 Downloadable Documentation

📄 **A detailed project report is available for download:**  
👉 [Download README.docx](https://github.com/robertifraimov97/atm_server/raw/main/README.docx)

🚀 **Live API URL**

The deployed API is hosted on Heroku:  
👉 [Banking API on Heroku](https://secure-savannah-57890-9c2b88f4bf0c.herokuapp.com/)

📌 **Note:** The API follows a RESTful structure, and direct interactions require a tool like cURL.


📌 API Endpoints

The following endpoints are available in the Banking API:

1️⃣ Get Account Balance

🔹 Endpoint: GET /accounts/<account_number>/balance
🔹 Example Request: curl -X GET https://secure-savannah-57890-9c2b88f4bf0c.herokuapp.com/accounts/123456/balance  
🔹 Expected Response: {"account_number": "123456", "balance": 1000.0}

2️⃣ Withdraw Funds

🔹 Endpoint: POST /accounts/<account_number>/withdraw
🔹 Example Request: curl -X POST "https://secure-savannah-57890-9c2b88f4bf0c.herokuapp.com/accounts/123456/withdraw" \
     -H "Content-Type: application/json" \
     -d '{"amount": 200}'  
🔹 Expected Response: {"message": "Withdrawal successful", "amount": 200}

3️⃣ Deposit Funds

🔹 Endpoint: POST /accounts/<account_number>/deposit
🔹 Example Request: curl -X POST "https://secure-savannah-57890-9c2b88f4bf0c.herokuapp.com/accounts/123456/deposit" \
     -H "Content-Type: application/json" \
     -d '{"amount": 500}'  
🔹 Expected Response: {"message": "Deposit successful", "amount": 500}
