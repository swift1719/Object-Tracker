import cv2
import numpy as np
class ObjectTracker:
    def __init__(self, src):
        #capture the video source stream
        self.v_handle = cv2.VideoCapture(src)
        #test
        if not self.v_handle.isOpened():
            raise Exception('Cant Access ' + src)

        #attributes
        self.selection = [] #x1,y1,x2,y2
        self.state = 0
        self.frame = None

    def mouse_event_handler(self, event, x,y,flag, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.selection.clear() #clear
            self.selection.append(x)#x1
            self.selection.append(y)#y1
            self.state = 1 # roi definition started
        if event == cv2.EVENT_LBUTTONUP:
            self.selection.append(x)  # x2
            self.selection.append(y)  # y2
            self.state = 2 #roi definition ended

        if self.state == 2:
            #irrespective of the users drawing orientation (top-left to bottom-right,
            #top-right to bottom-left, bottem-left to top-right, bottom-right to top-left)
            #roi must be defined as x1,y1 (top-left) and x2,y2 (bottom-right)

            if self.selection[0] > self.selection[2]:
                temp = self.selection[0]
                self.selection[0] = self.selection[2]
                self.selection[2] = temp
            if self.selection[1] > self.selection[3]:
                temp = self.selection[1]
                self.selection[1] = self.selection[3]
                self.selection[3] = temp

            #auto correct the selection in case it has the window bounds crossed
            self.selection[0] = max(self.selection[0], 0) #x1:x1 or x1:0
            self.selection[1] = max(self.selection[1], 0) #y1:y1 or y1:0
            self.selection[2] = min(self.selection[2], self.frame.shape[1])  # x2:x2 or x2:frame.width
            self.selection[3] = min(self.selection[3], self.frame.shape[0])  # y2:y2 or y2:frame.height

            self.state =3

    def tracker(self):
        #Create a named window
        cv2.namedWindow('Object Tracker')
        #register for a callback on mouse event
        cv2.setMouseCallback('Object Tracker', self.mouse_event_handler)

        # know the fps
        fps = self.v_handle.get(cv2.CAP_PROP_FPS)
        #fetch a frame
        flag, self.frame = self.v_handle.read() # boolean, numpy.ndarray
        while flag:
            #convert the frame from BGR to HSV
            hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            if self.state == 3:
                #selection (x1,y1, x2, y2) is defined
                #grab the roi from the frame
                #for this we apply array slicing
                hsv_roi = hsv_frame[self.selection[1]:self.selection[3], self.selection[0]:self.selection[2]] # roi = frame[y1:y2, x1:x2]

                #know how colors are distributed over the ROI
                hist_hsv_roi = cv2.calcHist([hsv_roi],[0], None, [180], [0,180])

                cv2.imshow('HSV ROI', hsv_roi)

                #define a tracker window (l,t,w,h)
                tracker_window = []
                tracker_window.append(self.selection[0]) #x1 = left
                tracker_window.append(self.selection[1]) #y1 = top
                tracker_window.append(self.selection[2] - self.selection[0])  # w = x2 - x1
                tracker_window.append(self.selection[3] - self.selection[1])  # h = y2 - y1

                # set the camshifts termination criteria to: 10 iterations or max movement = 1 px
                t_criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TermCriteria_EPS, 10, 1)

                self.state =4 #state changes
            if self.state == 4:
                #lets backproject (locate) the histogram (roi) over the frame (video)
                back_projection = cv2.calcBackProject([hsv_frame], [0], hist_hsv_roi, [0,180], 1)
                #a mask to discard the dim or weakly pronouced areas of the frame
                mask = cv2.inRange(hsv_frame, np.array((0,60, 30)) , np.array((180,255, 230)) )
                back_projection = back_projection & mask

                cv2.imshow('Back Projection', back_projection)

                #track
                ellipse_params, tracker_window = cv2.CamShift(back_projection, tracker_window, t_criteria)
                #draw the ellipse on video frame
                cv2.ellipse(self.frame, ellipse_params, color=(255, 0,0), thickness=1)

            #render the frame
            cv2.imshow('Object Tracker', self.frame)
            #delay
            if cv2.waitKey(int(1/fps*1000)) == 27: #27 == ascii of ESC key
                break
            #fetch the next frame
            flag,self.frame = self.v_handle.read() #boolean, numpy.ndarray

        #dispose the windows
        cv2.destroyAllWindows()

    def __del__(self):
        if self.v_handle.isOpened():
            self.v_handle.release()

def main():
    ot = ObjectTracker('f:/TE_PBL/object tracker/a.mp4')
    ot.tracker()

main()