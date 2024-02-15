from customtkinter import *
import pyautogui as pg

my_width = pg.size().width
my_height = pg.size().height

print(my_width, my_height)

window = CTk(fg_color="black")
window.title("Calculadora de IMC")
window.geometry(f'{my_width}x{my_height}')


def fonte(nome_da_fonte, tamanho_da_fonte):
    return f"{nome_da_fonte}", tamanho_da_fonte


title_label = CTkLabel(window, text="Calculadora de IMC!",
                       text_color="white", font=fonte('Ubuntu', 30))
title_label.configure(pady=35)
title_label.pack()

result_label = CTkLabel(window, text="", text_color="gray",
                        width=200, font=fonte("Ubuntu", 15))
result_label.configure(pady=35)
result_label.pack()

weight_label = CTkLabel(window, text="Insira seu peso (em Kg)",
                        text_color='white', font=fonte("Ubuntu", 20))
weight_label.configure(pady=10)
weight_label.pack()

weight_entry = CTkEntry(window, width=200, bg_color="#d9d9d9")
weight_entry.pack()

height_label = CTkLabel(
    window, text="Insira sua altura (em cm)", text_color="white", font=fonte("Ubuntu", 20))
height_label.configure(pady=10)
height_label.pack()

height_entry = CTkEntry(window, width=200, bg_color="#d9d9d9")
height_entry.pack()


def calcular_imc():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())/100

        imc = weight / (height ** 2)

        if imc < 17:
            result_label.configure(
                text_color="red", text=f"Seu IMC é {imc:.2f} - Muito abaixo do peso ideal! Consulte um médico.")
            result_label.pack()

        elif imc >= 17 and imc < 18.49:
            result_label.configure(
                text_color="yellow", text=f"Seu IMC é {imc:.2f} - Abaixo do peso ideal!")
            result_label.pack()

        elif imc > 18.49 and imc <= 24.99:
            result_label.configure(
                text_color="green", text=f"Seu IMC é {imc:.2f} - Peso Ideal! Parabéns.")
            result_label.pack()

        elif imc > 24.99 and imc <= 29.99:
            result_label.configure(text_color="yellow",
                                   text=f"Seu IMC é {imc:.2f} - Acima do peso ideal")
            result_label.pack()

        elif imc > 29.99 and imc < 34.99:
            result_label.configure(text_color="orange",
                                   text=f"Seu IMC é {imc:.2f} - Obesidade nivel 1! Tome cuidado.")
            result_label.pack()

        elif imc > 34.99 and imc < 39.99:
            result_label.configure(
                text_color="#ff5300", text=f"Seu IMC é {imc:.2f} - Obesidade nivel 2 (severa). Consulte um médico.")
            result_label.pack()

        else:
            result_label.configure(
                text_color="red", text=f"Seu IMC é {imc:.2f} - Obesidade nivel 3! Consulte um médico imediatamente!")
            result_label.pack()
        # result_label.configure(text=f"Seu IMC é {imc:.2f}")
        # result_label.pack()

    except ValueError:
        result_label.configure(
            text_color="red", text="Por favor, insira valores numéricos.")
        result_label.pack()


calculate_button = CTkButton(window, font=fonte(
    'Ubuntu', 15), text="Calcular", text_color="white", border_spacing=10, width=200, command=calcular_imc)
calculate_button.pack_configure(side=TOP, pady=(10, 0))
calculate_button.pack()


window.mainloop()
