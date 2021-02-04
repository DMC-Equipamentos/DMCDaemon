# DAEMOM DMC

Processo da DMC para instalção de software em produção.

Para instalar é necessária a instalação de todas as dependências do python e de outros gravadores.

Os arquivos necessários para instalaçoes das dependências podem ser acessados internamente em 192.168.2.164/dependencias/

## Instalação do python

Esse processo utiliza o python 3.8, no ubuntu basta instalar com o apt, no windows, o arquivo de instalação se encontra nas dependências

## Dependências do python

Para instalar deve ser feito um:

```
pip install -r requirements.txt
```

Está disponível um arquivo executável para fazer isso, no windows: install-requirements.bat, no ubuntu install-requirements.sh

## Arquivo de configuração

Existem dois arquivos de configuraçao disponíveis para os sistemas operacionais. Deve-se escolher o adequado e renomear para config.py

## Dependências de gravadores

### MPLAB IPE

#### No windows

O arquivo de instalação se encontra no diretório de dependencias e deve ser instalado. Durante a instalação, pode-se desmarcar a opção de instalar o IDE, apenas o IPE é suficiente.


#### No ubuntu

O arquivo de instalação tbm se encontra na pasta e deve ser executado com permissão de root, deve se proceder como no windows. Deve-se proceder como no windows.

#### Verificar config

Deve-se garantir que o caminho para o executável no arquivo de configuração está correto, deve-se também alterar o gravador para o que a pessoa utiliza no computador. 

### NINA JTAG

O arquivo para instalação do JLinkExe se encontra na pasta de dependências, tanto para linux quanto para windows. Depois deve-se confirmar co caminho no arquivo de configuraçoes.

### AVRDUDE

#### No windows

Deve-se instalar o WinAVR, ele já é instalado no PATH, então o arquivo de config não precisa ser alterado

#### No ubuntu

```
sudo apt install avrdude
```
