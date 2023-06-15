import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def Fechando():
    if messagebox.askyesno(title = "Saindo",  message = "Deseja fechar o programa?"):
        root.destroy()

def Repoem_bebidas(tipo_bebida):
    global doses
    global btn8
    if tipo_bebida == 'TODOS':
        for i in doses:
            doses[i] = 20
        btn8.config(bg= 'red')
    else:
        doses[tipo_bebida] = 20        
        if all( j != 0 for j in doses.values()):
            btn8.config(bg= 'red')
        
        else:
            btn8.config(bg= '#20fa20')
        
    print(doses)
            
def Barradefechar():
    global doses
    
    barra_de_ferramentas = tk.Menu(root)
    root.config(menu = barra_de_ferramentas)
    
    ferramentas_de_fechar = tk.Menu(barra_de_ferramentas, tearoff = 0)
    ferramentas_de_reposição = tk.Menu(barra_de_ferramentas, tearoff = 0)
    
    barra_de_ferramentas.add_cascade(menu = ferramentas_de_fechar, label = "Fechar Aplicativo")
    barra_de_ferramentas.add_cascade(menu = ferramentas_de_reposição, label = 'Realizar reposição')
    
    ferramentas_de_fechar.add_command(label = "Sair", command = Fechando)
    ferramentas_de_fechar.add_separator()
    ferramentas_de_fechar.add_command(label = "Sair sem perguntar", command = root.destroy)
    
    ferramentas_de_reposição.add_command(label = 'Café', command =lambda: Repoem_bebidas('CAFÉ'))
    ferramentas_de_reposição.add_separator()
    ferramentas_de_reposição.add_command(label = 'Leite', command =lambda: Repoem_bebidas('CAFÉ C/LEITE'))
    ferramentas_de_reposição.add_separator()
    ferramentas_de_reposição.add_command(label = 'MOCHACCINO', command =lambda: Repoem_bebidas('MOCHACCINO'))
    ferramentas_de_reposição.add_separator()
    ferramentas_de_reposição.add_command(label = 'Açucar', command =lambda: Repoem_bebidas('AÇUCAR'))
    ferramentas_de_reposição.add_separator()
    ferramentas_de_reposição.add_command(label = 'Encher todos', command =lambda: Repoem_bebidas('TODOS'))

def EscolheBebida(bebida):
    global tipo_de_bebida
    global buttons
    
    buttons[tipo_de_bebida].config(background="red")
    buttons[bebida].config(background="green")
    
    tipo_de_bebida = bebida
    
def EscolheTamanho(Tamanho):
    global tamanho_da_bebida
    global buttons
    
    buttons[tamanho_da_bebida].config(background="red")
    buttons[Tamanho].config(background="green")
    
    tamanho_da_bebida = Tamanho
    
    print(f'Bebida selecionada: {tamanho_da_bebida}')
    
def Com_Ou_Sem_Açucar(Condição):
    global Tem_açucar
    global buttons
    
    if Tem_açucar == False:
        buttons[Condição].config(background = 'green')
        Tem_açucar = True
    else:
        buttons[Condição].config(background = 'red')
        Tem_açucar = False
        
    print(f'Bebida selecionada: {Tem_açucar}')

def Diminui_Quantidade_Containers():
    global tamanho_da_bebida
    global tipo_de_bebida
    if Tem_açucar:
        
        if tamanho_da_bebida == 'PEQUENO':
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                doses['CAFÉ'] -= 1           
            doses[tipo_de_bebida] -= 1
            doses['AÇUCAR'] -= 1
        else:
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                doses['CAFÉ'] -= 2
            doses[tipo_de_bebida] -= 2
            doses['AÇUCAR'] -= 2 
    else:
        if tamanho_da_bebida == 'PEQUENO':
            doses[tipo_de_bebida] -= 1
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                doses['CAFÉ'] -= 1
        else:
            doses[tipo_de_bebida] -= 2
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                 doses['CAFÉ'] -= 2
   
def Verifica_Containers(olha_tipo,quantidade):
    global doses

    if quantidade == 'PEQUENO':
        if doses["AÇUCAR"] <= 0 and Tem_açucar == True:
            return True
        elif olha_tipo  == 'CAFÉ C/LEITE' and doses['CAFÉ'] <= 0:            
            return True
        elif doses[olha_tipo] <= 0:
            return True
        else:
            return False
    else:
        if doses["AÇUCAR"] <= 1 and Tem_açucar == True:
            return True
        elif olha_tipo  == 'CAFÉ C/LEITE' and doses['CAFÉ'] <= 1:            
            return True
        elif doses[olha_tipo] <= 1:
            return True
        else:
            return False    

