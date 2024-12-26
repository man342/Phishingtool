### **Phishing Simulation and Awareness Tool**

This project is designed to simulate phishing attacks and educate users on recognizing and avoiding phishing attempts. It demonstrates how attackers use phishing techniques to trick users and provides feedback to help users improve their security awareness.

The tool sends phishing emails with a link to a fake login page. When users click the link or enter credentials, their actions are logged for analysis. After submitting credentials, users are redirected to an educational feedback page that explains the simulation and offers tips to avoid real phishing attempts.

---

### **Technologies Used**

The backend is built with Python and Flask to host fake login pages and track user actions. SQLite is used to log user interactions, and smtplib is used for email automation. ngrok is employed to expose the tool to the internet, making it accessible from any device.

---

### **How It Works**

1. Phishing emails are sent to recipients with a realistic message and a link to a fake login page.
2. Clicking the link opens the fake login page, mimicking popular services like Amazon.
3. User actions, such as clicking the link or submitting credentials, are logged in a database.
4. Users receive educational feedback after interacting with the fake login page.
5. An admin dashboard displays user interactions for analysis.

---

### **Steps to Execute**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/man342/Phishingtool.git
   cd phishing-simulation-tool
   ```

2. **Set Up the Environment**:
   - Create a virtual environment and install dependencies:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install flask
     ```

3. **Start the Flask Server**:
   - Navigate to the `server/` directory and start the server:
     ```bash
     cd server
     python3 app.py
     ```

4. **Expose the Server Using ngrok**:
   - Run ngrok to make the server publicly accessible:
     ```bash
     ngrok http 5000
     ```
   - Replace the `http://127.0.0.1:5000` link in the phishing email with the ngrok URL.

5. **Send Phishing Emails**:
   - Navigate to the `email_sender/` directory and run the script:
     ```bash
     cd ../email_sender
     python3 email_sender.py
     ```

6. **Test the Simulation**:
   - Open the phishing email, click the link, and interact with the fake login page.
   - Check the SQLite database for logged user actions:
     ```bash
     sqlite3 ../server/database.sqlite
     SELECT * FROM logs;
     SELECT * FROM clicks;
     ```

7. **View the Dashboard**:
   - Access the dashboard via the ngrok link:
     ```
     http://<ngrok-url>/dashboard
     ```

---

### **Disclaimer**

This tool is for educational purposes only. Unauthorized use is strictly prohibited. Use it responsibly and with the consent of participants.
