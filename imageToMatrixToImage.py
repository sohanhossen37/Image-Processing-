from PIL import Image
import numpy as np

# Load the image and convert it to a NumPy array (matrix)
image_path = 'Rose.jpg'  # Replace with your image file path
image = Image.open(image_path)
image_matrix = np.array(image)

# Print the matrix shape
print("Image Matrix Shape:", image_matrix.shape)
print(image_matrix)  # You can also print the matrix if you want to see it

# Convert the matrix back to an image
image_from_matrix = Image.fromarray(image_matrix)

# Save or display the image
image_from_matrix.save('output_image.jpg')  # Save the image
image_from_matrix.show()  # Display the image
