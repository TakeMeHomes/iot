import tkinter as tk

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("340x520")
        self.root.resizable(0, 0)
        self.root.configure(bg="#121212")

        self.equation = ""
        self.display_text = tk.StringVar()
        self.display_text.set("0")

        self.create_widgets()

    def create_widgets(self):
        # --- หน้าจอแสดงผล (Display) ---
        display_frame = tk.Frame(self.root, bg="#121212")
        display_frame.pack(expand=True, fill="both", padx=20, pady=20)

        display_label = tk.Label(display_frame, textvariable=self.display_text, anchor="e", 
                                 bg="#121212", fg="#ffffff", font=("Helvetica", 36, "bold"))
        display_label.pack(expand=True, fill="both")

        # --- พื้นที่ปุ่มกด (Buttons) ---
        buttons_frame = tk.Frame(self.root, bg="#121212")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # โครงสร้างปุ่ม (ข้อความ, สีพื้นหลัง)
        buttons = [
            ('AC', '#f44336'), ('DEL', '#f44336'), ('%', '#ff9800'), ('/', '#ff9800'),
            ('7', '#2b2b2b'), ('8', '#2b2b2b'), ('9', '#2b2b2b'), ('*', '#ff9800'),
            ('4', '#2b2b2b'), ('5', '#2b2b2b'), ('6', '#2b2b2b'), ('-', '#ff9800'),
            ('1', '#2b2b2b'), ('2', '#2b2b2b'), ('3', '#2b2b2b'), ('+', '#ff9800'),
            ('0', '#2b2b2b'), ('.', '#2b2b2b'), ('=', '#4caf50')
        ]

        row_val = 0
        col_val = 0

        # สร้างปุ่มแบบวนลูปตามโครงสร้าง
        for text, color in buttons:
            action = lambda x=text: self.on_button_click(x)
            
            if text == '=':
                btn = tk.Button(buttons_frame, text=text, bg=color, fg="#ffffff", 
                                font=("Helvetica", 18, "bold"), borderwidth=0, command=action)
                btn.grid(row=row_val, column=col_val, columnspan=2, sticky="nsew", padx=6, pady=6)
                col_val += 2
            else:
                btn = tk.Button(buttons_frame, text=text, bg=color, fg="#ffffff", 
                                font=("Helvetica", 18, "bold"), borderwidth=0, command=action)
                btn.grid(row=row_val, column=col_val, sticky="nsew", padx=6, pady=6)
                col_val += 1
            
            # ขึ้นบรรทัดใหม่เมื่อครบ 4 คอลัมน์
            if col_val > 3:
                col_val = 0
                row_val += 1

        # จัดการสัดส่วนของ Grid ให้ขยายเต็มพื้นที่
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'AC':
            self.equation = ""
            self.display_text.set("0")
            
        elif char == 'DEL':
            self.equation = self.equation[:-1]
            self.display_text.set(self.equation if self.equation else "0")
            
        elif char == '=':
            try:
                # คำนวณผลลัพธ์
                # ปรับรูปแบบ % ให้คิดเป็นหาร 100 แบบง่ายๆ
                eval_eq = self.equation.replace('%', '/100')
                result = str(eval(eval_eq))
                
                # ตัดทศนิยม .0 ออกเพื่อให้ดูสวยงาม
                if result.endswith('.0'):
                    result = result[:-2]
                    
                self.display_text.set(result)
                self.equation = result
            except Exception:
                self.display_text.set("Error")
                self.equation = ""
        else:
            # ป้องกันการพิมพ์ 0 ซ้ำๆ ด้านหน้า
            if self.equation == "0" and char not in ['.', '+', '-', '*', '/']:
                self.equation = char
            else:
                self.equation += char
            self.display_text.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    calc = ModernCalculator(root)
    root.mainloop()