def gera_cupom_fiscal(tipo_de_bebida,com_ou_sem_açucar,tamanho_da_bebida):
    valor = 0
    if tipo_de_bebida == 'CAFÉ':
        valor += 1.00
    elif tipo_de_bebida == 'CAFÉ C/LEITE':
        valor += 2.00
    else:
        valor += 3.00
    if tamanho_da_bebida == 'PEQUENO':
        valor +=2.00
    else:
        valor += 4.00
            
    if not com_ou_sem_açucar:
        float(valor)
        cupom_fiscal = open ("cupom-fiscal.txt","w")
        cupom_fiscal.write(f'''/--------------------Cupom fiscal--------------------\\
|                                                    
|                                                    
|       Babida: {tipo_de_bebida}                     
|       Tamanho do copo: {tamanho_da_bebida}         
|       Açucar: Sem Açucar                           
|       Preço:R$ {valor}                                       
|                                                    
|                                                    
\____________________________________________________/''')
        cupom_fiscal.close()
        print('criado')
    if com_ou_sem_açucar:
        valor = float(valor) + float(0.25)
        cupom_fiscal = open ("cupom-fiscal.txt","w")
        cupom_fiscal.write(f'''/--------------------Cupom fiscal--------------------\\
|                                                   
|                                                    
|       Babida: {tipo_de_bebida}                     
|       Tamanho do copo: {tamanho_da_bebida}         
|       Açucar: Com Açucar                           
|       Preço:  {valor}                              
|                                                    
|                                                   
\____________________________________________________/''')
        cupom_fiscal.close()

def Preparar_O_Café():
    global tipo_de_bebida
    global tamanho_da_bebida
    global Tem_açucar
    global doses
    global preparando
    global tempo_total
    
    if not preparando:
        preparando = True
        
        tempo_preparo =0
        
        if Verifica_Containers(tipo_de_bebida,tamanho_da_bebida):
            messagebox.showerror(title = 'Reposição Requisitada', message = f"""Doses de  Café restante: {doses['CAFÉ']} 
    Doses de  Leite restante: {doses['CAFÉ C/LEITE']}
    Doses de  Mochaccino restante: {doses['MOCHACCINO']}
    Doses de  Açucar restante: {doses['AÇUCAR']}
    
    Necessario Reposição para a opção escolhida, Fale com algum responsavel pela manutenção""")
            btn8.config(bg = '#20fa20')
            
            
            
        
        elif tamanho_da_bebida == 'PEQUENO':   
            Diminui_Quantidade_Containers()
            tempo_preparo += 6
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                tempo_preparo +=1
            if Tem_açucar:
                tempo_preparo += 1
            
        else:                   #'Grande'
            Diminui_Quantidade_Containers()
            tempo_preparo +=12
            if tipo_de_bebida == 'CAFÉ C/LEITE':
                tempo_preparo +=2      
            if Tem_açucar:
                tempo_preparo += 2
        
        tempo_total = tempo_preparo
            
        print(doses)    
        print(f"{tempo_preparo} Segundo")
        barra_de_carregar(tempo_total)
        gera_cupom_fiscal(tipo_de_bebida,Tem_açucar,tamanho_da_bebida)
    
    
def barra_de_carregar(tempo):
    barra_de_progresso = ttk.Progressbar(root, orient= 'horizontal', length= 300, mode = 'determinate')
    barra_de_progresso.grid(sticky = 'S')
    
    porcentagem_da_barra = tk.Label(framebtns, bg = 'gray')
    porcentagem_da_barra.grid(row = 9 , column= 0, sticky = tk.W+tk.E)
    porcentagem_da_barra = tk.Label(framebtns, bg = 'gray', text = f"Tempo de espera estimado: {tempo} segundos", font = ('arial', 12))
    porcentagem_da_barra.grid(row = 10 , column= 0, sticky = tk.W+tk.E)
    
    atualiza_barra(tempo, barra_de_progresso, porcentagem_da_barra)
    
def atualiza_barra(tempo, barra_de_progresso, porcentagem_da_barra):
    global preparando
    
    if tempo > 0:
        barra_de_progresso['value'] = 100 * (tempo_total - tempo)/tempo_total
        porcentagem_da_barra.config(text=f"Tempo de espera estimado: {tempo} segundos" )
        tempo -= 1
        root.after(1000, lambda: atualiza_barra(tempo, barra_de_progresso, porcentagem_da_barra))
        
    else:
        porcentagem_da_barra.destroy()
        barra_de_progresso.destroy()
        barra_final = tk.Label(framebtns, bg = 'gray', text = 'Café pronto!', font = ('arial',12))
        barra_final.grid(row = 10 , column= 0, sticky = tk.W+tk.E)
        
        preparando = False
    
    
