import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
from datetime import datetime

# Dados do programa
lista_carros = [
    "Fiat Mobi", "Fiat Argo", "Fiat Pulse", "Fiat Cronos", "Fiat Strada", "Fiat Fastback", "Fiat Fiorino",
    "Fiat Toro", "Fiat Titano", "Chevrolet S10", "Chevrolet Silverado", "Chevrolet Equinox", "Chevrolet Captiva",
    "Chevrolet Spark", "Chevrolet Montana", "Chevrolet Tracker", "Chevrolet Spin", "Chevrolet Onix",
    "Chevrolet Trailblazer", "Toyota Yaris", "Toyota Yaris Cross", "Toyota Corolla", "Toyota Corolla Cross",
    "Toyota Hilux", "Toyota Rav4", "Toyota Gr Yaris", "Toyota Gr Corolla", "Toyota Hilux Sw4", "Hyundai Hb20",
    "Hyundai Hb20s", "Hyundai Creta", "Hyundai Tucson", "Hyundai Palisade", "Hyundai Kona", "Volkswagen Polo",
    "Volkswagen Tera", "Volkswagen Saveiro", "Volkswagen Virtus", "Volkswagen Nivus", "Volkswagen T-Cross",
    "Volkswagen Jetta", "Volkswagen Tiguan", "Volkswagen Amarok", "Jeep Renegade", "Jeep Compass", "Jeep Commander",
    "Jeep Gladiator", "Jeep Wrangler", "Renault Kwid", "Renault Logan", "Renault Kwid E-Tech", "Renault Duster",
    "Honda City", "Honda Wr-V", "Honda Hr-V", "Honda Civic", "Honda Accord", "Honda Crv", "Nissan Kicks",
    "Nissan Versa", "Nissan Sentra", "Nissan Frontier", "Peugeot 208", "Peugeot 2008", "Citroen C3", "Citroen Basalt",
    "Ford Maverick", "Ford Territory", "Ford Ranger", "Ford F-150", "Ford Mustang"
]

lista_bancos = ["Banco do Brasil", "Bradesco", "Caixa Econômica", "Itaú", "Santander"]

precos = {
    "Fiat Mobi": 85990,
    "Fiat Argo": 111990,
    "Fiat Pulse": 162490,
    "Fiat Cronos": 124990,
    "Fiat Strada": 151990,
    "Fiat Fastback": 183990,
    "Fiat Fiorino": 130990,
    "Fiat Toro": 235490,
    "Fiat Titano": 285990,
    "Chevrolet S10": 348790,
    "Chevrolet Silverado": 483990,
    "Chevrolet Equinox": 349990,
    "Chevrolet Captiva": 291190,
    "Chevrolet Spark": 154990,
    "Chevrolet Montana": 171390,
    "Chevrolet Tracker": 119900,
    "Chevrolet Spin": 165590,
    "Chevrolet Onix": 139390,
    "Chevrolet Trailblazer": 422590,
    "Toyota Yaris": 135090,
    "Toyota Yaris Cross": 189990,
    "Toyota Corolla": 206990,
    "Toyota Corolla Cross": 222690,
    "Toyota Hilux": 357890,
    "Toyota Rav4": 349290,
    "Toyota Gr Yaris": 354990,
    "Toyota Gr Corolla": 399990,
    "Toyota Hilux Sw4": 475990,
    "Hyundai Hb20": 132490,
    "Hyundai Hb20s": 138890,
    "Hyundai Creta": 206990,
    "Hyundai Tucson": 199490,
    "Hyundai Palisade": 479990,
    "Hyundai Kona": 239990,
    "Volkswagen Polo": 138690,
    "Volkswagen Tera": 146190,
    "Volkswagen Saveiro": 134190,
    "Volkswagen Virtus": 176690,
    "Volkswagen Nivus": 189690,
    "Volkswagen T-Cross": 203490,
    "Volkswagen Jetta": 278490,
    "Volkswagen Tiguan": 299990,
    "Volkswagen Amarok": 399890,
    "Jeep Renegade": 189490,
    "Jeep Compass": 278990,
    "Jeep Commander": 329990,
    "Jeep Gladiator": 529990,
    "Jeep Wrangler": 529990,
    "Renault Kwid": 89090,
    "Renault Logan": 101000,
    "Renault Kwid E-Tech": 99990,
    "Renault Duster": 171990,
    "Honda City": 155300,
    "Honda Wr-V": 155300,
    "Honda Hr-V": 214000,
    "Honda Civic": 430500,
    "Honda Accord": 333000,
    "Honda Crv": 353500,
    "Nissan Kicks": 199000,
    "Nissan Versa": 146490,
    "Nissan Sentra": 198790,
    "Nissan Frontier": 317990,
    "Peugeot 208": 138990,
    "Peugeot 2008": 184990,
    "Citroen C3": 112590,
    "Citroen Basalt": 129890,
    "Ford Maverick": 239900,
    "Ford Territory": 219900,
    "Ford Ranger": 499000,
    "Ford F-150": 580000,
    "Ford Mustang": 649000
}

