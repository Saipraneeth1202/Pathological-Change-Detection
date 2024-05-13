import os
import cv2

#preprocess train data
#covid19
folder_path = 'Raw_Data/train/COVID19'
output_folder = 'Preprocessed_Data_2/train/COVID19_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("Train covid 19 is done...")

#normal
folder_path = 'Raw_Data/train/NORMAL'
output_folder = 'Preprocessed_Data_2/train/NORMAL_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("Train normal is done...")

#PNEUMONIA
folder_path = 'Raw_Data/train/PNEUMONIA'
output_folder = 'Preprocessed_Data_2/train/PNEUMONIA_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("Train pneumonia is done...")

#preprocess test data
#covid19
folder_path = 'Raw_Data/test/COVID19'
output_folder = 'Preprocessed_Data_2/test/COVID19_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("Test covid 19 is done...")

#normal
folder_path = 'Raw_Data/test/NORMAL'
output_folder = 'Preprocessed_Data_2/test/NORMAL_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("Test normal is done...")

#PNEUMONIA
folder_path = 'Raw_Data/test/PNEUMONIA'
output_folder = 'Preprocessed_Data_2/test/PNEUMONIA_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (299, 299))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

print("test pneumonia is done...")
