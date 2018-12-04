import cv2

from utils.figures import Region, Point

region = Region()


def on_mouse(event, x, y, flags, params):
    global region

    if event == cv2.EVENT_LBUTTONUP:
        region.add_corner(Point(x=x, y=y))


class RegionDetection(object):

    def __init__(self, url=0):
        self.url = url
        self.capture = cv2.VideoCapture(url)
        cv2.namedWindow('region', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('region', 1400, 800)
        cv2.setMouseCallback('region', on_mouse)

    def detect_region(self):
        _, image_frame = self.capture.read()
        while _:
            if region.is_ready:
                region.sort()
                image_frame = region.draw_region(image_frame)
                image_frame = cv2.putText(image_frame,
                                          "Region is set up, please press q to continue...",
                                          (30, 30),
                                          cv2.FONT_HERSHEY_DUPLEX,
                                          0.5,
                                          (0, 0, 0),
                                          2)
            cv2.imshow('region', image_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.capture.release()
        cv2.destroyAllWindows()
        return region
