import os

data_dir = r"C:\Users\Gamil\Desktop\foodsnap-ai\dataset\Indian Food Images\Indian Food Images"  # replace with your actual path
class_names = sorted(os.listdir(data_dir))

with open("classes.txt", "w") as f:
    for name in class_names:
        f.write(name + "\n")
