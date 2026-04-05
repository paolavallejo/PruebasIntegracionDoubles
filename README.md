# PruebasIntegracionDoubles

## Descripción de la aplicación

La aplicación permite: 

Crear órdenes para usuarios
Consultar usuarios desde un sistema externo
Guardar órdenes en una base de datos
Mostrar resultados desde una interfaz web


## Arquitectura conceptual:

Web UI
 ↓
Order Service (lógica)
 ↓              ↓
User Repository   Base de datos
 ↓
API externa (JSONPlaceholder)