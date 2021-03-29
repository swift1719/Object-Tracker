import cv2


class MotionTracker:
    def __init__(self, src=0):
        self.v_handle = cv2.VideoCapture(src)
        if not self.v_handle.isOpened():
            raise Exception(src + ' is not accessible')

        # 3 frames
        self.prev_frame = None
        self.curr_frame = None
        self.next_frame = None

    def frame_difference(self):
        d1 = cv2.absdiff(self.prev_frame, self.curr_frame)
        d2 = cv2.absdiff(self.curr_frame, self.next_frame)
        return cv2.bitwise_and(d1, d2)  # movement

    def track(self):
        # create 2 windows
        cv2.namedWindow('VIDEO')
        cv2.namedWindow('TRACKER')

        # know the fps
        fps = self.v_handle.get(cv2.CAP_PROP_FPS)

        # initialize the frames
        _, self.prev_frame = self.v_handle.read()  # fetch a frame and return a tuple(read status (boolean), frame (ndarray))
        _, self.curr_frame = self.v_handle.read()
        flag, self.next_frame = self.v_handle.read()

        while flag:
            # render the frames
            cv2.imshow('VIDEO', self.curr_frame)
            cv2.imshow('TRACKER', self.frame_difference())

            # delay and break support
            if cv2.waitKey(int(1 / fps * 1000)) == 27:  # ESC hit
                break

            # reinitialize the frame
            self.prev_frame = self.curr_frame
            self.curr_frame = self.next_frame
            flag, self.next_frame = self.v_handle.read()

        cv2.destroyAllWindows()

    def __del__(self):
        if self.v_handle.isOpened():
            self.v_handle.release()


def main():
    mt = MotionTracker('f:/TE_PBL/resource/bears.mp4')
    mt.track()


main()
