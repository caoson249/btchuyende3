# Bài 2: Thống kê dữ liệu bằng dict và set

def main():
    # Dữ liệu ban đầu
    subjects = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

    # 1. Loại bỏ phần tử trùng lặp bằng set
    unique_subjects = set(subjects)
    print("Danh sách không trùng:", unique_subjects)

    # 2. Đếm số lần xuất hiện bằng dict
    count_dict = {}
    for sub in subjects:
        if sub in count_dict:
            count_dict[sub] += 1
        else:
            count_dict[sub] = 1

    print("Số lần xuất hiện:", count_dict)

    # 3. Môn học được đăng ký nhiều nhất
    max_subject = max(count_dict, key=count_dict.get)
    print("Môn học đăng ký nhiều nhất:", max_subject)

    # 4. Sắp xếp giảm dần theo số lần
    sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    print("Danh sách sau khi sắp xếp giảm dần:")
    for sub, count in sorted_list:
        print(sub, ":", count)


# Chạy chương trình
if __name__ == "__main__":
    main()