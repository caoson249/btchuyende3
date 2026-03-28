import csv

# ===== 1. Đọc danh sách sinh viên từ file =====
def nhap_danh_sach():
    ds = []
    try:
        with open("studentsb4.csv", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ma = row["ma_sv"]
                ten = row["ten"]
                diem = float(row["diem"])
                ds.append((ma, ten, diem))
    except FileNotFoundError:
        print("❌ Không tìm thấy file studentsb4.csv")
    return ds


# ===== 2. Tính điểm trung bình =====
def tinh_diem_trung_binh(ds):
    if len(ds) == 0:
        return 0
    return sum(sv[2] for sv in ds) / len(ds)


# ===== 3. Tìm sinh viên điểm cao nhất =====
def tim_sv_max(ds):
    if not ds:
        return None
    return max(ds, key=lambda x: x[2])


# ===== 4. Xếp loại =====
def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "F"


# ===== 5. In báo cáo =====
def in_bao_cao(ds):
    if not ds:
        print("Danh sách rỗng!")
        return

    print("\n===== BÁO CÁO SINH VIÊN =====")

    # In danh sách + xếp loại
    for sv in ds:
        print(f"{sv[0]} - {sv[1]} - {sv[2]} - Xếp loại: {xep_loai(sv[2])}")

    # Điểm trung bình
    dtb = tinh_diem_trung_binh(ds)
    print(f"\nĐiểm trung bình lớp: {dtb:.2f}")

    # Sinh viên cao điểm nhất
    sv_max = tim_sv_max(ds)
    if sv_max:
        print("\nSinh viên có điểm cao nhất:")
        print(f"{sv_max[0]} - {sv_max[1]} - {sv_max[2]}")


# ===== Chương trình chính =====
def main():
    ds = nhap_danh_sach()
    in_bao_cao(ds)


if __name__ == "__main__":
    main()