# app.py

# 1. Danh sách để lưu các công việc (Cấu trúc mới: list of dict)
# Mỗi công việc là một dictionary: {'name': 'Tên công việc', 'completed': False}
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    # SỬA ĐỔI: Thêm dictionary vào danh sách, với trạng thái completed mặc định là False
    new_task = {'name': task_name, 'completed': False}
    tasks.append(new_task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành dựa trên chỉ số (index) bắt đầu từ 1."""
    try:
        # Chuyển chỉ số từ 1 (người dùng) sang 0 (code)
        index = task_index - 1
        
        # Kiểm tra chỉ số hợp lệ
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print(f"Công việc số {task_index} ('{tasks[index]['name']}') đã được đánh dấu là hoàn thành.")
        else:
            print(f"Lỗi: Chỉ số {task_index} không hợp lệ.")
    except (TypeError, ValueError):
        print("Lỗi: Chỉ số công việc phải là một số nguyên.")

def list_tasks():
    """Duyệt qua danh sách và in ra tất cả công việc hiện có."""
    if not tasks:
        print("Danh sách công việc trống.")
        return
    
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    # SỬA ĐỔI: Duyệt qua dictionary và hiển thị trạng thái [x] hoặc [ ]
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")
    print("----------------------------")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    # 1. Thêm công việc (sử dụng cấu trúc mới)
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Chuẩn bị cho Yêu cầu 3")

    # 2. Liệt kê công việc
    list_tasks()

    # 3. Đánh dấu một công việc là hoàn thành (YÊU CẦU MỚI)
    complete_task(2) # Hoàn thành công việc số 2: "Làm bài tập thực hành ở nhà"
    complete_task(1) # Hoàn thành công việc số 1: "Học bài Git và GitHub"
    complete_task(10) # Thử một chỉ số không hợp lệ

    # 4. Liệt kê lại để xem trạng thái
    list_tasks()