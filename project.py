import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode('System') 
customtkinter.set_default_color_theme('green')  


class App(customtkinter.CTk):
    """Основной класс приложения для калькулятора."""
    def __init__(self):
        """Инициализация главного окна приложения."""
        super().__init__()
        self.title('Number Theory Calculator')
        self.geometry(f"{980}x{580}")
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        """Боковая панель с кнопками и настройками."""
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text='Calculator', font=customtkinter.CTkFont(size=20, weight='bold'))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = 'НОД(a,b)',font = customtkinter.CTkFont(size = 15, weight = 'bold'),command=self.gcdf)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text = 'НОK(a,b)',font = customtkinter.CTkFont(size = 15, weight = 'bold'), command=self.lcmf)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text = 'Простота числа a',font = customtkinter.CTkFont(size = 12, weight = 'bold'), command=self.primecheck)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text = 'Значение функции Эйлера числа a',font = customtkinter.CTkFont(size = 12, weight = 'bold'), command=self.eulercount)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame,text = 'Разложение на простые множители',font = customtkinter.CTkFont(size = 10, weight = 'bold'), command=self.factorizationf)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text='Appearance Mode:', anchor='w')
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(200, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=['Light', 'Dark', 'System'],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        
        """Фрейм для ввода чисел."""
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky='nsew')
        self.labelentry = customtkinter.CTkLabel(master=self.entry_frame, text='Введите числа a и b', font = customtkinter.CTkFont(size = 15, weight = 'bold'))
        self.labelentry.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.entry_1 = customtkinter.CTkEntry(master=self.entry_frame,placeholder_text='Число a')
        self.entry_1.grid(row=1, column=2, pady=10, padx=20, sticky='n')
        self.entry_2 = customtkinter.CTkEntry(master=self.entry_frame,placeholder_text='Число b')
        self.entry_2.grid(row=2, column=2, pady=10, padx=20, sticky='n')

        """Фрейм для отображения результатов вычисления НОД и НОК."""
        self.gcd = customtkinter.CTkFrame(self)
        self.gcd.grid(row=1,column = 1, padx = (20,20), pady = (20,20), sticky = "nsew")
        self.gcdinf = customtkinter.CTkLabel(master = self.gcd, text ='Наибольший общий делитель', font = customtkinter.CTkFont(size = 15, weight = 'bold') )
        self.gcdinf.grid(row = 0, column = 0, padx = 10, pady = 0)
        self.lcm = customtkinter.CTkFrame(self)
        self.lcm.grid(row=2,column = 1, padx = (20,20), pady = (20,20), sticky = 'nsew')
        self.lcminf = customtkinter.CTkLabel(master = self.lcm, text ='Наименьшее общее кратное', font = customtkinter.CTkFont(size = 15, weight = 'bold') )
        self.lcminf.grid(row = 0, column = 0, padx = 10, pady = 0)

        """Фрейм для отображения результатов проверки числа на простоту."""
        self.prime = customtkinter.CTkFrame(self)
        self.prime.grid(row = 0, column = 2, padx = (20,20), pady = (20,20), sticky = 'nsew')
        self.primeinf = customtkinter.CTkLabel(master = self.prime,text = 'Проверка простоты числа a', font = customtkinter.CTkFont(size = 15, weight = 'bold'))
        self.primeinf.grid(row = 0, column =  0, padx = 10, pady = 10)

        """Фрейм для отображения результатов вычисления функции Эйлера"""
        self.euler = customtkinter.CTkFrame(self)
        self.euler.grid(row = 1, column = 2, padx = (20,20), pady = (0,20), sticky = "nsew")
        self.eulerinf = customtkinter.CTkLabel(master = self.euler,text = 'Функция Эйлера числа a', font = customtkinter.CTkFont(size = 15, weight = 'bold'))
        self.eulerinf.grid(row = 0, column = 0, padx =10,pady = 10 )

        """Фрейм для отображения результата разложения числа на простые множители"""
        self.factorization = customtkinter.CTkFrame(self)
        self.factorization.grid(row = 2, column = 2, padx = 20 , pady = 20, sticky = 'nsew')
        self.factinfo = customtkinter.CTkLabel(master = self.factorization, text = 'Разложение числа a на простые множители', font = customtkinter.CTkFont(size = 15, weight = 'bold'))
        self.factinfo.grid(row = 0, column = 0, padx = 10, pady = 10)

    
        self.appearance_mode_optionemenu.set('System')
             
    def gcdf(self):
        """Находит НОД a и b"""
        a = int(self.entry_1.get())
        b = int(self.entry_2.get())
        a1 = a
        b1 = b
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.gcdinf2 = customtkinter.CTkLabel(master = self.gcd, text = f'НОД({a1},{b1}) = {a+b}')
        self.gcdinf2.grid(row =1, column = 0, padx = 10, pady = 0)
    def lcmf(self):
        """Находит НОК a и b"""
        a= int(self.entry_1.get())
        b= int(self.entry_2.get())
        a1 = a
        b1 = b
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        self.gcdinf3 = customtkinter.CTkLabel(master = self.lcm, text = f'НОК({a1},{b1}) = {(a1*b1)//(a+b)}')
        self.gcdinf3.grid(row =1, column = 0, padx = 10, pady = 0)
    def primecheck(self):
        """Проверяет число на простоту"""
        a = int(self.entry_1.get())
        if a == 1:
            self.primecheckinf = customtkinter.CTkLabel(master = self.prime, text = f'Число 1 не является простым')
            self.primecheckinf.grid(row = 1, column = 0, padx = 10, pady = 0)
            return 0
        d = 2
        while d * d <= a and a % d != 0:
            d += 1
        if d*d > a:
            self.primecheckinf = customtkinter.CTkLabel(master = self.prime, text = f'Число {a} простое')
            self.primecheckinf.grid(row = 1, column = 0, padx = 10, pady = 0)
        else:
            self.primecheckinf = customtkinter.CTkLabel(master = self.prime, text = f'Число {a} не является простым')
            self.primecheckinf.grid(row = 1, column = 0, padx = 10, pady = 0)
    def eulercount(self):
        """Вычисляет функцию Эйлера"""
        a = int(self.entry_1.get())
        result = 0
        for i in range(1,a):
            k = i
            a1 = a
            while a1 != 0 and k != 0:
                if a1 > k:
                    a1 = a1 % k
                else:
                    k = k % a1
            if max(a1,k) == 1:
                result += 1
        self.eulerinfor = customtkinter.CTkLabel(master = self.euler, text = f'φ({a}) = {result}')
        self.eulerinfor.grid(row = 1, column = 0, padx = 0, pady = 0)
    def factorizationf(self):
        """Выполняет разложение числа на простые множители"""
        a = int(self.entry_1.get())
        a1 = a
        Ans = []
        d = 2
        while d * d <= a:
            if a % d == 0:
                Ans.append(str(d))
                a = a // d
            else:
                d += 1
        if a > 1:
            Ans.append(str(a))
        s = "*".join(Ans)
        print(s)
        self.factor = customtkinter.CTkLabel(master = self.factorization, text =f'a = {s}')
        self.factor.grid(row = 1, column = 0, padx = 0, pady = 0) 

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Меняет тему приложения"""
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == '__main__':
    app = App()
    app.mainloop()
