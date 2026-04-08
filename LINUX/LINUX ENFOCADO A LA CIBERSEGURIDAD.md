# Introducción

- Este documento está diseñado para pasar **de cero a desenvolverse completamente** en sistemas Linux, entendiendo el "por qué" de cada acción.

- Se enfoca en **seguridad ofensiva** (hacking ético), usando **Kali Linux** como distribución principal.

---
# ¿Qué es Linux?

## Historia

- Creado por **Linus Torvalds** en 1991, inspirado en **Minix**.

- Primera versión del kernel: **0.01**.

- Se unió al proyecto **GNU**, dando lugar a **GNU/Linux** (aunque normalmente se llama solo Linux).

- Licencia: **GNU GPL** (permite modificar y distribuir).

## Definición

- **Linux** es el **kernel** (núcleo) del sistema operativo.

- Una **distribución (distro)** = kernel Linux + capas de personalización + paquetes + herramientas, orientada a un nicho específico.

---

## 3. Distribuciones basadas en otras

- Una distro se **basa** en otra cuando reutiliza su código fuente, bibliotecas y herramientas.

- Ejemplo: **Kali Linux** está basada en **Debian** (y también toma componentes de Ubuntu).

- Ventaja: ahorro de tiempo y estabilidad.

---

## 4. Estructura del sistema de archivos de Linux

### 4.1. Jerarquía y directorios principales

| Directorio | Contenido |

|------------|-----------|

| `/boot` | Arranque del sistema (kernel, initramfs) |

| `/etc` | Configuraciones del sistema y aplicaciones |

| `/var` | Datos variables (logs, bases de datos) |

| `/usr` | Aplicaciones y librerías compartidas (`/usr/bin`, `/usr/lib`) |

| `/home` | Directorios personales de los usuarios |

| `/root` | Home del usuario root |

| `/tmp` | Archivos temporales (se borran al reiniciar) |

| `/dev` | Dispositivos de hardware |

| `/sbin` | Ejecutables esenciales para el sistema |

| `/proc` | Sistema virtual con información del kernel y procesos |

| `/sys` | Interfaz directa con el kernel para hardware |

### 4.2. Inodos, bloques y superbloque

- **Inodo**: metadatos del archivo (permisos, propietario, tamaño).

- **Bloque**: unidad de almacenamiento de datos.

- **Superbloque**: información global del sistema de archivos.

### 4.3. Enlaces (links)

- **Enlace duro**: apunta al mismo inodo. Si modificas uno, cambian todos.

- **Enlace simbólico** (blando): acceso directo a una ruta. Si se elimina el original, queda roto.

### 4.4. Permisos básicos

- **Lectura (r)** – Ver contenido.

- **Escritura (w)** – Modificar o eliminar.

- **Ejecución (x)** – Ejecutar (archivos) o entrar (directorios).

- Categorías: **propietario (u)**, **grupo (g)**, **otros (o)**.

---

## 5. Principales distribuciones de Linux

- **Debian** (base de muchas), **Slackware**, **Red Hat**, **Arch Linux**.

- Mapa histórico: [https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg)

- Páginas de referencia: `distrowatch.com`, `archiveos.org`

---

## 6. Distribuciones para ciberseguridad

| Distro | Base | Enfoque |

|--------|------|---------|

| Kali Linux | Debian | Pentesting, red team |

| Kali Purple | Debian | Blue team (defensiva) |

| Parrot Security | Debian | Similar a Kali |

| BlackBuntu | Ubuntu | Pentesting (soporte intermitente) |

| BlackArch | Arch Linux | Pentesting |

| Wifislax | Slackware | Redes inalámbricas |

| Tails | Debian | Anonimato (modo amnesia) |

| Whonix | Debian | Todo el tráfico por Tor |

| Qubes OS | (hipervisor Xen) | Aislamiento de seguridad |

| CAINE / SANS SIFT | Ubuntu | Forensia digital |

---

## 7. Instalación de Kali Linux en VirtualBox

### 7.1. Importar máquina preconfigurada

1. Descargar la máquina virtual desde la web oficial de Kali (sección "Virtual Machines").

2. Descomprimir el `.7z`.

