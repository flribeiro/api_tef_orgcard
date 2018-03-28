from email.mime.text import MIMEText
import smtplib

def sendmail(nome_redecred, destinatarios, lojas):
    texto_mail_1 = """Prezados, boa tarde!

Seguem os dados para disponibilização da bandeira CONVENIOS CARD no TEF do {}.

Nome do módulo: ORGCARD

CNPJ                CODIGO""".format(nome_redecred)

    texto_mail_2 = """Obs.: Preencher o campo de código de estabelecimento com zeros à esquerda do código.

DTE: 0724 12172642241
Para SiTef GW a porta Orgcard na Software Express é 22046.
User Data: 3f 5f 5f 4e 5b 
A carga de bins é automática.
O módulo ORGCARD deve ser solicitado à Software Express."""
    
    for loja in lojas:
        texto_mail_1 += '\n{}     {}'.format(loja['cnpj'], loja['neu'])

    msg = MIMEText(texto_mail_1 + "\n\n" + texto_mail_2)
    msg['Subject'] = 'Ativação do módulo Orgcard no TEF do {}'.format(nome_redecred)
    msg['From'] = 'orgsysbackup@orgsystem.com.br'
    msg['To'] = ', '.join(destinatarios) + ', fabricio@orgsystem.com.br'

    try:
        s = smtplib.SMTP('smtp.gmail.com' + ':' + '587')
        s.starttls()
        s.login('orgsysbackup@orgsystem.com.br', '')
        s.send_message(msg)
        s.quit()
    except smtplib.SMTPException as e:
        msg = 'Não foi possível enviar o e-mail de notificação. Favor verificar configurações de e-mail:' + str(e)
        print(msg)
        exit()
