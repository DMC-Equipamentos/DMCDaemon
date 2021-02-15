
export DOALL=0

# verifica opção de executar tudo
while getopts "y" opt
do
    case $opt in
    (y) export DOALL=1 ; 
    esac
done


@confirm() {
  local message="$*"
  local result=3

  if [[ "$DOALL" == 1 ]]; then 
    return 0;
  fi

  echo -ne "\n> $message (y/n) " >&2

  while [[ $result -gt 1 ]] ; do
    read -s -n 1 choice
    case "$choice" in
      y|Y ) result=0 ;;
      n|N ) result=1 ;;
    esac
  done

  return $result
}

set -e # Exit script immediately on first error.


if @confirm 'Instalações iniciais?'; then
    # sudo apt update

    # instalações basicas
    sudo apt install -y python3 avrdude python3-pip

    #instalar dependencias do python
    python3 -m pip install -r requirements.txt
fi 

if @confirm 'Instalar mplab?'; then
    (
    mkdir -p install/mplabx
    cd install/mplabx
    # Instalar dependencias
    sudo apt-get install libc6:i386 libx11-6:i386 libxext6:i386 libstdc++6:i386 libexpat1:i386
    wget 'http://gravarplacas.dmcgroup.com.br/dependencias/Ubuntu/MPLABX-v5.45-linux-installer.sh' -O mplabx.sh    
    chmod +x *.sh
    for f in *.sh; do
        sudo ./"$f" || break  # execute successfully or break
    done
    )
fi

if @confirm 'Instalar JLink?'; then
    (
        mkdir -p install/jlink
        cd install/jlink
        # Instalar dependencias
        wget 'http://gravarplacas.dmcgroup.com.br/dependencias/Ubuntu/JLink_Linux_V682c_x86_64.deb' -O jlink.deb
        sudo apt install -y ./jlink.deb 
    )
fi

if @confirm 'Criar config?'; then
    (
        cp config_ubuntu.yaml config.yaml
    )
fi

if @confirm 'Criar desktop?'; then
    (
          cat > DMCService.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=gnome-terminal -e "python3 $PWD/main.py"
Path=$PWD
Name=DMCService
EOF
        chmod +x DMCService.desktop
        sudo mv ./DMCService.desktop /usr/share/applications/
    )
fi