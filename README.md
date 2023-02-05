# Proyecto-Final---RojasParucho
Proyecto Final Con Python Y Django - CoderHouse
Link Del Video: https://www.loom.com/share/1314f67e36b74db68c72e5cf13829b50

Documentacion Aqui Tratare De Explicar Un Poco Sobre lo Que Hice En Mi Proyecto, Ademas De Que Funciones Utilice y Que tal Fueron Los Resultados, Para Acceder A Estos, Se Encuentran Dentro De La Carpeta Del Proyecto, Esta Seria La Ubicacion "blog/devsocial/" Aqui Encontraras La Mayoria De Archivos Importantes

Models.py Dentro De Este Archivo De Python Se Encontrara Con Dos Modelos (Post Y Comentario) Cada Uno De Estos Recibe En La BD, Un Nombre, Una Fecha, Un Contenido,etc

forms.py Dentro De forms.py se utilizaron unicamente tres clases, una para la creacion o registro de un usuario, otra para agregar un post y otra para agregar un comentario en un debido post, cabe destacar que en los formularios de post solo se pediran el titulo,contenido y imagen y en comentarios solo el contenido del comentario

views.py Dentro de views.py Te Encontraras con muchas importaciones ademas de muchas funciones, que van desde la renderizacion de la pagina de inicio y muchas otras mas, hasta diferentes formularios como para iniciar sesion, registrarse, buscar un post, agregar un post, agregar un comentario, listar los post al igual que los comentarios, y eliminar los post(solo el superusuario puede hacerlo)

Urls.py En Urls Encontraras las distintas ubicaciones creadas, donde se incluye la direccion, el nombre de la funcion y un nombre aparte...

Plantillas Aqui Encontraras Las Diferentes Plantillas Las Cuales Herederan De Una Plantilla Padre, La Cual utilice de una pagina web

Css Y Imagenes Para Que El Css Funcione Se Hicieron Algunos Cambios En Settings.py Ademas De La Creacion De Una Carpeta Static, Se Hizo Un Proceso Similar Para Mostrar Las Imagenes De Los Post
