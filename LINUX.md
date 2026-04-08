
# Estructura de ficheros en Linux:

* ### EXT4 (Este es el más usado)
* ### XFS
* ### BTRS
---
# Inodos, Bloques y Superbloques en Linux

En los sistemas operativos basados en Linux, los sistemas de archivos utilizan estructuras internas para gestionar y organizar la información almacenada en disco. Entre las más importantes se encuentran el **inodo**, el **bloque** y el **superbloque**.

---
## 1. Inodo (inode)

Un **inodo** (*index node*) es una estructura de datos que almacena la **información descriptiva de un archivo o directorio**, pero no su nombre ni su contenido.

### Información que almacena un inodo
- Tipo de archivo (archivo regular, directorio, enlace, etc.)
- Permisos de acceso (lectura, escritura y ejecución)
- Identificador del propietario (UID) y del grupo (GID)
- Tamaño del archivo
- Fechas importantes:
  - Último acceso (atime)
  - Última modificación (mtime)
  - Último cambio de metadatos (ctime)
- Número de enlaces duros (*hard links*)
- Direcciones de los bloques donde se almacenan los datos

### Características importantes
- Cada archivo tiene un único inodo
- El nombre del archivo se almacena en el directorio, no en el inodo
- Linux identifica internamente los archivos por su número de inodo


Ejemplo para ver el inodo de un archivo:

### BASH: 
ls -i archivo.txt

---
# Bloque (Block)

Un **bloque** es la **unidad mínima de almacenamiento** utilizada por el sistema de archivos en Linux. Es el espacio donde se guardan tanto los datos reales de los archivos como cierta información del sistema.

### Características principales
- Tamaño común: **4 KB** (puede variar según el sistema de archivos)
- Un archivo puede ocupar uno o varios bloques
- Los bloques son asignados dinámicamente según el tamaño del archivo

### Tipos de bloques
- **Bloques de datos**: almacenan el contenido real de los archivos
- **Bloques de metadatos**: almacenan información del sistema como inodos y mapas de bits

### Relación con el inodo
- El inodo contiene **punteros** que indican en qué bloques están los datos del archivo
- Para archivos grandes se utilizan punteros:
  - Directos
  - Indirectos
  - Doblemente indirectos
  - Triplemente indirectos

Los bloques permiten un uso eficiente del espacio en disco y facilitan el acceso rápido a la información.

---

## Superbloque (Superblock)

El **superbloque** es una estructura crítica que almacena la **información global del sistema de archivos**. Describe cómo está organizado y en qué estado se encuentra.

### Información que almacena
- Tipo de sistema de archivos (ext4, ext3, XFS, etc.)
- Tamaño total del sistema de archivos
- Número total de bloques
- Número total de inodos
- Cantidad de bloques e inodos libres
- Tamaño de los bloques
- Estado del sistema de archivos (limpio o con errores)

### Importancia
- Se lee cuando el sistema de archivos es montado
- Si el superbloque se daña, el sistema de archivos puede quedar inaccesible
- Existen copias de respaldo del superbloque para tareas de recuperación

El superbloque es esencial para que el sistema operativo pueda interpretar correctamente la estructura del disco.






https://youtu.be/8v1cR7-msQ0?t=715