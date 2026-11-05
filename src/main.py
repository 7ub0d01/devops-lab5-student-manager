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


def update_student(students, student_id, name=None, age=None, grade=None):
    """Sửa thông tin sinh viên theo mã (chỉ đổi các trường được truyền vào)."""
    for s in students:
        if s.student_id == student_id:
            if name is not None:
                s.name = name
            if age is not None:
                s.age = age
            if grade is not None:
                s.grade = grade
            print(f"  [OK] Đã sửa: {s}")
            return True
    print(f"  [ERROR] Không tìm thấy mã {student_id} để sửa!")
    return False


def delete_student(students, student_id):
    """Xóa sinh viên khỏi danh sách theo mã."""
    for s in students:
        if s.student_id == student_id:
            students.remove(s)
            print(f"  [OK] Đã xóa: {s.name} ({student_id})")
            return True
    print(f"  [ERROR] Không tìm thấy mã {student_id} để xóa!")
    return False


def main():
    """Hàm chính — menu nhập liệu thủ công."""
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    while True:
        print("=" * 50)
        print("STUDENT MANAGER — DevOps Lab 5")
        print("=" * 50)
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("4. Sửa sinh viên")
        print("5. Xóa sinh viên")
        print("0. Thoát")
        print("=" * 50)

        choice = input("Chọn chức năng (0-5): ").strip()

        if choice == "1":
            print("\n--- Danh sách sinh viên ---")
            for student in students:
                print(f"  {student}")
            print(f"\nTotal: {len(students)} students")

        elif choice == "2":
            print("\n--- Thêm sinh viên mới ---")
            student_id = input("  Mã sinh viên: ").strip()
            name = input("  Họ tên: ").strip()
            try:
                age = int(input("  Tuổi: ").strip())
            except ValueError:
                print("  [ERROR] Tuổi phải là số!")
                input("\nNhấn Enter để tiếp tục...")
                continue
            grade = input("  Lớp: ").strip()
            add_student(students, student_id, name, age, grade)

        elif choice == "3":
            print("\n--- Tìm kiếm sinh viên ---")
            keyword = input("  Nhập tên hoặc mã cần tìm: ").strip()
            found = search_student(students, keyword)
            print(f"  Tìm thấy {len(found)} kết quả:")
            for s in found:
                print(f"    {s}")

        elif choice == "4":
            print("\n--- Sửa sinh viên ---")
            student_id = input("  Mã sinh viên cần sửa: ").strip()
            name = input("  Họ tên mới (Enter để giữ nguyên): ").strip()
            age_input = input("  Tuổi mới (Enter để giữ nguyên): ").strip()
            grade = input("  Lớp mới (Enter để giữ nguyên): ").strip()
            age = None
            if age_input:
                try:
                    age = int(age_input)
                except ValueError:
                    print("  [ERROR] Tuổi phải là số!")
                    input("\nNhấn Enter để tiếp tục...")
                    continue
            update_student(
                students,
                student_id,
                name=name if name else None,
                age=age,
                grade=grade if grade else None,
            )

        elif choice == "5":
            print("\n--- Xóa sinh viên ---")
            student_id = input("  Mã sinh viên cần xóa: ").strip()
            confirm = input(f"  Xác nhận xóa {student_id}? (y/N): ").strip().lower()
            if confirm == "y":
                delete_student(students, student_id)
            else:
                print("  Đã hủy xóa.")

        elif choice == "0":
            print("Tạm biệt!")
            break

        else:
            print("  [ERROR] Lựa chọn không hợp lệ, chọn 0-5!")

        input("\nNhấn Enter để tiếp tục...")


if __name__ == "__main__":
    main()
