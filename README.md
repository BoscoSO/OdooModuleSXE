
# My Inventory
Módulo Odoo para Segunda Evaluación 

## Que es?

My Inventory es un módulo de gestión de inventario

## De que sirve

Su principal objetivo, es mantener cuenta de los distintos inventarios que una empresa puede tener y donde están distribuidos (las localizaciones de la empresa) <br>
Entre otras cosas este módulo muestra de manera visual el estado del stock de productos avisando cuando quedan pocos, o cuando no queda ninguno

# REQUISITOS PARA EL MODULO

## -Fields
A mayores de datos tipo básico se implementan en este módulo valores monetary (con su campo currency relacionado), campos data, campos calculados (para ver el valor total de un inventario), y campos relacionales en los que una localización puede tener N inventarios y estos a su vez pueden tener N items

<br>

## -Herencia

Este módulo no hace esto

<br>

## -Vistas y acciones y gesion de registros

La creacion y modificacion de registros esta implementada, y restringiendo valores no deseados
<br>
El borrado de registros conlleva un borrado en cascada de los registros hijos que posea

Estan implementadas en este módulo las vistas form, tree, search y kanban
- Se implementan un filtro para buscar inventarios vacios
- Un boton para reponer unidades en stock
- La vista kanban informa de manera visual el estado del producto en ese inventario cambiando el color si hay suficientes(verde) o quedan pocos (naranja), o ninguno (rojo)
- En la vista form los campos relacionales se autoCompletan por defecto 
- Los campos calculados se reflejan en vistas tree y kanban
