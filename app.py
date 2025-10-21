# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
def list_tasks():
    """Duyệt qua danh sách và in ra tất cả công việc hiện có."""
    if not tasks:
        print("Danh sách công việc trống.")
        return

    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    # Duyệt qua danh sách và in ra với chỉ mục bắt đầu từ 1
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("----------------------------")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()