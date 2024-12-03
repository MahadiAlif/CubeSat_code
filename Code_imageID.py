import tensorflow as tf
import numpy as np
from PIL import Image

# Load the pre-trained MobileNetV2 model
interpreter = tf.lite.Interpreter(model_path='mobilenet_v2_1.0_224_quant.tflite')
interpreter.allocate_tensors()

# Get input and output tensors
input_tensor_index = interpreter.get_input_details()[0]['index']
output = interpreter.tensor(interpreter.get_output_details()[0]['index'])

# Load and preprocess an image
image_path = 'path/to/your/image.jpg'
image = Image.open(image_path).resize((224, 224))
image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
image = np.expand_dims(image, axis=0)  # Add batch dimension

# Perform inference
interpreter.set_tensor(input_tensor_index, image)
interpreter.invoke()

# Get the results
predictions = output()[0]
predicted_class = np.argmax(predictions)

# Print the results
print(f"Predicted class: {predicted_class}")

