# 📸 Image Resizer Tool

A simple Python tool to **resize multiple images in batch**.
Built using **Python 3** and the **Pillow (PIL)** library.


## 🚀 Features

✔ Resize multiple images at once
✔ Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`
✔ Enter custom **width & height**
✔ Uses **default folders** (or ask user at runtime)
✔ Auto-creates the output folder
✔ Beginner-friendly CLI tool


## 📂 Project Structure

Image-Resizer-Tool/
│── image_resize.py   # Main script
│── images/           # (Put your original images here)
│── resized/          # (Resized images will be saved here)
│── README.md         # Project documentation


## 🛠️ Installation

1. **Clone the repository**

bash:
git clone https://github.com/SyedDanish6897/Image-Resizer-Tool.git
cd Image-Resizer-Tool

2. **Install dependencies**

-- pip install pillow


## ▶️ Usage

Run the script:

bash:
python image_resize.py


### Output :

📸 Welcome to Image Resizer Tool

Enter the folder path where your images are stored (default: images): 
Enter the folder name for resized images (default: resized): 
Enter new width (default: 800): 500
Enter new height (default: 600): 500

✅ Resized and saved: resized/photo1.jpg
✅ Resized and saved: resized/photo2.png

🎉 Done! 2 images resized and saved in 'resized' folder.



## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.