3. En VirtualBox: **Nueva máquina** → **Usar disco duro existente** → seleccionar el `.vdi`.

4. Credenciales por defecto: `kali / kali`

5. Cambiar teclado: `setxkbmap es` (temporal) o `dpkg-reconfigure keyboard-configuration` (permanente).

6. Cambiar idioma: `dpkg-reconfigure locales`

### 7.2. Instalación manual desde ISO

1. Descargar ISO de Kali.

2. Crear máquina virtual nueva, **sin disco existente**.

3. Iniciar y seleccionar la ISO.

4. Seguir asistente: idioma, ubicación, teclado, nombre de máquina, usuario, contraseña.

5. Particionado: **guiado** (recomendado para el curso).

6. Seleccionar entorno de escritorio (por defecto).

7. Instalar el cargador de arranque (GRUB) en el disco virtual.

8. Posibles errores: desactivar antivirus o descargar ISO de nuevo.

---

## 8. Instalación de Kali Linux en WSL (Windows Subsystem for Linux)

- **WSL1**: traducción de llamadas (no kernel real).

- **WSL2**: máquina virtual ligera con kernel Linux real.

- **Instalación**:

  1. Activar "Subsistema de Windows para Linux" desde Panel de control.

  2. Reiniciar.

  3. Ir a Microsoft Store → buscar "Kali Linux" → instalar.

  4. Iniciar y configurar usuario/contraseña.

- **Limitación**: no sirve para laboratorios de red complejos (ideal solo para practicar comandos).

---

## 9. ¿Qué es un comando?

- **Comando**: secuencia de instrucciones escritas en algún lenguaje de programación, asociada a una **palabra clave**.

- Al ejecutarla, el sistema corre todas esas instrucciones y realiza una acción.

- Ejemplo: `ls` → llama al código que lista el contenido del directorio.

- Puedes crear tus propios comandos (scripts).

---

## 10. Shell vs Emulador de terminal

- **Terminal** (física): interfaz antigua de entrada/salida.

- **Emulador de terminal**: programa que simula una terminal física (ej: Terminator, GNOME Terminal, Kitty).

- **Shell**: programa que interpreta comandos y los traduce al sistema. Es el puente entre usuario y kernel.

- Shells comunes: `sh` (Bourne), `bash` (Bourne Again, la más usada), `zsh` (más interactiva).

---

## 11. Emulador de terminal online

- Alternativa si tu PC no tiene recursos.

- Sitios: JS Linux, JSLinux, Tutorialspoint Unix Terminal.

- **Advertencia**: no almacenes información sensible; solo para practicar comandos.

---

## 12. Terminator (emulador de terminal mejorado)

### Instalación

