import tkinter as tk
from tkinter import ttk

class DataEntryForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Entry Form")
        self.geometry("500x450")

        self.create_widgets()

    def create_widgets(self):
        # Frame thông tin người dùng
        user_info_frame = ttk.LabelFrame(self, text="User Information")
        user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # First Name
        ttk.Label(user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5)
        self.first_name = ttk.Entry(user_info_frame)
        self.first_name.grid(row=1, column=0, padx=5, pady=5)

        # Last Name
        ttk.Label(user_info_frame, text="Last Name").grid(row=0, column=1, padx=5, pady=5)
        self.last_name = ttk.Entry(user_info_frame)
        self.last_name.grid(row=1, column=1, padx=5, pady=5)

        # Title
        ttk.Label(user_info_frame, text="Title").grid(row=0, column=2, padx=5, pady=5)
        self.title_var = tk.StringVar()
        self.title_combobox = ttk.Combobox(user_info_frame, textvariable=self.title_var, values=["Mr.", "Ms.", "Dr.", "Prof."])
        self.title_combobox.grid(row=1, column=2, padx=5, pady=5)

        # Age
        ttk.Label(user_info_frame, text="Age").grid(row=2, column=0, padx=5, pady=5)
        self.age_spinbox = ttk.Spinbox(user_info_frame, from_=18, to=100)
        self.age_spinbox.grid(row=3, column=0, padx=5, pady=5)

        # Nationality
        ttk.Label(user_info_frame, text="Nationality").grid(row=2, column=1, padx=5, pady=5)
        self.nationality = ttk.Entry(user_info_frame)
        self.nationality.grid(row=3, column=1, padx=5, pady=5)

        # Frame tình trạng đăng ký
        reg_status_frame = ttk.LabelFrame(self, text="Registration Status")
        reg_status_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Currently Registered
        self.reg_var = tk.BooleanVar()
        self.currently_registered = ttk.Checkbutton(reg_status_frame, text="Currently Registered", variable=self.reg_var)
        self.currently_registered.grid(row=0, column=0, padx=5, pady=5)

        # Completed Courses
        ttk.Label(reg_status_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5)
        self.completed_courses = ttk.Spinbox(reg_status_frame, from_=0, to=50)
        self.completed_courses.grid(row=0, column=2, padx=5, pady=5)

        # Semesters
        ttk.Label(reg_status_frame, text="# Semesters").grid(row=1, column=1, padx=5, pady=5)
        self.semesters = ttk.Spinbox(reg_status_frame, from_=0, to=20)
        self.semesters.grid(row=1, column=2, padx=5, pady=5)

        # Frame điều khoản & điều kiện
        terms_frame = ttk.LabelFrame(self, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.terms_var = tk.BooleanVar()
        self.terms_checkbutton = ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=self.terms_var)
        self.terms_checkbutton.grid(row=0, column=0, padx=5, pady=5)

        # Nút Enter Data
        self.enter_data_button = ttk.Button(self, text="Enter data", command=self.enter_data)
        self.enter_data_button.grid(row=3, column=0, pady=10)

    def enter_data(self):
        # Logic xử lý khi nhấn nút Enter data
        print("First Name:", self.first_name.get())
        print("Last Name:", self.last_name.get())
        print("Title:", self.title_var.get())
        print("Age:", self.age_spinbox.get())
        print("Nationality:", self.nationality.get())
        print("Currently Registered:", self.reg_var.get())
        print("# Completed Courses:", self.completed_courses.get())
        print("# Semesters:", self.semesters.get())
        print("Terms Accepted:", self.terms_var.get())

if __name__ == "__main__":
    app = DataEntryForm()
    app.mainloop()