#Config default --> Café Sem leite, Pequeno, Sem Açucar
#Doses MOCHACCINO, é o container de Mochaccino
#Doses CAFÉ C/LEITE, é o container de leite

 
tempo_total = 0
preparando = False
Tem_açucar = False
tamanho_da_bebida = 'PEQUENO'
tipo_de_bebida = 'CAFÉ'
buttons = {}
doses = {}

root = tk.Tk()
root.title("Cafeteira")
root.geometry("950x700")
root. config(bg= 'black')
#root.protocol("WM_DELETE_WINDOW", Fechando)



Barradefechar()
root.columnconfigure(0, weight = 1)

framebtns = tk.Frame(root)
framebtns.grid(row = 0, column=0, pady = 75)

framcafe = tk.Frame(framebtns, background= "gray")
framcafe.grid(row = 0, column=0)

btn1 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), bg = "green", activebackground = "yellow", command =lambda: [EscolheBebida('CAFÉ')])
btn1.grid(row = 0, column = 0, sticky= tk.W, padx=10, pady = 5)
buttons['CAFÉ'] = btn1
doses['CAFÉ'] = 20

texto1 = tk.Label(framcafe, text = "CAFÉ", font = ("Arial", 12),bg= 'gray')
texto1.grid(row = 0, column=1, sticky= "W")

btn2 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow", command =lambda: EscolheBebida('CAFÉ C/LEITE'))
btn2.grid(row = 1, column = 0, sticky = "E", padx=10, pady = 5)
buttons['CAFÉ C/LEITE'] = btn2
doses['CAFÉ C/LEITE'] = 20

texto2 = tk.Label(framcafe, text = "CAFÉ C/LEITE", font = ("Arial", 12), bg= 'gray')
texto2.grid(row = 1, column=1, sticky= "W")

btn3 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow", command =lambda: EscolheBebida('MOCHACCINO'))
btn3.grid(row = 2, column = 0, sticky = "E", padx=10, pady = 5)
buttons['MOCHACCINO'] = btn3
doses['MOCHACCINO'] = 20

texto3 = tk.Label(framcafe, text = "MOCHACCINO", font = ("Arial", 12), bg= 'gray')
texto3.grid(row = 2, column=1, sticky= "W")

btn4 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "green", activebackground = "yellow", command =lambda: EscolheTamanho('PEQUENO'))
btn4.grid(row = 3, column = 0, sticky= "E", padx=10, pady = 5)
buttons['PEQUENO'] = btn4

texto4 = tk.Label(framcafe, text = "PEQUENO", font = ("Arial", 12), bg= 'gray')
texto4.grid(row = 3, column=1, sticky= "W")

btn5 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow", command =lambda: EscolheTamanho('GRANDE'))
btn5.grid(row = 4, column = 0, sticky= "E", padx=10, pady = 5)
buttons['GRANDE'] = btn5

texto5 = tk.Label(framcafe, text = "GRANDE", font = ("Arial", 12), bg= 'gray')
texto5.grid(row = 4, column=1, sticky= "W")

btn6 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow", command =lambda: Com_Ou_Sem_Açucar('AÇUCAR'))
btn6.grid(row = 5, column = 0, sticky= "E", padx=10, pady = 5)
buttons['AÇUCAR'] = btn6
doses['AÇUCAR'] = 20

texto6 = tk.Label(framcafe, text = "AÇUCAR", font = ("Arial", 12), bg= 'gray')
texto6.grid(row = 5, column=1, sticky= "W")

btn7 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow", command =lambda: Preparar_O_Café())
btn7.grid(row = 6, column = 0, sticky= "E", padx=10, pady = 5)
buttons['PREPARO'] = btn6

texto7 = tk.Label(framcafe, text = "PREPARO", font = ("Arial", 12), bg= 'gray')
texto7.grid(row = 6, column=1, sticky= "W")

btn8 = tk.Button(framcafe, text = "         ", font = ("Arial", 15), background = "red", activebackground = "yellow")
btn8.grid(row = 7, column = 0, sticky= "E", padx=10, pady = 5)
texto8 = tk.Label(framcafe, text = "REPOSIÇÃO NECESSARIA", font = ("Arial", 12), bg= 'gray')
texto8.grid(row = 7, column=1, sticky= "W")
btn8.config(state = 'disabled') 


root.mainloop()