```bash

sudo apt update

sudo apt install terminator -y

Uso básico

·

Ejecutar: terminator

·

·

Zoom: Ctrl + rueda del ratón.

·

·

Dividir vertical: Ctrl + Shift + E

·

·

Dividir horizontal: Ctrl + Shift + O

·

·

Atajos configurables.

·

13. El Prompt en Linux

·

Es el indicador de comandos (ej: usuario@host:~$).

·

·

Estructura típica en bash: usuario@hostname:ruta_actual$

·

·

$ → usuario normal.

·

·

# → usuario root.

·

Para cambiar a bash temporalmente: /bin/bash

Cambio permanente: chsh -s /bin/bash

14. Ficheros más importantes en Linux

Fichero Contenido

/etc/passwd Usuarios del sistema (nombre, UID, GID, home, shell)

/etc/group Grupos del sistema

/etc/shadow Contraseñas encriptadas (solo accesible por root)

/etc/fstab Puntos de montaje de sistemas de archivos

/etc/network/interfaces Configuración de red (en distros antiguas)

/etc/hostname Nombre del host

/etc/resolv.conf Servidores DNS

~/.bashrc (o ~/.zshrc) Configuración persistente de la shell (alias, variables de entorno)

15. Directorios más importantes (ya visto en punto 4.1)

16. Variables de entorno en Linux

16.1. Ver todas las variables

bash

env

16.2. Ver una variable concreta

bash

echo $HOMEecho $PATHecho $USER

16.3. Crear/modificar variables (temporal)

bash

export MI_VARIABLE="valor"export PATH="$PATH:/nuevo/directorio"

16.4. Eliminar variable

bash

unset MI_VARIABLE

16.5. Variables persistentes

Añadir la línea export a ~/.bashrc (o ~/.zshrc). Luego recargar:

bash

source ~/.bashrc

16.6. Variables de entorno importantes

·

PATH – rutas donde el sistema busca ejecutables.

·

·

HOME – directorio home del usuario.

·

·

USER – nombre del usuario actual.

·

·

SHELL – shell actual.

·

·

TERM – tipo de terminal.

·

·

LANG – idioma y localización.

·

17. Comandos de ayuda y soporte

Comando Función

man <comando> Manual completo

info <comando> Información más detallada (a veces)

whatis <comando> Breve descripción

apropos <palabra> Busca comandos relacionados

whereis <comando> Ubicación del binario y página del manual

which <comando> Ruta del ejecutable

<comando> --help Ayuda rápida

help <comando> Para comandos internos de la shell (ej: help cd)

18. Rutas absolutas y relativas

·

Absoluta: comienza con / (raíz). Ej: /home/marti/documento.txt

·

·

Relativa: no comienza con /. Usa . (directorio actual) y .. (directorio padre).

·

·

Ejemplo: estando en /home/marti, para ir a /etc:

·

o

Absoluta: cd /etc

o

o

Relativa: cd ../.. (subes a /) y luego cd etc

o

19. Argumentos vs Parámetros

·

Parámetros (opciones): modifican el comportamiento. Suelen empezar con - o --. Ej: ls -l

·

·

Argumentos: datos sobre los que actúa el comando. Ej: ls /home → /home es argumento.

·

·

Pueden combinarse: ls -l /home

·

20. Comandos de navegación, gestión de ficheros y directorios

Navegación

·

cd <ruta> – cambiar directorio.

·

·

pwd – mostrar directorio actual.

·

Listado

·

ls, ls -a (ocultos), ls -l (detallado), ls -R (recursivo), ls -lh (tamaño legible).

·

Gestión de ficheros

·

touch <archivo> – crear vacío o actualizar fecha.

·

·

cp <origen> <destino> – copiar. cp -r para directorios.

·

·

mv <origen> <destino> – mover o renombrar.

·

·

rm <archivo> – eliminar. rm -r para directorios. rm -i pide confirmación.

·

Gestión de directorios

·

mkdir <dir> – crear. mkdir -p crea padres intermedios.

·

·

rmdir <dir> – eliminar directorio vacío (mejor usar rm -r).

·

Visualización de ficheros

·

cat <archivo> – muestra todo.

·

·

head -n <archivo> – primeras n líneas.

·

·

tail -n <archivo> – últimas n líneas. tail -f sigue en tiempo real.

·

·

less <archivo> – paginado, permite desplazamiento.

·

21. Stdin, stdout y stderr

·

stdin (0) – entrada estándar (teclado).

·

·

stdout (1) – salida estándar (terminal).

·

·

stderr (2) – salida de errores (terminal).

·

Redirecciones

·

comando > archivo – redirige stdout (sobrescribe).

·

·

comando >> archivo – añade stdout.

·

·

comando 2> archivo – redirige stderr.

·

·

comando &> archivo – redirige ambos.

·

·

comando > /dev/null – descarta salida.

·

Tuberías (pipe) |

Envía stdout de un comando como stdin del siguiente.

Ej: ls -l | grep ".txt"

xargs

Convierte stdin en argumentos para comandos que no aceptan tubería directamente (ej: rm, cp).

Ej: ls *.txt | xargs rm

22. Operadores lógicos entre comandos

Operador Efecto

&& Ejecuta segundo solo si el primero tuvo éxito.

|| Ejecuta segundo solo si el primero falló.

; Ejecuta todos en secuencia, sin importar éxito.

! Invierte el código de salida.

& Ejecuta el comando en segundo plano.

23. Gestión de usuarios

Comando Función

sudo adduser <nombre> Crear usuario (interactivo, recomendado).

sudo deluser <nombre> Eliminar usuario. --remove-home borra su home.

sudo usermod Modificar usuario. Opciones: -l (login), -d (home), -aG (añadir a grupo).

passwd Cambiar contraseña propia. sudo passwd <user> para otro.

id <usuario> Mostrar UID, GID y grupos.

who Usuarios conectados. who -u con hora.

su - <usuario> Cambiar de usuario (sin argumentos → root).

sudo Ejecutar comando como otro usuario (por defecto root).

whoami Muestra el usuario actual.

finger <usuario> Información detallada del usuario.

24. Gestión de grupos

Comando Función

sudo addgroup <grupo> Crear grupo.

sudo delgroup <grupo> Eliminar grupo (vacío).

sudo groupmod -n <nuevo> <viejo> Renombrar grupo.

sudo gpasswd -a <user> <grupo> Añadir usuario al grupo.

sudo gpasswd -d <user> <grupo> Quitar usuario del grupo.

groups <usuario> Ver grupos del usuario.

25. Gestión de paquetes (Debian/Kali)

apt (recomendado)

Comando Función

sudo apt update Actualiza lista de paquetes.

sudo apt upgrade Actualiza paquetes instalados.

sudo apt full-upgrade Actualización completa con manejo de dependencias.

sudo apt install <paquete> Instalar.

sudo apt remove <paquete> Eliminar (conserva configuraciones).

sudo apt purge <paquete> Eliminar completamente.

sudo apt autoremove Eliminar dependencias no necesarias.

dpkg (bajo nivel)

·

sudo dpkg -i <paquete.deb> – instalar.

·

·

sudo dpkg -r <paquete> – eliminar (sin purgar).

·

·

sudo dpkg -P <paquete> – purgar.

·

·

dpkg -l – listar instalados.

·

Ficheros de repositorios

·

/etc/apt/sources.list

·

·

/etc/apt/sources.list.d/

·

26. Gestión de redes

Nomenclatura de interfaces

·

Tradicionales: eth0, wlan0, lo (loopback).

·

·

Predictivas: enp2s0 (Ethernet bus PCI 2 slot 0), wlps (WiFi).

·

Comandos

Comando Función

ifconfig Mostrar/configurar interfaces (instalar con net-tools).

ip a o ip addr Mostrar direcciones IP.

ip link set <interfaz> up/down Activar/desactivar.

ip route Tabla de enrutamiento.

netstat -tulpn Conexiones y puertos en escucha.

ping -c <n> <host> Prueba conectividad ICMP.

traceroute <host> Ruta de los paquetes.

nslookup <dominio> Consulta DNS.

hostname Mostrar/cambiar nombre del host.

27. Comandos de ficheros comprimidos

Herramienta Comprimir Descomprimir

tar + gzip tar czf archivo.tar.gz directorio/ tar xzf archivo.tar.gz

gzip gzip archivo (crea .gz) gzip -d archivo.gz

zip zip archivo.zip ficheros unzip archivo.zip

28. Gestión de procesos

Comando Función

ps aux Todos los procesos con detalles.

top Procesos en tiempo real.

kill -9 <PID> Matar proceso (señal SIGKILL).

killall <nombre> Matar todos los procesos con ese nombre.

·

Señales comunes: -15 (TERM, normal), -9 (KILL, forzada).

·

29. Comandos de búsqueda

Comando Función

find <ruta> -name "patrón" Buscar archivos por nombre, tipo, tamaño, fecha.

grep "texto" <archivo> Buscar texto dentro de archivos. -i (ignora mayúsculas), -c (cuenta).

locate <nombre> Buscar en base de datos (actualizar con sudo updatedb).

Ejemplo combinado: find /home -name "*.txt" | grep "secreto"

30. Editores de texto en terminal

nano (sencillo)

·

Abrir: nano archivo

·

·

Guardar: Ctrl+O

·

·

Salir: Ctrl+X

·

vim (avanzado)

·

Modos: Normal (Esc), Inserción (i), Comando (:).

·

·

Comandos: :w guardar, :q salir, :wq guardar y salir, :q! salir sin guardar.

·

·

Moverse: h (izq), j (abajo), k (arriba), l (der).

·

31. Comandos adicionales útiles

Comando Función

nc (netcat) Leer/escribir en conexiones de red. -l escucha, -v verbose.

echo Imprimir texto o variables. -e interpreta escapes (\n, \t).

sort Ordenar líneas. -n numérico, -k por campo, -r inverso.

wget Descargar archivos. -c reanudar.

curl Transferir datos con URL.

du -h Espacio en disco (legible).

free -h Memoria RAM y swap.

32. Atajos en Linux (Parte 1 y 2)

Atajos de línea de comandos

Atajo Función

Ctrl+A Ir al inicio de la línea.

Ctrl+E Ir al final.

Ctrl+U Borrar desde cursor al inicio.

Ctrl+K Borrar desde cursor al final.

Ctrl+L Limpiar pantalla (similar a clear).

Ctrl+C Terminar proceso actual.

Ctrl+Z Suspender proceso (reanudar con fg).

Ctrl+R Buscar en historial.

Ctrl+D Salir de terminal o de cat sin argumentos.

Tab Autocompletar.

Flechas arriba/abajo Navegar historial.

Atajos de procesos y background

·

jobs – ver procesos suspendidos o en segundo plano.

·

·

fg %<número> – traer a primer plano.

·

·

bg – reanudar en segundo plano.

·

·

disown – desligar proceso de la terminal.

·

Atajos de Terminator

·

Ctrl+Shift+E – dividir vertical.

·

·

Ctrl+Shift+O – dividir horizontal.

·

33. Alias en Linux

·

Crear alias temporal: alias <nombre>='comando'

·

·

Ver alias: alias

·

·

Eliminar: unalias <nombre>

·

·

Alias permanente: añadir la línea a ~/.bashrc o ~/.zshrc.

·

Ejemplo: alias ll='ls -la'

34. Permisos en Linux

34.1. Notación octal

Cada permiso tiene un valor:

·

r = 4

·

·

w = 2

·

·

x = 1

·

Los permisos se expresan con tres dígitos (propietario, grupo, otros).

Ejemplo: chmod 755 archivo → propietario: 7 (rwx), grupo: 5 (r-x), otros: 5 (r-x).

34.2. Notación simbólica

·

chmod u+rwx archivo – añade rwx al propietario.

·

·

chmod g-w archivo – quita escritura al grupo.

·

·

chmod o=r archivo – establece solo lectura para otros.

·

·

chmod a+x archivo – añade ejecución a todos.

·

34.3. Permisos especiales: SUID, SGID, Sticky Bit

Permiso Octal Efecto Visualización

SUID 4xxx Ejecuta con permisos del propietario rws en lugar de rwx del propietario

SGID 2xxx Ejecuta con permisos del grupo; en directorios, nuevos archivos heredan el grupo rws en el campo del grupo

Sticky Bit 1xxx Solo el propietario puede borrar/renombrar en el directorio t en el campo de otros

Ejemplo: chmod 4755 archivo → SUID + rwxr-xr-x

34.4. Cambio de propietario y grupo

·

chown usuario:grupo archivo

·

·

chown usuario archivo (solo propietario)

·

·

chgrp grupo archivo (solo grupo)

·

·

Usar -R para recursivo.

·

35. Permisos Sudoers

·

El archivo /etc/sudoers controla quién puede usar sudo.

·

·

Editar siempre con visudo (evita errores de sintaxis).

·

·

Línea típica: usuario ALL=(ALL:ALL) ALL → puede ejecutar todo como cualquier usuario/grupo.

·

·

NOPASSWD: ALL → no pide contraseña.

·

·

Grupo especial sudo: por defecto, sus miembros tienen permisos completos.

·

36. Conclusión y recomendaciones finales

·

Practicar es la única forma de aprender. Usa tu máquina virtual o WSL.

·

·

No memorices comandos; aprende a consultar ayuda (man, --help).

·

·

Toma apuntes manuales (papel y lápiz) para retener mejor.

·

·

Únete a la comunidad (Discord) para resolver dudas.

·

·

Este curso es el cimientos de tu carrera en ciberseguridad. Sigue profundizando.

·

[!tip] La clave del éxito es la constancia y la curiosidad.