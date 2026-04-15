""" 
Módulo SMTPLIB

Define um objeto de sessão do cliente SMTP que pode ser usado a fim de enviar e-mail para qualquer
máquina da internet com um serviço de processamento SMTP ou ESMTP. O exemplo a seguir vai permitir
que você envie um e-mail a partir do servidor SMTP do Gmail.


Como a Google não permite, por padrão, realizar o login com a utilização do smtplib por considerar
esse tipo de conexão mais arriscada, será necessário alterar uma configuração de segurança. Para resolver
isso, siga as instruções a seguir.


Acesse sua conta no Google.

Depois acesse Segurança.

Acesso a app menos seguro. (Atenção! Em algumas contas, os nomes estarão escritos no
idioma inglês - allow less secure apps).

Mude para "ativada" a opção de "Permitir aplicativos menos seguros".

Para fazer seu primeiro envio, crie um programa no seu projeto. O código a seguir mostra as importações
necessárias para o envio. Confira!

#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

O código seguinte mostra a criação da mensagem com o corpo e os seus parâmetros.

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

Agora, vamos analisar o código.


A linha 2 mostra a criação de um objeto de mensagem.

A linha 3 exibe o corpo da mensagem em uma string.

As linhas de 6 a 9 devem ser preenchidas com os valores adequados para que seu programa seja executado com sucesso.

A linha 12 anexa o corpo da mensagem (que estava em uma string) ao objeto msg.

O próximo código mostra os passos necessários para o próprio envio. Conheça!

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()
print('Mensagem enviada com sucesso')

A seguir, faremos análise do código.

As linhas 2 e 3 mostram a criação do servidor e a sua conexão no modo TLS.

A linha 6 mostra o login na conta de origem do e-mail.

A linha 9 representa o envio propriamente dito.

A linha 12 exibe o encerramento do servidor.

O código referente ao programa para o envio de e-mail a partir do servidor SMTP do Gmail
encontra-se no arquivo disponibilizado neste conteúdo (código 28).

Módulo time

Provê diversas funções relacionadas a tempo. Também pode ser útil conhecer os módulos datetime e calendar.

Esta tabela aponta algumas das principais funções disponíveis no módulo time, confira!

Função	| Retorno
time() |	Número de segundos passados desde o início da
contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de
janeiro de 1970.

ctime(segundos) |	Uma string representando o
horário local, calculado a partir do número de segundos passado como
parâmetro.

gmtime(segundos) |	Converte o número de segundos em um objeto struct_time descrito a seguir.

localtime(segundos)	Semelhante à gmtime() , mas
converte para o horário local.

sleep(segundos) |	A função suspende a execução por determinado
número de segundos.

O código a seguir (código 23 no arquivo disponibilizado)
mostra um exemplo de chamada das funções time() e ctime().

import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

Veremos a seguir o resultado.


A variável x recebe o número de segundos desde 00:00:00 de 01/01/1970 pela função time(). Ao executar ctime(x), o número de segundos armazenado em x é convertido em uma string com o horário local.

A classe time.struct_time gera objetos sequenciais com valor de tempo retornado pelas funções gmtime() e localtime(). São objetos com interface de tupla nomeada: os valores podem ser acessados pelo índice e pelo nome do atributo.

Aparecem os seguintes valores:


Índice	Atributo	Valores
0	tm_year	Por exemplo, 2020
1	tm_mon	range [1, 12]
2	tm_mday	range [1, 31]
3	tm_hour	range [0, 23]
4	tm_min	range [0, 59]
5	tm_sec	range [0, 61]
6	tm_wday	range [0, 6] Segunda-feira é 0
7	tm_yday	range [1, 366]
8	tm_isdst	0,1 ou -1
N/A	tm_zone	Abreviação do nome da timezone

Principais funções do módulo time.
Humberto Henriques de Arruda.


Para mais informações sobre o módulo time, visite a biblioteca Python.


Módulo tkinter

O pacote tkinter é a interface Python padrão para o Tk GUI (interface gráfica com o usuário) toolkit.
Na maioria dos casos, basta importar o próprio tkinter, mas diversos outros módulos estão disponíveis no pacote.


A biblioteca tkinter permite a criação de janelas com elementos gráficos, como a entrada de dados e botões,
por exemplo.


O exemplo a seguir vai permitir que você crie a primeira janela com alguns elementos.
Para isso, crie um programa novo no seu projeto. O código adiante mostra a criação da sua primeira janela,
ainda sem qualquer elemento gráfico.

from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.mainloop()

Agora, veremos a análise do código.


A linha 1 mostra a importação de todos os elementos disponíveis em tkinter.
O objeto janelaPrincipal é do tipo Tk. Um objeto Tk é um elemento que representa a janela GUI.
Para que essa janela apareça, é necessário chamar o método mainloop();

Para exibir textos, vamos usar o elemento Label. O próximo código mostra as linhas 4 e 5,
com a criação do elemento e o seu posicionamento. O tamanho padrão da janela é 200 X 200 pixels,
com o canto superior esquerdo de coordenadas (0,0) e o inferior direito de coordenadas (200,200).

Observe agora a primeira janela com tkinter 2.

from tkinter import *

janelaPrincipal = Tk()
texto Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.place(x = 50 y = 100)
janelaPrincipal.mainloop()

Vamos agora incrementar um pouco essa janela. Para isso, acrescentaremos uma imagem e um botão.
A imagem precisa estar na mesma pasta do seu arquivo .py.


Confira o código da segunda janela com tkinter.

from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="logoEstacio.gif")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()

A seguir, analisaremos o código.


No código, há a inserção do elemento de imagem e o botão. Nas linhas 10, 11 e 12,
é feita a criação do objeto Label para conter a imagem e seu posicionamento.
Observe que passamos a utilizar o método pack(), que coloca o elemento centralizado
e posicionado o mais perto possível do topo, depois dos elementos posicionados anteriormente.

O elemento botão é criado na linha 14 com os atributos text e command, os quais são respectivamente o texto exibido no corpo do botão e a função a ser executada quando o botão é clicado.

Para o funcionamento correto do botão, é preciso definir a função funcClicar(), nas linhas 3 e 4.

"""