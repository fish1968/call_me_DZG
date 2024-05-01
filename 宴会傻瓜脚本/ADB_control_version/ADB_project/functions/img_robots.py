import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
import cv2
import numpy as np

class ImgRobot:
    def __init__(self, image_path = None):
        if image_path != None:
            try:
                self.image = cv2.imread(image_path)
            except Exception as e:
                print("An error occurred during reading images:", str(e))
                return None
        self.position = [0, 0]
        self.brightness = None
    def get_image(self):
        return self.image
    
    def get_image_shape(self):
        height, width, channels = self.image.shape
        # twist height and width order
        return width, height,  channels 
    def get_pixel_rgb(self, x, y):
        pixel_value = self.image[y, x]
        rgb_value = (int(pixel_value[2]), int(pixel_value[1]), int(pixel_value[0]))
        return rgb_value
    def find_image_position(self, img2, threshold, left_most=0, right_most=None, top_most=0, down_most=None, at_center = True):
        # return the left top pixel if not at_center
        # otherwise return the center of matched image
        try:
            if right_most is None:
                right_most = self.image.shape[1]
            if down_most is None:
                down_most = self.image.shape[0]
            
            search_area = self.image[top_most:down_most, left_most:right_most]
            
            result = cv2.matchTemplate(search_area, img2, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            
            if max_val >= threshold:
                abs_position = (max_loc[0] + left_most , max_loc[1] + top_most)
                if at_center == True:
                    shape = img2.shape
                    abs_position = int(abs_position[0] + shape[0]/2),int( abs_position[1] + shape[1]/2)
                return abs_position
            else:
                return None
        except Exception as e:
            print("An error occurred during template matching:", str(e))
            return None
    def find_image_position_with_robot(self, robot, threshold = 0.8, left_most=0, right_most=None, top_most=0, down_most=None, at_center = True):
        img2 = robot.get_image()
        return self.find_image_position(img2, threshold, left_most, right_most, top_most, down_most, at_center) 
    def get_sub_image(self, start_x, start_y, width, height):
        sub_image = self.image[start_y:start_y+height, start_x:start_x+width]
        return sub_image

    def get_brightness(self, refresh = False):
        if self.brightness != None and refresh == False:
            return self.brightness
        else:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            average_brightness = np.mean(gray_image)
            return average_brightness

    def get_subregion_brightness(self, x1, y1, width, height):
        sub_image = self.image[y1:y1+height, x1:x1+width]
        gray_image = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
        average_brightness = np.mean(gray_image)
        return average_brightness

if __name__ == "__main__":
    # Example usage
    image_path1 = "test1.png"
    image_path2 = "test2.png"

    robot = ImgRobot(image_path1)

    # Load the second image
    image2 = cv2.imread(image_path2)

    # Get the RGB value of a pixel at the position
    pixel_rgb = robot.get_pixel_rgb(robot.position[0], robot.position[1])
    # Specify the sub-image dimensions
    start_x = 100
    start_y = 200
    width = 300
    height = 400

    # Get the sub-image
    sub_image = robot.get_sub_image(start_x, start_y, width, height)

    # Save the sub-image to a file
    sub_image_path = "sub_image.png"
    cv2.imwrite(sub_image_path, sub_image)

    print("Image shape:", robot.get_image().shape)
    print("Current position:", robot.position)
    print("RGB value at position:", pixel_rgb)

    # Find the position of image2 within image1
    threshold = 0.8
    match_position = robot.find_image_position(image2, threshold)

    if match_position is not None:
        print("Image2 found at position:", match_position)
    else:
        print("No match found.")
