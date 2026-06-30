El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas 

Zahid Joel Jara Cazorla

El objetivo principal de este sistema es proporcionar una herramienta informática accesible y eficiente para la Generación de Credenciales Seguras, minimizando el riesgo de vulnerabilidades digitales y ciberataques en el entorno social actual.

1.- Control y Validación de Entradas : El sistema exige y valida mediante estructuras de control de errores que el usuario ingrese una longitud numérica entera y positiva. Además, emite una advertencia si la longitud deseada es menor a 6 caracteres, promoviendo activamente las buenas prácticas de ciberseguridad.

2.- Personalización Dinámica de Seguridad: Permite al usuario decidir de forma interactiva si desea incluir números y caracteres especiales símbolos en el algoritmo de generación. El sistema adapta dinámicamente los bancos de caracteres según estas respuestas.

3.- Algoritmo de Generación Aleatoria: Utiliza la librería random para seleccionar de manera impredecible cada componente de la credencial, asegurando que ninguna contraseña sea idéntica a otra.

4.- Segmentación de Lectura Humana : El sistema implementa una estructura condicional basada en operadores aritméticos de residuo para inyectar automáticamente un guion cada 4 caracteres. Esto optimiza la legibilidad de las claves largas para el usuario sin comprometer su seguridad.

5.- Ciclo de Vida Continuo: Mediante un bucle repetitivo , el programa permite al usuario generar múltiples credenciales de forma consecutiva, limpiando las variables en memoria en cada iteración y finalizando la ejecución de forma segura únicamente cuando el operador lo decida.

Fecha:2026-06-29
