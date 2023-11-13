# The AirBnB Clone Project

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

# Console de AirBnB

## Descripcion del proyecto

Esta es la primera parte del proyecto de AirBnB clone, en el cual solo nos enfocaremos en el backend mientras lo conectamos a través del modulo cmd en python.
Todos los datos (objetos de python) generados se almacenan en un archivo json y a su vez se puede acceder a esos archivos a través del modulo de lectura de archivos json en python.

## Descripcion del interprete

La interfaz desarrollada con el modulo de cmd de python, es muy similar al interprete de comando (bash), con la diferencia que esta interfaz tiene muy limitado los comandos que son aceptados ya que se definieron únicamente para los fines del uso del la pagina de Airbnb.

### Como empezar

Use el siguiente comando para clonar este repositorio:

```sh
git clone https://github.com/Isaac2036/holbertonschool-AirBnB_clone.git
```

### Como usarlo

Ejecute el comando siguiente, para comenzar:

##### Desde Linux:

`./console.py`

##### Desde Windows:

`python3 console.py`

Através de este interprete puede hacer un CRUD, todos los cambios se
almacenaran en `file.json` (no es necesario que lo cree).

Tiene los siguientes comandos

`EOF`, `all`, `show`,`create`, `destroy`, `help`, `quit` y `update`.

### Ejemplos

#### help

```bash
 ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all create destroy help quit update

(hbnb)
(hbnb)
(hbnb) quit
$
```

#### help [comando]

Use este comando para solicitar ayuda sobre un comando.

```
 ./console.py
(hbnb) help all
Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
(hbnb) help destroy
Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
(hbnb)
```

#### create [objeto]

Con `create` generas una instancia del `objeto`, la cual se almacena en
un archivo file.json.

Use `create [BaseModel | User | State | City | Place | Amenity | Review]`

```
 ./console.py
(hbnb) create BaseModel
ff6d522d-5cbb-4d2e-b273-bf14b21f859b
(hbnb)
```

#### all | all [objeto]

Para mostrar todos los objetos creados o solo un objeto.

```
 ./console.py
(hbnb) all
["[BaseModel] (ff6d522d-5cbb-4d2e-b273-bf14b21f859b) {'id': 'ff6d522d-5cbb-4d2e-b273-bf14b21f859b', 'created_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 905175), 'updated_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 915019)}"]
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (ff6d522d-5cbb-4d2e-b273-bf14b21f859b) {'id': 'ff6d522d-5cbb-4d2e-b273-bf14b21f859b', 'created_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 905175), 'updated_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 915019)}"]
(hbnb)
```

#### show [objeto] [id]

Para imprimir en stdout la representación en cadena de un objeto.

```
 ./console.py
(hbnb) show BaseModel ff6d522d-5cbb-4d2e-b273-bf14b21f859b
[BaseModel] (ff6d522d-5cbb-4d2e-b273-bf14b21f859b) {'id': 'ff6d522d-5cbb-4d2e-b273-bf14b21f859b', 'created_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 905175), 'updated_at': datetime.datetime(2023, 11, 13, 7, 29, 39, 915019)}
(hbnb)
```

#### destroy [objeto] [id]

Elimina un objeto creado con `destroy`.

```
 ./console.py
(hbnb) destroy BaseModel ff6d522d-5cbb-4d2e-b273-bf14b21f859b
(hbnb)
```

#### update [objeto] [id] [atributo] [valor]

Para actualizar un atributo de un objeto use `update`.

```
 ./console.py
(hbnb) update BaseModel ff6d522d-5cbb-4d2e-b273-bf14b21f859b email "aibnb@mail.com"
(hbnb)
```
