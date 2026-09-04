# QR Generator Using Python

A simple Python-based QR Code Generator that allows users to generate QR codes from  URLs.

## 🚀 Features

* Generate QR codes using Python
* Supports text and URLs
* Saves generated QR codes as image files
* Simple and beginner-friendly implementation

## 🛠️ Technologies Used

* Python
* qrcode
* Pillow

## 📥 Installation & Setup

### Step 1: Clone the Repository

bash
git clone <your-repository-url>
cd QR-Code-Using-Python


### Step 2: Create & Activate Virtual Environment

Create a virtual environment:

bash
python -m venv .venv


Activate it on Windows PowerShell:

powershell
.\.venv\Scripts\Activate.ps1
```

 Step 3: Install Required Libraries

Install the required dependencies:

```bash
pip install qrcode
pip install Pillow
```

Or install them together:

bash
pip install qrcode Pillow


### Step 4: Run the Project

After adding your code to `qr.py`, run:

bash
python qr.py
```

Your QR code will be generated and saved according to the configuration in the Python file.

## 📂 Project Structure

```text
QR-Code-Using-Python/
│
├── qr.py
├── .venv/
└── README.md
```

## 📌 Future Improvements

* Add a graphical user interface
* Allow users to customize QR colors
* Add QR code size and error-correction options
* Create a web-based QR generator

