import os
import cv2

#preprocess train data
#covid19
folder_path = 'Raw_Data/train/COVID19'
output_folder = 'Preprocessed_Data/train/COVID19_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

#normal
folder_path = 'Raw_Data/train/NORMAL'
output_folder = 'Preprocessed_Data/train/NORMAL_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

#PNEUMONIA
folder_path = 'Raw_Data/train/PNEUMONIA'
output_folder = 'Preprocessed_Data/train/PNEUMONIA_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)



#preprocess test data
#covid19
folder_path = 'Raw_Data/test/COVID19'
output_folder = 'Preprocessed_Data/test/COVID19_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

#normal
folder_path = 'Raw_Data/test/NORMAL'
output_folder = 'Preprocessed_Data/test/NORMAL_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)

#PNEUMONIA
folder_path = 'Raw_Data/test/PNEUMONIA'
output_folder = 'Preprocessed_Data/test/PNEUMONIA_RGB'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

files = os.listdir(folder_path)

for file in files:
    gray_image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(gray_image, (224, 224))
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2RGB)
    output_path = os.path.join(output_folder, file.replace('.jpg', '_RGB.jpg')) 
    cv2.imwrite(output_path, rgb_image)
