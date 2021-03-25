# video_player
import cv2


class VideoRender:
    def __init__(self, src=0):  # constructor
        self.src = src
        self.v_handle = cv2.VideoCapture(self.src)  # open the video file / access the webcam (src : 0)
        if not self.v_handle.isOpened():  # on failure
            raise FileExistsError(self.src + ' not accessible')

        # print(self.v_handle.get(cv2.CAP_PROP_FPS)) #FPS
        # print(self.v_handle.get(cv2.CAP_PROP_FRAME_WIDTH)) #WIDTH
        # print(self.v_handle.get(cv2.CAP_PROP_FRAME_HEIGHT)) #HEIGHT
        # print(self.v_handle.get(cv2.CAP_PROP_FRAME_COUNT)) #FRAMES
        # print(self.v_handle.get(cv2.CAP_PROP_FRAME_COUNT) / self.v_handle.get(cv2.CAP_PROP_FPS)) #DURATION

    def play(self):
        cv2.namedWindow('VIDEO PLAYER')
        fps = self.v_handle.get(cv2.CAP_PROP_FPS)
        while True:
            flag, frame = self.v_handle.read()  # (boolean, numpy.ndarray)
            if not flag:
                break
            cv2.imshow('VIDEO PLAYER', frame)  # render

            if cv2.waitKey(int(1 / fps * 1000)) == 27:  # delay + break on ESC
                break

        cv2.destroyWindow('VIDEO PLAYER')

    def __del__(self):  # destructor
        if self.v_handle.isOpened():
            self.v_handle.release()


def main():
    vr = VideoRender('f:/TE_PBL/resource/bears.mp4')
    vr.play()


main()
