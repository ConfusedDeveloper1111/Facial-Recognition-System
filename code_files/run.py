from create_dataset import start_capture
from create_classifier import train_classifer
from Detector import main_app

name = input("Enter your name: ")

print("Step 1: Capturing face data...")
start_capture(name)

print("Step 2: Training classifier...")
train_classifer(name)

print("Step 3: Starting face detection...")
main_app(name)
