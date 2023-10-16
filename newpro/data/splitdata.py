import os

def split_chapters(input_file_path, output_folder):
    # Đảm bảo thư mục đầu ra tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Đọc nội dung từ file đầu vào
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # Tách các chương dựa trên một đặc điểm nhất định (ví dụ: tiêu đề chương)
    chapters = content.split('Chương')

    # Lặp qua từng chương và tạo file cho mỗi chương
    for i, chapter_content in enumerate(chapters):
        # Tạo tên file cho mỗi chương (ví dụ: chuong_1.txt, chuong_2.txt, ...)
        output_file_path = os.path.join(output_folder, f'chuong_{i }.txt')

        # Ghi nội dung chương vào file mới
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(chapter_content.strip())

if __name__ == "__main__":
    # Thay đổi đường dẫn file đầu vào và thư mục đầu ra theo nhu cầu của bạn
    input_file_path = 'D:/web/newpro/data/tiên nghịch.txt'
    output_folder = 'D:/web/newpro/data/tien_nghich'

    split_chapters(input_file_path, output_folder)