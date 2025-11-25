# Guía esencial de Git – Control de versiones.

## ¿Qué es Git?

Git es un **sistema de control de versiones**, es decir, una herramienta que permite:

- Guardar el historial de cambios de un proyecto.
- Volver a versiones anteriores cuando algo sale mal.
- Trabajar con ramas sin afectar la versión principal.
- Colaborar sin sobreponer el trabajo de otros.

Es una de las herramientas fundamentales para cualquier desarrollador.

---

## ¿Qué es GitHub?

GitHub es una plataforma en la nube donde puedes **almacenar repositorios Git**, colaborar con otros programadores y mostrar tu portafolio profesional.

- Git = herramienta local  
- GitHub = plataforma online para guardar proyectos y colaborar  

---
# 📁 Configuración inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

---

# 📁 Crear o iniciar un repositorio

```bash
git init
```

---

# 📄 Ciclo básico: add → commit → log

## Añadir archivos al área de preparación
```bash
git add archivo.py
git add .
```

## Guardar cambios (commit)
```bash
git commit -m "Mensaje del commit"
```

## Ver historial
```bash
git log
```

---

# 🌿 Ramas (branches)

## Ver la rama actual
```bash
git branch
```

## Crear una rama
```bash
git branch nombre-rama
```

## Cambiar de rama
```bash
git checkout nombre-rama
```

## Borrar una rama
```bash
git branch -d nombre-rama
git branch -D nombre-rama
```

---

# 🔀 Merge (unión de ramas)

Merge es el proceso de unir los cambios de una rama dentro de otra.

## Realizar un merge
```bash
git checkout main
git merge nombre-rama
```

---

# ⏪ Volver a un commit anterior

## Ver historial simplificado
```bash
git log --oneline
```

## Volver temporalmente a un commit
```bash
git checkout ID_DEL_COMMIT
```

Regresar:
```bash
git checkout main
```

## Volver permanentemente (elimina historia hacia adelante)
```bash
git reset --hard ID_DEL_COMMIT
```

---

# ☁️ Guardar notas de Obsidian en GitHub

1. Entra a tu carpeta de Obsidian.
2. Ejecuta:
```bash
git init
git add .
git commit -m "Primer commit de mis notas"
```
3. Crea un repo en GitHub.
4. Conéctalo:
```bash
git remote add origin URL_DEL_REPO
git push -u origin main
```

---

# 🎯 ¿Qué estudiar después?

## GitHub remoto
- git push
- git pull
- git clone

## Resolver conflictos de merge

## Stash
Guardar cambios temporalmente.

## Rebase
Reescribir la historia de forma más limpia (nivel intermedio).

## Buenas prácticas profesionales
- Mensajes de commit limpios.
- Ramas bien nombradas.
- Flujo GitFlow o trunk-based.

---

# 🏁 Conclusión

Ya dominas los comandos esenciales de Git: init, add, commit, log, branch, checkout, merge, reset, borrar ramas, volver a commits y guardar notas en GitHub. Este archivo está listo para guardarlo en Obsidian o subirlo a tu repositorio personal.