juros = {
    "Banco do Brasil": 0.0207,
    "Bradesco": 0.0174,
    "Caixa Econômica": 0.0197,
    "Itaú": 0.0212,
    "Santander": 0.0190
}

# Agrupar carros por marca
separados = defaultdict(list)
for carro in lista_carros:
    marca = carro.split()[0]
    separados[marca].append(carro)

marcas_disponiveis = sorted(separados.keys())


class FinanciamentoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Financiamento de Carros")
        self.root.geometry("720x620")
        self.root.resizable(False, False)

        self.marca_selecionada = tk.StringVar()
        self.modelo_selecionado = tk.StringVar()
        self.banco_selecionado = tk.StringVar()
        self.parcelas_var = tk.IntVar(value=60)
        self.tipo_financiamento = tk.StringVar(value="Price")

        self.criar_interface()

    def criar_interface(self):
        main_frame = ttk.Frame(self.root, padding="16")
        main_frame.pack(fill=tk.BOTH, expand=True)

        titulo = ttk.Label(main_frame, text="SIMULADOR DE FINANCIAMENTO", font=("Arial", 18, "bold"))
        titulo.pack(pady=(0, 16))

        campos_frame = ttk.Frame(main_frame)
        campos_frame.pack(fill=tk.X, pady=(0, 10))
        campos_frame.columnconfigure(1, weight=1)
        campos_frame.columnconfigure(2, weight=1)

        ttk.Label(campos_frame, text="1. Marca:", font=("Arial", 11, "bold")).grid(row=0, column=0, sticky="w", pady=4)
        self.marca_combo = ttk.Combobox(campos_frame, textvariable=self.marca_selecionada, values=marcas_disponiveis, state="readonly", width=40)
        self.marca_combo.grid(row=0, column=1, sticky="ew", padx=6, columnspan=2)
        self.marca_combo.bind("<<ComboboxSelected>>", self.atualizar_modelos)

        ttk.Label(campos_frame, text="2. Modelo:", font=("Arial", 11, "bold")).grid(row=1, column=0, sticky="w", pady=4)
        self.modelo_combo = ttk.Combobox(campos_frame, textvariable=self.modelo_selecionado, state="readonly", width=40)
        self.modelo_combo.grid(row=1, column=1, sticky="w", padx=6)
        self.modelo_combo.bind("<<ComboboxSelected>>", self.atualizar_preco)

        ttk.Label(campos_frame, text="3. Banco:", font=("Arial", 11, "bold")).grid(row=2, column=0, sticky="w", pady=4)
        self.banco_combo = ttk.Combobox(campos_frame, textvariable=self.banco_selecionado, values=lista_bancos, state="readonly", width=40)
        self.banco_combo.grid(row=2, column=1, sticky="w", padx=6)

        ttk.Label(campos_frame, text="4. Parcelas:", font=("Arial", 11, "bold")).grid(row=3, column=0, sticky="w", pady=4)
        spin_parcelas = tk.Spinbox(campos_frame, from_=20, to=120, textvariable=self.parcelas_var, width=10, command=self.atualizar_parcela_valor)
        spin_parcelas.grid(row=3, column=1, sticky="w", padx=6)
        self.parcelas_label = ttk.Label(campos_frame, text="60 parcelas selecionadas", font=("Arial", 10), wraplength=260, justify="left")
        self.parcelas_label.grid(row=3, column=2, sticky="w", padx=20)

        ttk.Label(campos_frame, text="5. Tipo:", font=("Arial", 11, "bold")).grid(row=4, column=0, sticky="w", pady=4)
        tipo_frame = ttk.Frame(campos_frame)
        tipo_frame.grid(row=4, column=1, sticky="w", padx=6)
        ttk.Radiobutton(tipo_frame, text="Price", variable=self.tipo_financiamento, value="Price", command=self.atualizar_parcela_valor).pack(side=tk.LEFT)
        ttk.Radiobutton(tipo_frame, text="Sac", variable=self.tipo_financiamento, value="Sac", command=self.atualizar_parcela_valor).pack(side=tk.LEFT, padx=(12, 0))

        preco_frame = ttk.Frame(main_frame)
        preco_frame.pack(fill=tk.X, pady=(10, 10))
        ttk.Label(preco_frame, text="Preço do carro:", font=("Arial", 11, "bold")).pack(side=tk.LEFT)
        self.preco_label = ttk.Label(preco_frame, text="R$ 0,00", font=("Arial", 12, "bold"), foreground="green")
        self.preco_label.pack(side=tk.LEFT, padx=8)

        ttk.Button(main_frame, text="Calcular Financiamento", command=self.calcular_financiamento).pack(fill=tk.X, pady=(10, 0))

        resultado_frame = ttk.LabelFrame(main_frame, text="Resultado", padding="12")
        resultado_frame.pack(fill=tk.BOTH, expand=True, pady=(12, 0))
        self.resultado_text = tk.Text(resultado_frame, height=16, state=tk.DISABLED, wrap=tk.WORD)
        self.resultado_text.pack(fill=tk.BOTH, expand=True)

        self.atualizar_parcela_valor()

    def atualizar_modelos(self, event=None):
        marca = self.marca_selecionada.get()
        if marca in separados:
            modelos = sorted(separados[marca])
            self.modelo_combo['values'] = modelos
            self.modelo_selecionado.set("")
            self.preco_label.config(text="R$ 0,00")
            self.resultado_text.config(state=tk.NORMAL)
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.config(state=tk.DISABLED)
        else:
            self.modelo_combo['values'] = []

    def atualizar_preco(self, event=None):
        modelo = self.modelo_selecionado.get()
        if modelo in precos:
            valor = precos[modelo]
            self.preco_label.config(text=f"R$ {valor:,.2f}")
        else:
            self.preco_label.config(text="R$ 0,00")
        self.atualizar_parcela_valor()

    def atualizar_parcela_valor(self, *args):
        modelo = self.modelo_selecionado.get()
        parcelas = self.parcelas_var.get()
        if modelo in precos and 20 <= parcelas <= 120:
            valor = precos[modelo]
            valor_parcela = valor / parcelas
            self.parcelas_label.config(text=f"{parcelas} parcelas selecionadas — referência: R$ {valor_parcela:,.2f} por parcela")
        else:
            self.parcelas_label.config(text=f"{parcelas} parcelas selecionadas")

    def calcular_financiamento(self):
        marca = self.marca_selecionada.get()
        modelo = self.modelo_selecionado.get()
        banco = self.banco_selecionado.get()
        parcelas = self.parcelas_var.get()
        tipo = self.tipo_financiamento.get()

        if not marca:
            messagebox.showerror("Erro", "Escolha uma marca.")
            return
        if not modelo:
            messagebox.showerror("Erro", "Escolha um modelo.")
            return
        if modelo not in precos:
            messagebox.showerror("Erro", "Modelo inválido.")
            return
        if banco not in lista_bancos:
            messagebox.showerror("Erro", "Escolha um banco válido.")
            return
        if parcelas < 20 or parcelas > 120:
            messagebox.showerror("Erro", "Parcelas devem ficar entre 20 e 120.")
            return

        valor = precos[modelo]
        taxa = juros[banco]
        data_final = self.calcular_data_final(parcelas)

        if tipo == "Price":
            parcela_valor = self.calcular_price(valor, taxa, parcelas)
            total = parcela_valor * parcelas
            juros_totais = total - valor
            primeira = ultima = parcela_valor
            metodo = "Price"
        else:
            prestacoes = self.calcular_sac(valor, taxa, parcelas)
            total = sum(prestacoes)
            juros_totais = total - valor
            primeira = prestacoes[0]
            ultima = prestacoes[-1]
            metodo = "Sac"

        resultado = (
            f"Tipo de financiamento: {metodo}\n"
            f"Marca: {marca}\n"
            f"Modelo: {modelo}\n"
            f"Banco: {banco}\n"
            f"Taxa mensal: {taxa*100:.2f}%\n"
            f"Parcelas: {parcelas}x\n"
            f"Data final: {data_final}\n"
            f"Preço do carro: R$ {valor:,.2f}\n"
            f"Primeira parcela: R$ {primeira:,.2f}\n"
            f"Última parcela: R$ {ultima:,.2f}\n"
            f"Total pago: R$ {total:,.2f}\n"
            f"Total de juros: R$ {juros_totais:,.2f}\n"
        )

        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, resultado)
        self.resultado_text.config(state=tk.DISABLED)

    def calcular_price(self, valor, taxa, parcelas):
        return valor * taxa / (1 - (1 + taxa) ** (-parcelas))

    def calcular_sac(self, valor, taxa, parcelas):
        amortizacao = valor / parcelas
        saldo_devedor = valor
        prestacoes = []
        for _ in range(parcelas):
            juros_parcela = taxa * saldo_devedor
            prestacao = amortizacao + juros_parcela
            prestacoes.append(prestacao)
            saldo_devedor -= amortizacao
        return prestacoes

    def calcular_data_final(self, parcelas):
        agora = datetime.now()
        mes_final = agora.month + parcelas
        ano_final = agora.year + (mes_final - 1) // 12
        mes_final = ((mes_final - 1) % 12) + 1
        return f"{mes_final:02d}/{ano_final}"


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanciamentoGUI(root)
    root.mainloop()
