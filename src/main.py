"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def add_student(students, student_id, name, age, grade):
    """Thêm sinh viên mới vào danh sách (kiểm tra trùng mã)."""
    for s in students:
        if s.student_id == student_id:
            print(f"  [ERROR] Mã {student_id} đã tồn tại!")
            return False
    students.append(Student(student_id, name, age, grade))
    print(f"  [OK] Đã thêm: {name} ({student_id})")
    return True


def search_student(students, keyword):
    """Tìm sinh viên theo tên hoặc mã (không phân biệt hoa thường)."""
    keyword = keyword.lower()
    results = [s for s in students
               if keyword in s.name.lower() or keyword in s.student_id.lower()]
    return results


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

    # --- Tính năng: Thêm sinh viên ---
    print("\n--- Thêm sinh viên mới ---")
    add_student(students, "SV004", "Pham Van D", 20, "K21")
    add_student(students, "SV001", "Nguyen Van A", 20, "K20")  # Trùng mã

    print(f"\nTotal sau khi thêm: {len(students)} students")

    # --- Tính năng: Tìm kiếm sinh viên ---
    print("\n--- Tìm kiếm sinh viên ---")
    for keyword in ["Van", "SV002", "XYZ"]:
        found = search_student(students, keyword)
        print(f"  Từ khóa '{keyword}': {len(found)} kết quả")
        for s in found:
            print(f"    {s}")


if __name__ == "__main__":
    main()
