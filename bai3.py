import csv

def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "F"


def main():
    scores = []

    # Đọc file CSV
    with open("diem.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores.append(float(row["diem"]))

    print("Danh sách điểm:", scores)

    # 1. Điểm đạt (>=5)
    passed = [x for x in scores if x >= 5]
    print("Điểm đạt:", passed)

    # 2. Bình phương điểm đạt
    squared = [x**2 for x in passed]
    print("Bình phương điểm đạt:", squared)

    # 3. Tạo dict xếp loại
    result = {i+1: xep_loai(scores[i]) for i in range(len(scores))}

    print("Xếp loại sinh viên:")
    for k, v in result.items():
        print(f"Sinh viên {k}: {v}")


if __name__ == "__main__":
    main()