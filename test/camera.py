import cv2

default_camera_name = '/dev/v4l/by-id/usb-046d_HD_Pro_Webcam_C920_A4EC6ABF-video-index0'


class Camera:
    def __init__(self, camera_name=default_camera_name, width=1920, height=1080):
        self.cap = cv2.VideoCapture(camera_name)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read(self):
        return self.cap.read()

    def get_frame(self):
        _, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()

