import os
import cv2

left=900
top=50
right=1500
bottom=500

def crop_images(input_folder, output_folder, crop_box):
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # フォルダ内の全画像ファイルを処理
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 画像を読み込む
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)
            
            # トリミング
            cropped_img = img[crop_box[1]:crop_box[3], crop_box[0]:crop_box[2]]
            
            # トリミングした画像を保存
            cv2.imwrite(os.path.join(output_folder, filename), cropped_img)

if __name__ == "__main__":
    # 入力フォルダ、出力フォルダ、トリミングボックスを指定
    input_folder = 'C:/Users/labta/Downloads'  # 画像フォルダのパス
    output_folder = 'C:/Users/labta/Downloads/after'  # 出力フォルダのパス
    crop_box = (left, top, right, bottom)  # トリミングする領域（左, 上, 右, 下）

    crop_images(input_folder, output_folder, crop_box)
