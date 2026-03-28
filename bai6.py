import csv

def main():
    hop_le = []   # danh sách hợp lệ
    loi = []      # danh sách lỗi

    # ===== 1. Đọc file CSV =====
    try:
        with open("diemlop.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                ma = row["MaSV"]
                ten = row["HoTen"]
                diem_raw = row["Diem"]

                # ===== 2. Kiểm tra điểm có phải số =====
                try:
                    diem = float(diem_raw)
                except:
                    print(f"❌ Lỗi: {ma} - điểm không hợp lệ ({diem_raw})")
                    loi.append(f"{ma},{ten},{diem_raw} (không phải số)")
                    continue

                # ===== 3. Kiểm tra khoảng 0-10 =====
                if diem < 0 or diem > 10:
                    print(f"❌ Lỗi: {ma} - điểm ngoài khoảng ({diem})")
                    loi.append(f"{ma},{ten},{diem} (ngoài 0-10)")
                    continue

                # ===== 4. Dữ liệu hợp lệ =====
                hop_le.append((ma, ten, diem))

    except FileNotFoundError:
        print("❌ Không tìm thấy file diemlop.csv")
        return

    # ===== 5. Tính điểm trung bình =====
    if hop_le:
        dtb = sum(sv[2] for sv in hop_le) / len(hop_le)
    else:
        dtb = 0

    print("\nDanh sách hợp lệ:")
    for sv in hop_le:
        print(sv)

    print(f"\nĐiểm trung bình (hợp lệ): {dtb:.2f}")

    # ===== 6. Ghi file lỗi =====
    with open("loi.txt", "w", encoding="utf-8") as f:
        f.write("Danh sách lỗi:\n")
        for item in loi:
            f.write(item + "\n")

    print("\nĐã ghi lỗi vào file loi.txt")


if __name__ == "__main__":
    main()