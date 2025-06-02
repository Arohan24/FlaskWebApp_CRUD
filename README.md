
# 📝 Flask MongoDB Form App

This is a simple Flask web application that lets users submit a form containing their name and email. Submitted data is stored in a MongoDB database. You can also view all submissions from a separate route.

## 🚀 Features

* Submit form data (name and email)
* Save data to MongoDB Atlas
* Display success page after submission
* View all submitted data
* Flash messages for form validation and errors

## 🛠️ Tech Stack

* Python
* Flask
* MongoDB Atlas
* PyMongo
* dotenv (for environment variable management)
* HTML Templates with Jinja2

## 📂 Project Structure

```
project/
│
├── templates/
│   ├── form.html
│   ├── success.html
│   └── view.html
│
├── .env
├── app.py
├── requirements.txt
└── README.md
```

## 🔧 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` File**

   Inside the project folder, create a `.env` file and add the following:

   ```
   MongoDB_Username=your_mongodb_username
   MongoDB_Password=your_mongodb_password
   App_Secret=your_flask_secret_key
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

5. **Access in Browser**
   Open your browser and go to `http://localhost:5000`

## 📄 Routes

| Route      | Description                        |
| ---------- | ---------------------------------- |
| `/`        | Form page (input name and email)   |
| `/submit`  | POST route to submit the form      |
| `/success` | Page shown after successful submit |
| `/view`    | View all submitted form data       |

## 📌 Notes

* Ensure MongoDB Atlas is accessible and credentials are correct.
* This app uses a database called `testdb` and a collection called `formdata`.

## 📃 License

This project is open-source and free to use.
