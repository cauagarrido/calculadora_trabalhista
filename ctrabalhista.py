import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from calculadora import *

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Trabalhista")

        
        master.configure(bg="#2E2E2E")
        self.history_text = tk.StringVar()
        
        self.salario_bruto = 0
        self.horas_trabalhadas = 0
        self.historico = []

        self.label = tk.Label(master, text="Calculadora Trabalhista", font=("Arial", 16), fg="#FFFFFF", bg="#2E2E2E")
        self.label.pack(pady=10)

       
        self.create_button("Calcular Salário Bruto", self.calcular_salario_bruto)
        self.create_button("Calcular Horas Extras", self.calcular_horas_extras)
        self.create_button("Calcular INSS", self.calcular_inss)
        self.create_button("Calcular IRRF", self.calcular_irrf)
        self.create_button("Calcular Férias Proporcionais", self.calcular_ferias_proporcionais)
        self.create_button("Calcular 13º Salário Proporcional", self.calcular_13_salario)
        self.create_button("Calcular FGTS", self.calcular_fgts)
        self.create_button("Calcular Rescisão", self.calcular_rescisao)
        self.create_button("Sair", master.quit)

        
        self.history_label = tk.Label(master, text="Histórico de Cálculos", fg="#FFFFFF", bg="#2E2E2E")
        self.history_label.pack(pady=5)
        
        self.history_box = scrolledtext.ScrolledText(master, width=40, height=10, bg="#444444", fg="#FFFFFF", state="disabled")
        self.history_box.pack(pady=5)

    def create_button(self, text, command):
        btn = tk.Button(self.master, text=text, command=command, bg="#4A4A4A", fg="#FFFFFF", font=("Arial", 10), width=30)
        btn.pack(pady=5)

    def add_to_history(self, message):
        self.historico.append(message)
        self.history_box.config(state="normal")
        self.history_box.insert(tk.END, message + "\n")
        self.history_box.config(state="disabled")
        self.history_box.see(tk.END)

    def calcular_salario_bruto(self):
        valor_hora = float(simpledialog.askstring("Entrada", "Digite o valor da hora trabalhada: R$"))
        self.horas_trabalhadas = float(simpledialog.askstring("Entrada", "Digite o número de horas trabalhadas no mês: "))
        self.salario_bruto = calcular_salario_bruto(valor_hora, self.horas_trabalhadas)
        result = f"Salário Bruto: R$ {self.salario_bruto:.2f}"
        messagebox.showinfo("Salário Bruto", result)
        self.add_to_history(result)

    def calcular_horas_extras(self):
        horas_extras = float(simpledialog.askstring("Entrada", "Digite o número de horas extras trabalhadas: "))
        pagamento = calcular_horas_extras(self.salario_bruto, self.horas_trabalhadas, horas_extras)
        result = f"Horas Extras: R$ {pagamento:.2f}"
        messagebox.showinfo("Horas Extras", result)
        self.add_to_history(result)

    def calcular_inss(self):
        desconto = calcular_inss(self.salario_bruto)
        result = f"INSS: R$ {desconto:.2f}"
        messagebox.showinfo("INSS", result)
        self.add_to_history(result)

    def calcular_irrf(self):
        irrf = calcular_irrf(self.salario_bruto)
        result = f"IRRF: R$ {irrf:.2f}"
        messagebox.showinfo("IRRF", result)
        self.add_to_history(result)

    def calcular_ferias_proporcionais(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        ferias = calcular_férias_proporcionais(self.salario_bruto, meses_trabalhados)
        result = f"Férias Proporcionais: R$ {ferias:.2f}"
        messagebox.showinfo("Férias Proporcionais", result)
        self.add_to_history(result)

    def calcular_13_salario(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        decimo_terceiro = calcular_13_salario(self.salario_bruto, meses_trabalhados)
        result = f"13º Salário: R$ {decimo_terceiro:.2f}"
        messagebox.showinfo("13º Salário", result)
        self.add_to_history(result)

    def calcular_fgts(self):
        fgts = calcular_fgts(self.salario_bruto)
        result = f"FGTS: R$ {fgts:.2f}"
        messagebox.showinfo("FGTS", result)
        self.add_to_history(result)

    def calcular_rescisao(self):
        dias_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de dias trabalhados no mês: "))
        total_rescisao = calcular_rescisao(self.salario_bruto, dias_trabalhados)
        result = f"Rescisão: R$ {total_rescisao:.2f}"
        messagebox.showinfo("Rescisão", result)
        self.add_to_history(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()