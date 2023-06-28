import cv2
import ffmpeg
from datetime import datetime
import numpy as np
import os

def main():
    width, height = 1920, 1080

    background = np.zeros((height, width, 3), np.uint8)

    ffmpeg_process = (
        ffmpeg.input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(width, height))
        .output(f"rtmp://{os.environ['TARGET_SERVER']}/live/live", vcodec='libx264', pix_fmt='yuv420p', format='flv')
        .overwrite_output()
        .run_async(pipe_stdin=True)
    )

    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        frame = np.copy(background)
        frame = cv2.putText(
            img=frame,
            text=current_time,
            org=(50, 200),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=4,
            color=(255, 255, 255),
            thickness=2,
        )

        # cv2.imshow('Cam', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        ffmpeg_process.stdin.write(frame.tobytes())

    ffmpeg_process.stdin.close()
    ffmpeg_process.wait()

    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
