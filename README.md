# DAEMOM DMC

Processo da DMC para instalção de software em produção.

Para instalar é necessária a instalação de todas as dependências do python e de outros gravadores.

Os arquivos necessários para instalaçoes das dependências podem ser acessados internamente em 192.168.2.164/dependencias/

# Procedimento para instalação no windows no Windows

- Acessar a URL: http://gravarplacas.dmcgroup.com.br/dependencias/Windows/

- Baixar Todos os arquivos.

- Instalar o PYTHON (Rodar o executável duas vezes, garantir que foi instalado o PIP e que o python foi adicionado as variáveis de sistema)

- Instalar o GIT (garantir tbm que foi adicionado as variáveis de ambiente)

- executar o arquivo: baixar_dmcservice.bat que foi baixado nos passos anteriores, isso fará com que o repo seja clonado do GITHUB (nesse passo ele vai pedir algum tipo de autenticação)

- Dentro do repositório, deve ter um arquivo: install-requirements.bat, que deve ser executado, isso instalará todas as dependências do python.

- Instalar o MPLABX, WinAVR e JLinkExe baixados anteriormente, prestar atenção no caminho das instalacões do MPLABX e do JLinkExe.

- Renomear o arquivo config_windows.yaml para config.yaml e alterar os caminhos necessários de acrodo com o que foi instalado.
  
- Criar um atalho no desktop para DMCService.bat.

- Rodar e verificar se ele está funcionando corretamente.