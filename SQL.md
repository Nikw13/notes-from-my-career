# Procesos almacenados en SQL

En **SQL**, los **procesos almacenados** (conocidos formalmente como **procedimientos almacenados** o *stored procedures*) son **bloques de código SQL que se guardan y ejecutan directamente en el servidor de la base de datos**.

---

## Definición

Un **procedimiento almacenado** es un programa que:
- Se escribe una sola vez.
- Se almacena dentro del SGBD.
- Se ejecuta cuando se le llama explícitamente.

---

## ¿Qué pueden contener?

Un procedimiento almacenado puede incluir:

- Consultas `SELECT`
- Operaciones `INSERT`, `UPDATE`, `DELETE`
- Estructuras de control:
  - Condicionales (`IF`, `CASE`)
  - Ciclos (`WHILE`, `LOOP`)
- Parámetros de entrada y salida
- Manejo de errores (dependiendo del motor)

---

## Ejemplo básico

```sql
CREATE PROCEDURE ObtenerUsuarios()
BEGIN
  SELECT * FROM usuarios;
END;
