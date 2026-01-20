# IYC Weekly Todo List

Una aplicación web para organizar tareas semanales de manera visual, utilizando un enfoque estilo Kanban. Perfecta para mejorar la productividad y mantener tus actividades organizadas durante la semana.

## Características

- **Organización por días**: Tareas separadas por días de la semana (Lunes a domingo).
- **Botones funcionales**: Cada día tiene un botón para acceder a la página correspondiente.
- **Interfaz sencilla**: Diseño minimalista que prioriza la facilidad de uso.

## Estructura del Proyecto

El proyecto utiliza una estructura simple basada en HTML, CSS y JavaScript:

- **HTML**: Estructura principal de la aplicación.
- **CSS**: Estilos básicos para las columnas y botones.
- **JavaScript**: Lógica interactiva para navegación con botones.

## Cómo Usar

1. Descarga o clona este repositorio:

   ```bash
   git clone https://github.com/ivanayael/weeklytodolist.git
   

    Abre el archivo index.html en tu navegador.
    Navega entre los días utilizando los botones "Ver" para cada uno.

Código de Ejemplo

A continuación, un fragmento de cómo están organizados los días en el HTML:

```html
<div class="column">
    <h2>Lunes</h2>
    <button onclick="location.href='monday.html'">Ver</button>
</div>
```

## Próximas Mejoras

- **Formato User-Story**: Agregar el template en formato user-story.
- **Tareas al otro dia**:Cuando una tarea no se termine, que se permita pasar manualmente al dia siguiente
- **Agregar horario**: Agregar horario a las tareas que lo necesiten de forma manual.
- **Agregar horas o puntos**: Agregar horas o puntos a la tarea.
- **Agregar prioridad**: Agregar numero de prioridad a las tareas. Y que la prioridad escale al solucionar tareas priorizadas al principio.
- **Agregar diseño a los mensajes de entrada**: Que los mensajes utilicen una libreria propia en javascript.
- **Mejoras en la pagina inicial**: Agregar barra de busqueda, accesibilidad y diseño UI.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes una idea o encuentras un problema, por favor abre un issue o envía un pull request.
Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme.