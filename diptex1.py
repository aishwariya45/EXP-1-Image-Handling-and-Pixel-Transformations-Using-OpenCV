#!/usr/bin/env python
# coding: utf-8

# # *EXP-1 Image Handling and Pixel Transformations Using OpenCV* #
# # *NAME AISHWARIYA* #
# # *REG NO : 212224240005

# In[ ]:


import cv2
import matplotlib.pyplot as plt


# In[11]:


# Read the image using OpenCV
img = cv2.imread('Qno. 1.jpg', cv2.IMREAD_COLOR)


# In[12]:


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[13]:


# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  # You can change 'viridis' to another cmap or use None for RGB images
plt.title("Original Image")
plt.axis('off')  # Removes axis ticks and labels
plt.show()


# In[14]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[15]:


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[16]:


img_rgb.shape


# In[17]:


# Draw a line from top-left to bottom-right
line_img = cv2.line(img_rgb, (0, 0), (768, 600), (255, 0, 0), 2) # cv2.line(image, start_point, end_point, color, thickness)


# In[18]:


plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()


# In[19]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[20]:


img_rgb.shape


# In[21]:


circle_img = cv2.circle(img_rgb,(400,300),150,(255,0,0),10) # cv2.circle(image, center, radius, color, thickness)


# In[22]:


plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()


# In[23]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[24]:


img.shape


# In[25]:


# Draw a rectangle around the Whole image
rectangle_img = cv2.rectangle(img_rgb, (0, 0), (768, 600), (0, 0, 255), 10)  # cv2.rectangle(image, start_point, end_point, color, thickness)


# In[26]:


plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()


# In[27]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[28]:


# Add text to the image
text_img = cv2.putText(img_rgb, "OpenCV Drawing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 10)  ## cv2.putText(image, text, position, font, font_scale, color, thickness)



# In[29]:


plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()


# In[30]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[33]:


# Original RGB Image
plt.imshow(img_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[34]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[35]:


# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[36]:


# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)


# In[37]:


# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")


# In[38]:


# Convert RGB to GRAY
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# In[39]:


# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")


# In[40]:


# Convert RGB to YCrCb
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)


# In[41]:


# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")


# In[42]:


# Convert HSV back to RGB
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)


# In[43]:


plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")


# In[44]:


# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  # Rows: 200-499, Columns: 200-499


# In[45]:


# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[46]:


# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()


# In[47]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[48]:


# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)


# In[49]:


# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


# In[50]:


resized_image_rgb.shape


# In[51]:


# Display the resized image
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()


# In[52]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[53]:


image.shape


# In[54]:


# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  # Rows: 50-349, Columns: 50-349


# In[55]:


# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)


# In[56]:


# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()


# In[57]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[58]:


# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)


# In[59]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)


# In[60]:


# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")


# In[61]:


# Flip the image vertically (up-down)
flipped_vertically = cv2.flip(image, 0)


# In[62]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)


# In[63]:


# Vertical flip
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




