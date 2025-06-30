## 🚀 How to Run the To-Do App

### 🪟 For Windows:
1. Open the `ToDoApp` folder
2. Double-click `launch.bat`
3. Your browser will open the app
4. If you see a black terminal window — that’s normal!

> 🧩 Optional: Right-click → "Create Shortcut" → Add custom icon (e.g., `icon.ico`)

---

### 🍎 For macOS:
1. Open the `ToDoApp` folder
2. Double-click `launch.command`
3. If you see a security message the first time:
   - Right-click → Open
   - Then approve it under **System Settings > Privacy & Security**

✅ You can move the `ToDoApp` folder anywhere — the app will still work!

### To close the web app just quit the terminal or press ctrl+C


### 🐍 Install Python & Streamlit (Required Once)

Before running the app, make sure you have **Python** and **Streamlit** installed.

---

## 🪟 Windows

1. 🔹 **Install Python**  
   Download it from [python.org](https://www.python.org/downloads/windows/)  
   ✅ During installation, **check the box** that says:  
   > "Add Python to PATH"

2. 🔹 **Open Command Prompt**  
   Press `Win + R`, type `cmd`, and hit Enter

3. 🔹 **Install Streamlit**  
   Run this in the terminal:

   ```bash
   pip install streamlit


## 🍎 Macos

Before running the app, make sure you have **Python 3** and **Streamlit** installed.

---

### ✅ Step 1: Check if Python 3 is installed

Open **Terminal** and run:

```bash
python3 --version
```
If you see something like Python 3.x.x, you're good to go.
If not, install Python from python.org or with Homebrew:

```bash
brew install python
```
# Step 2: Install streamlit

Open **Terminal** and run:
```bash
pip install streamlit
```

# Step 3: Install All Required Packages

After downloading the app folder, install all required packages by opening **Terminal** from the folder:
-Right-click the folder
-Go to services
-Click New terminal at Folder

Then run
```bash
pip3 install -r requirements.txt
```
