import tkinter as tk
from tkinter import messagebox, simpledialog
from calculadora import *  

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Trabalhista")

        self.salario_bruto = 0
        self.horas_trabalhadas = 0

        self.label = tk.Label(master, text="Calculadora Trabalhista", font=("Arial", 16))
        self.label.pack(pady=10)

        self.btn_salario_bruto = tk.Button(master, text="Calcular Salário Bruto", command=self.calcular_salario_bruto)
        self.btn_salario_bruto.pack(pady=5)

        self.btn_horas_extras = tk.Button(master, text="Calcular Horas Extras", command=self.calcular_horas_extras)
        self.btn_horas_extras.pack(pady=5)

        self.btn_inss = tk.Button(master, text="Calcular INSS", command=self.calcular_inss)
        self.btn_inss.pack(pady=5)

        self.btn_irrf = tk.Button(master, text="Calcular IRRF", command=self.calcular_irrf)
        self.btn_irrf.pack(pady=5)

        self.btn_rescisao = tk.Button(master, text="Calcular Rescisão", command=self.calcular_rescisao)
        self.btn_rescisao.pack(pady=5)

        self.btn_ferias = tk.Button(master, text="Calcular Férias Proporcionais", command=self.calcular_ferias_proporcionais)
        self.btn_ferias.pack(pady=5)

        self.btn_decimo_terceiro = tk.Button(master, text="Calcular 13º Salário Proporcional", command=self.calcular_13_salario)
        self.btn_decimo_terceiro.pack(pady=5)

        self.btn_fgts = tk.Button(master, text="Calcular FGTS", command=self.calcular_fgts)
        self.btn_fgts.pack(pady=5)

        self.btn_sair = tk.Button(master, text="Sair", command=master.quit)
        self.btn_sair.pack(pady=5)

    def calcular_salario_bruto(self):
        valor_hora = float(simpledialog.askstring("Entrada", "Digite o valor da hora trabalhada: R$"))
        self.horas_trabalhadas = float(simpledialog.askstring("Entrada", "Digite o número de horas trabalhadas no mês: "))
        self.salario_bruto = calcular_salario_bruto(valor_hora, self.horas_trabalhadas)
        messagebox.showinfo("Salário Bruto", f"O salário bruto é: R$ {self.salario_bruto:.2f}")

    def calcular_horas_extras(self):
        horas_extras = float(simpledialog.askstring("Entrada", "Digite o número de horas extras trabalhadas: "))
        pagamento = calcular_horas_extras(self.salario_bruto, self.horas_trabalhadas, horas_extras)
        messagebox.showinfo("Horas Extras", f"O pagamento total por horas extras é: R$ {pagamento:.2f}")

    def calcular_inss(self):
        desconto = calcular_inss(self.salario_bruto)
        messagebox.showinfo("INSS", f"O desconto do INSS é: R$ {desconto:.2f}")

    def calcular_irrf(self):
        irrf = calcular_irrf(self.salario_bruto)
        messagebox.showinfo("IRRF", f"O desconto de IRRF é: R$ {irrf:.2f}")

    def calcular_ferias_proporcionais(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        ferias = calcular_férias_proporcionais(self.salario_bruto, meses_trabalhados)
        messagebox.showinfo("Férias Proporcionais", f"O valor das férias proporcionais é: R$ {ferias:.2f}")

    def calcular_13_salario(self):
        meses_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de meses trabalhados: "))
        decimo_terceiro = calcular_13_salario(self.salario_bruto, meses_trabalhados)
        messagebox.showinfo("13º Salário", f"O valor do 13º salário proporcional é: R$ {decimo_terceiro:.2f}")

    def calcular_fgts(self):
        fgts = calcular_fgts(self.salario_bruto)
        messagebox.showinfo("FGTS", f"O valor do FGTS é: R$ {fgts:.2f}")

    def calcular_rescisao(self):
        dias_trabalhados = int(simpledialog.askstring("Entrada", "Digite o número de dias trabalhados no mês: "))
        total_rescisao = calcular_rescisao(self.salario_bruto, dias_trabalhados)
        messagebox.showinfo("Rescisão", f"Total de rescisão: R$ {total_rescisao:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
