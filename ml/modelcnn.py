
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os,sys
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.layers import DepthwiseConv2D
from tensorflow.keras.models import load_model

def efficient_net (img_path) : 
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_DIR = os.path.join(BASE_DIR,  'ml')  # Sesuaikan dengan struktur direktori Anda
#     sys.path.append(MODEL_DIR)
    model_path = MODEL_DIR +'/efficientnet_model.h5'  # Sesuaikan dengan nama model Anda
  # Replace with your actual model file name
    model = load_model(model_path)
    # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    class_names = ['MildDemented','ModerateDemented', 'NonDemented',  'VeryMildDemented']
# Replace this with the path to your image
    img = Image.open(img_path).convert("RGB")
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Check the shape of the image array
    print("Image array shape:", img_array.shape)  # Should output: (1, 224, 224, 3)

    # Step 6: Load the pre-trained model

    # Recompile the model to include metrics (using a dummy optimizer since we are not training)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Step 7: Predict the class probabilities
    predictions = model.predict(img_array)
    index = np.argmax(predictions)
    predicted_class = np.argmax(predictions, axis=1)
    confidence_score = predictions[0][index]
    # print("Predicted Class:", predicted_class)
    # print("confidence_score" ,confidence_score)
    # # Step 8: Map predicted class index to class name
    # predicted_class_name = class_names[predicted_class[0]]
    # print("Predicted Class Name:", predicted_class_name)
    return  class_names[predicted_class[0]] , confidence_score
# def alex(image_path):
#     # Disable scientific notation for clarity
#     np.set_printoptions(suppress=True)
#     # Load the model 
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     MODEL_DIR = os.path.join(BASE_DIR,  'ml')  # Sesuaikan dengan struktur direktori Anda
#     sys.path.append(MODEL_DIR)
#     model_path = MODEL_DIR +'/vgg19_model.h5'  # Sesuaikan dengan nama model Anda
#     model = tensorflow.keras.models.load_model(model_path)
#     model.compile( optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#     # Load the labels
#     class_names = ['MildDemented','ModerateDemented', 'NonDemented',  'VeryMildDemented']
#     # Create the array of the right shape to feed into the keras model
#     # The 'length' or number of images you can put into the array is
#     # determined by the first position in the shape tuple, in this case 1
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#     # Replace this with the path to your image
#     image = Image.open(image_path).convert("RGB")
#     # resizing the image to be at least 224x224 and then cropping from the center
#     size = (224, 224)
#     image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

#     # turn the image into a numpy array
#     image_array = np.asarray(image)

#     # Normalize the image
#     normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

#     # Load the image into the array
#     data[0] = normalized_image_array

#     # Predicts the model
#     prediction = model.predict(data)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     confidence_score = prediction[0][index]
#     return class_name,confidence_score

def vgg19(img_path):
#     # Disable scientific notation for clarity
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_DIR = os.path.join(BASE_DIR,  'ml')  # Sesuaikan dengan struktur direktori Anda
#     sys.path.append(MODEL_DIR)
    model_path = MODEL_DIR +'/vgg19_model.h5'  # Replace with your actual model file name
    model = load_model(model_path)
    # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    class_names = ['MildDemented','ModerateDemented', 'NonDemented',  'VeryMildDemented']
# Replace this with the path to your image
    img = Image.open(img_path).convert("RGB")
    if img.mode != 'RGB':
        img = img.convert('RGB')

    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Check the shape of the image array
    print("Image array shape:", img_array.shape)  # Should output: (1, 224, 224, 3)

    # Step 6: Load the pre-trained model

    # Recompile the model to include metrics (using a dummy optimizer since we are not training)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Step 7: Predict the class probabilities
    predictions = model.predict(img_array)
    index = np.argmax(predictions)
    predicted_class = np.argmax(predictions, axis=1)
    confidence_score = predictions[0][index]
    # print("Predicted Class:", predicted_class)
    # print("confidence_score" ,confidence_score)
    # # Step 8: Map predicted class index to class name
    # predicted_class_name = class_names[predicted_class[0]]
    # print("Predicted Class Name:", predicted_class_name)
    return  class_names[predicted_class[0]] , confidence_score

# efficient_net("moderate.jpg")