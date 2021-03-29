import cv2
import numpy

# defining the region of interest(ROI) on video frames
class ROI:
    def __init__(self, src=0):
        #  initialising the resources
        self.v_handle = cv2.VideoCapture(src)
        if not self.v_handle.isOpened():
            raise Exception(src + " not accessible.")

        self.frame = None
        #  roi
        self.roi = []  # x1,y1,x2,y2
        # action flag
        self.selection_state = 0

    # called by cv2 on detection of mouse activity on
    def mouse_event_handler(self, event, x, y, flag, param):
        # event parameter represents what event happened
        # x,y represents co-ordinates where event occured
        # flag represent if any other event is also happened like keypress also ctrl+click
        # parameter which are setup from caller
        if event == cv2.EVENT_LBUTTONDOWN:
            # print('mouse left button down @(', x, y, ')')
            self.roi.clear()
            self.roi.append(x)
            self.roi.append(y)
            self.selection_state = 1
        elif event == cv2.EVENT_LBUTTONUP:
            print('mouse left button up @(', x, y, ')')
            self.roi.append(x)
            self.roi.append(y)
            self.selection_state = 2
        # dragging orientation from
        # top-left to bottom-right
        # bottom-left to top-right
        # top-right to bottom-left
        # bottom-right to top-left
        # correct it in a way so that x1,y1 is top left and x2,y2 is bottom right
        if self.selection_state == 2:
            if self.roi[0] > self.roi[2]:  # x1>x2
                temp = self.roi[0]
                self.roi[0] = self.roi[2]
                self.roi[2] = temp
            if self.roi[1] > self.roi[3]:
                temp = self.roi[1]
                self.roi[1] = self.roi[3]
                self.roi[3] = temp
            # for out of bounds area
            self.roi[0] = max(self.roi[0], 0)
            self.roi[1] = max(self.roi[1], 0)

            self.roi[2] = min(self.roi[2], self.frame.shape[0])
            self.roi[3] = min(self.roi[3], self.frame.shape[1])

    def read(self):
        # create window
        cv2.namedWindow("Video Roi")

        # enable mouse event callback
        cv2.setMouseCallback("Video Roi", self.mouse_event_handler)
        # know the fps (for playing speed)
        fps = self.v_handle.get(cv2.CAP_PROP_FPS)
        # initialize

        flag, self.frame = self.v_handle.read()
        while flag:
            if self.selection_state == 2:
                cv2.rectangle(self.frame, pt1=(self.roi[0], self.roi[1]), pt2=(self.roi[2], self.roi[3]),
                              color=(0, 127, 255), thickness=2)

            # render
            cv2.imshow("Video Roi", self.frame)

            # reinitialize
            flag, self.frame = self.v_handle.read()

            # delay and exit option
            if cv2.waitKey(int(1 / fps * 1000)) == 27:
                break
        cv2.destroyAllWindows()


def main():
    roi = ROI("f:/TE_PBL/resource/bears.mp4");
    roi.read()


main()
