import cv2

def vid_into_frames(capture, every_x_frames):
    count_frames, frame_number, success = 0, 0, True
    while 1:
        success, image = capture.read()
        if success == True:
            if every_x_frames == 0 or count_frames % every_x_frames == 0:
                cv2.imwrite(f'frame{frame_number}.jpg', image)
                print(f'Successfully written {frame_number} frame')
                count_frames = 0
                frame_number += 1
            count_frames += 1
        else:
            exit()

def main():
    capture = cv2.VideoCapture('m_krummer.mp4')
    # A value that determines how often the frame from the video will be saved.
    # Place 0 - if you want to get every frame from the video.
    every_x_frames = 10
    vid_into_frames(capture, every_x_frames)

if __name__ == '__main__':
    main()
