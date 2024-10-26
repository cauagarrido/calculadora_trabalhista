import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from calculadora import *  

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Trabalhista")

       
        master.configure(bg="#1F1F1F")
        self.history_text = tk.StringVar()
        self.salario_bruto = 0
        self.horas_trabalhadas = 0
        self.historico = []

        
        self.label = tk.Label(master, text="Calculadora Trabalhista", font=("Arial", 18, "bold"), fg="#F0F0F0", bg="#1F1F1F")
        self.label.pack(pady=10)

        
        buttons = [
            ("Calcular Salário Bruto", self.calcular_salario_bruto),
            ("Calcular Horas Extras", self.calcular_horas_extras),
            ("Calcular INSS", self.calcular_inss),
            ("Calcular IRRF", self.calcular_irrf),
            ("Calcular Férias Proporcionais", self.calcular_ferias_proporcionais),
            ("Calcular 13º Salário Proporcional", self.calcular_13_salario),
            ("Calcular FGTS", self.calcular_fgts),
            ("Calcular Rescisão", self.calcular_rescisao),
            ("Sair", master.quit)
        ]

        for text, command in buttons:
            self.create_button(text, command)

    
        self.history_label = tk.Label(master, text="Histórico de Cálculos", fg="#C0C0C0", bg="#1F1F1F", font=("Arial", 12, "bold"))
        self.history_label.pack(pady=5)

        self.history_box = scrolledtext.ScrolledText(master, width=50, height=10, bg="#2E2E2E", fg="#DADADA", font=("Arial", 10), state="disabled", wrap="word")
        self.history_box.pack(pady=5, padx=10)

        
        self.details_label = tk.Label(master, text="Detalhes do Cálculo", fg="#C0C0C0", bg="#1F1F1F", font=("Arial", 12, "bold"))
        self.details_label.pack(pady=5)

        self.details_box = scrolledtext.ScrolledText(master, width=50, height=5, bg="#2E2E2E", fg="#DADADA", font=("Arial", 10), state="disabled", wrap="word")
        self.details_box.pack(pady=5, padx=10)

    def create_button(self, text, command):
        btn = tk.Button(self.master, text=text, command=command, bg="#333333", fg="#FFFFFF", font=("Arial", 12), width=40, height=1, relief="flat")
        btn.config(highlightbackground="#555555", highlightthickness=1)
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#505050"))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#333333"))
        btn.pack(pady=4, padx=10)

    def add_to_history(self, message):
        self.historico.append(message)
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, message + "\n")
        self.history_box.config(state="disabled")
        self.history_box.see(tk.END)

    def add_to_details(self, details):
        self.details_box.config(state="normal")
        self.details_box.delete(1.0, tk.END)  
        self.details_box.insert(tk.END, details)
        self.details_box.config(state="disabled")

    def calcular_salario_bruto(self):
        valor_hora = float(simpledialog.askstring("Entrada", "Digite o valor da hora trabalhada: R$"))
        self.horas_trabalhadas = float(simpledialog.askstring("Entrada", "Digite o número de horas trabalhadas no mês: "))
        self.salario_bruto = calcular_salario_bruto(valor_hora, self.horas_trabalhadas)
        result = f"Salário Bruto: R$ {self.salario_bruto:.2f}"
        details = f"Salário Bruto = Valor Hora ({valor_hora}) * Horas Trabalhadas ({self.horas_trabalhadas})"
        messagebox.showinfo("Salário Bruto", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_horas_extras(self):
        horas_extras = float(simpledialog.askstring("Entrada", "Digite o número de horas extras trabalhadas: "))
        pagamento = calcular_horas_extras(self.salario_bruto, self.horas_trabalhadas, horas_extras)
        result = f"Horas Extras: R$ {pagamento:.2f}"
        details = f"Horas Extras = (Salário Bruto ({self.salario_bruto}) / Horas Trabalhadas ({self.horas_trabalhadas})) * Horas Extras ({horas_extras})"
        messagebox.showinfo("Horas Extras", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_inss(self):
        desconto = calcular_inss(self.salario_bruto)
        result = f"INSS: R$ {desconto:.2f}"
        details = f"INSS calculado conforme faixa salarial do salário bruto ({self.salario_bruto})"
        messagebox.showinfo("INSS", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_irrf(self):
        irrf = calcular_irrf(self.salario_bruto)
        result = f"IRRF: R$ {irrf:.2f}"
        details = f"IRRF calculado com base no salário bruto ({self.salario_bruto}) e dependentes"
        messagebox.showinfo("IRRF", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_ferias_proporcionais(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        ferias = calcular_férias_proporcionais(self.salario_bruto, meses_trabalhados)
        result = f"Férias Proporcionais: R$ {ferias:.2f}"
        details = f"Férias Proporcionais = (Salário Bruto ({self.salario_bruto}) / 12) * Meses Trabalhados ({meses_trabalhados})"
        messagebox.showinfo("Férias Proporcionais", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_13_salario(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        decimo_terceiro = calcular_13_salario(self.salario_bruto, meses_trabalhados)
        result = f"13º Salário: R$ {decimo_terceiro:.2f}"
        details = f"13º Salário = (Salário Bruto ({self.salario_bruto}) / 12) * Meses Trabalhados ({meses_trabalhados})"
        messagebox.showinfo("13º Salário", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_fgts(self):
        fgts = calcular_fgts(self.salario_bruto)
        result = f"FGTS: R$ {fgts:.2f}"
        details = f"FGTS = Salário Bruto ({self.salario_bruto}) * 0.08"
        messagebox.showinfo("FGTS", result)
        self.add_to_history(result)
        self.add_to_details(details)

    def calcular_rescisao(self):
        dias_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de dias trabalhados no mês: "))
        total_rescisao = calcular_rescisao(self.salario_bruto, dias_trabalhados)
        result = f"Rescisão: R$ {total_rescisao:.2f}"
        details = f"Rescisão = (Salário Bruto ({self.salario_bruto}) / 30) * Dias Trabalhados ({dias_trabalhados})"
        messagebox.showinfo("Rescisão", result)
        self.add_to_history(result)
        self.add_to_details(details)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.geometry("500x750")
    root.resizable(False, False)
    root.mainloop()
