# Bài 5: Đọc file và thống kê dữ liệu sinh viên

def main():
    ds = []

    # ===== 1. Đọc file =====
    try:
        with open("sinhvien.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(",")

                if len(data) != 3:
                    continue

                ma = data[0]
                ten = data[1]
                diem = float(data[2])

                ds.append((ma, ten, diem))

    except FileNotFoundError:
        print("❌ Không tìm thấy file sinhvien.txt")
        return

    # ===== 2. Thống kê =====
    so_luong = len(ds)

    if so_luong == 0:
        print("Danh sách rỗng!")
        return

    diem_tb = sum(sv[2] for sv in ds) / so_luong

    sv_dat = [sv for sv in ds if sv[2] >= 5]
    sv_khong_dat = [sv for sv in ds if sv[2] < 5]

    # ===== 3. Ghi file báo cáo =====
    with open("baocao.txt", "w", encoding="utf-8") as f:
        f.write("===== BAO CAO THONG KE =====\n")
        f.write(f"So luong sinh vien: {so_luong}\n")
        f.write(f"Diem trung binh: {diem_tb:.2f}\n")
        f.write(f"So sinh vien dat: {len(sv_dat)}\n")
        f.write(f"So sinh vien khong dat: {len(sv_khong_dat)}\n")

    # ===== 4. In ra màn hình =====
    print("Đã ghi báo cáo vào file baocao.txt")


if __name__ == "__main__":
    main()