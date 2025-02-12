import cv2
import sys

# 変換したいAVIファイルのパス
input_file = "input.avi"

# 出力したいMP4ファイルのパス
output_file = input_file+'.mp4'

# AVIファイルをOpenCVで読み込む
cap = cv2.VideoCapture(input_file)

newsize=50

# フレームレートとフレームサイズを取得
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 出力用のVideoWriterオブジェクトを作成
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter(output_file, fourcc, fps, (newsize, newsize))

while True:
    # フレームを取得
    ret, frame = cap.read()

    # フレームが存在しない場合はループを抜ける
    if not ret:
        break
    
    rframe=cv2.resize(frame, (newsize, newsize))

    # フレームを書き込む
    writer.write(rframe)

# リソースを開放
cap.release()
writer.release()
