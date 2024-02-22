# Cosas que un no programador puede hacer
## Empieza a escuchar

Todo en código abierto involucra a otras personas.
Estás buscando unirte a un equipo y eso significa comprender la comunidad y cómo funciona.
Entrar en un proyecto y decir "Hola, esto es lo que creo que debería hacer este proyecto" generalmente no se considera algo bueno.
Algunos proyectos pueden acoger con agrado ese tipo de enfoque, pero si el proyecto lleva funcionando un tiempo, las posibilidades de que se adopte esa actitud son pequeñas.
**Escuchar es la mejor manera de saber qué necesita el proyecto.**

1. **Únase a una lista de correo** : para muchos proyectos, la lista de correo es el principal conducto de comunicación sobre el desarrollo del proyecto.
En proyectos grandes, hay muchas listas de correo para elegir.
Por ejemplo, el proyecto PostgreSQL tiene no menos de 12 listas orientadas a usuarios y seis listas de desarrolladores en su página de lista de correo.
Le sugiero que siga la lista principal orientada al usuario y la lista principal de desarrolladores para comenzar a escuchar.

2. **Siga un blog** : los blogs mantenidos por desarrolladores principales a menudo brindan información sobre lo que se avecina en futuras versiones.
y lo que se necesita para llegar allí. Un sitio planetario agrega noticias y entradas de blogs de muchas fuentes relacionadas con el proyecto.
Si hay un sitio planetario, como planet.gnome.org o planet.mysql.com, comience allí. Simplemente busque en Google "planeta <nombre del proyecto>".

3. **Únase a un canal IRC** : muchos proyectos de código abierto tienen canales de chat de retransmisión (IRC) de Internet dedicados donde desarrolladores y usuarios se reúnen para discutir problemas y desarrollo.
Consulte el sitio web del proyecto para obtener detalles sobre cómo se llama el canal y en qué red IRC se encuentra.

**Trabajar con tickets**  
El código es el corazón de cualquier proyecto de código abierto, pero no crea que escribir código es la única forma de contribuir.
El mantenimiento del código y de los sistemas que lo rodean a menudo se descuidan en la prisa por crear nuevas funciones y corregir errores.
Considere estas áreas como una manera fácil de involucrarse en un proyecto.
La mayoría de los proyectos tienen un sistema de notificación de problemas visible públicamente, vinculado desde la página principal del sitio web del proyecto e incluido en la documentación.
Es el conducto principal de comunicación entre los usuarios y los desarrolladores. Mantenerlo actualizado es una excelente manera de ayudar al proyecto.
Es posible que necesite obtener permisos especiales en el sistema de tickets, que la mayoría de los líderes de proyecto estarán encantados de otorgarle cuando diga que quiere ayudar a limpiar los tickets.

4. **Diagnosticar un error** : los errores a menudo no se informan correctamente.
Diagnosticar y clasificar un error puede ayudar a los desarrolladores a ahorrar tiempo con el trabajo preliminar de descubrir los detalles del problema.
Si un usuario informó: "El software no funciona cuando hago X", dedique algún tiempo a descubrir los detalles de ese problema.
¿Es repetible? ¿Puedes crear un conjunto de pasos para causar el problema repetidamente? ¿Puedes limitar el problema, por ejemplo, si solo ocurre en un navegador pero no en otro, o en una distribución pero no en otra?

Incluso si no sabes qué causa el problema, el esfuerzo que pones en delimitar las circunstancias hace que sea más fácil para otra persona solucionarlo.
Cualquier cosa que descubras, agrégala al ticket en el sistema de errores para que todos lo vean.

5. **Cerrar errores solucionados** : a menudo, los errores se corrigen en el código base, pero los tickets informados sobre ellos no se actualizan en el sistema de emisión de tickets.
Limpiar este trozo de papel puede llevar mucho tiempo, pero es valioso para todo el proyecto.

Comience consultando el sistema de tickets en busca de tickets con más de un año y vea si el error aún existe.
Consulte el registro de cambios de versión del proyecto para ver si el error se solucionó y se puede cerrar.
Si se sabe que está solucionado, anote el número de versión en el ticket y ciérrelo.

Intente recrear el error con la última versión del software.
Si no se puede recrear con la última versión, anótelo en el ticket y ciérrelo.
Si todavía existe, anótelo también en el ticket y déjelo abierto.

Trabajar con código
Los programadores de todos los niveles de experiencia pueden ayudar con el código del proyecto.
No creas que tienes que ser un genio de la programación para hacer contribuciones reales a tu proyecto favorito.

Si su trabajo implica modificar el código, investigue el método que utiliza el proyecto para obtener el código de los contribuyentes.
Cada proyecto tiene su propio flujo de trabajo, así que pregunte cómo hacerlo antes de enviar el código.

Por ejemplo, el proyecto PostgreSQL es muy riguroso en su proceso: las modificaciones del código se envían en forma de parche a una lista de correo donde los desarrolladores principales examinan cada aspecto del cambio. En el otro extremo hay un proyecto como Parrot donde es fácil obtener privilegios de confirmación para el código base. Si el proyecto usa GitHub, puede haber un flujo de trabajo que use la función de solicitud de extracción de GitHub. No hay dos proyectos iguales.

Siempre que modifique el código, asegúrese de actuar como un miembro responsable de la comunidad y de mantener el estilo de su código para que coincida con el resto del código base. El código que agregue o modifique debería verse como el resto. Puede que no le guste el estilo de refuerzo o el manejo de los espacios para la sangría, pero es de mala educación enviar un cambio de código que no coincide con los estándares existentes. Es lo mismo que decir "No me gusta tu estilo y creo que el mío es mejor, así que deberías hacerlo a mi manera".

6. **Pruebe una versión beta o candidata** : cualquier proyecto diseñado para ejecutarse en múltiples plataformas puede tener todo tipo de problemas de portabilidad.
Cuando se acerca una versión y se publica una versión beta o candidata, el líder del proyecto espera que sea probada por muchas personas diferentes en muchas plataformas diferentes.
Usted puede ser una de esas personas y ayudar a garantizar que el paquete funcione en su plataforma.

Por lo general, solo necesita descargar, compilar y probar el software, pero el valor para el proyecto puede ser enorme si utiliza una distribución o hardware poco común.
Simplemente informar que la compilación y la prueba funcionan ayuda a los líderes del proyecto a saber que el lanzamiento inminente es sólido.

7. **Corregir un error** : aquí es donde generalmente comienzan los contribuyentes que desean comenzar a trabajar en el código.
Es simple: encuentre un error que parezca interesante en el sistema de tickets e intente corregirlo en el código.
Documente la solución en el código si es apropiado.
Es una buena idea agregar una prueba al conjunto de pruebas para probar el código que corrigió; algunos proyectos requieren correcciones de errores para incluir pruebas. Tome notas mientras hurga en este código base desconocido. Incluso si no puede corregir el error, documente en el ticket lo que descubrió como parte del intento de solucionarlo. Lo que encuentres ayudará a quienes te sucedan.

8. **Escribe una prueba** : la mayoría de los proyectos tienen un conjunto de pruebas que prueba el código, pero es difícil imaginar un conjunto de pruebas al que no se le puedan agregar más pruebas.
Utilice una herramienta de cobertura de pruebas como gcov para C o Devel::Cover para Perl para identificar áreas en el código fuente que no han sido probadas por el conjunto de pruebas.
Luego, agregue una prueba a la suite para cubrirlo.

9. **Silenciar una advertencia del compilador** : el proceso de compilación de muchos proyectos basados en C a menudo arroja algún que otro indicador de advertencia del compilador en la pantalla.
Estas advertencias generalmente no son indicadores de un problema, pero pueden parecerlo.
Tener demasiadas advertencias puede hacer que el compilador suene como si estuviera llorando.
Verifique si el código realmente podría estar ocultando un error. De lo contrario, modificar la fuente para silenciarla ayuda a ocultar estos falsos positivos.

10. **Agrega un comentario** :
Cuando exploras el código, es posible que encuentres algunos puntos que te resulten confusos.
Lo más probable es que si usted estaba confundido, otros también lo estarán. Documentarlos en el código y enviar un parche.
Trabajar con documentación
La documentación suele ser la parte de un proyecto que recibe poca atención.
También puede verse afectado por haber sido escrito desde el punto de vista de quienes están familiarizados con el proyecto, en lugar de desde los ojos de alguien que recién se está involucrando en él.
Si alguna vez ha leído documentos de un proyecto en el que piensa: "Es como si este manual esperara que yo ya supiera cómo utilizar el paquete", sabe de lo que estoy hablando.
A menudo, un par de ojos nuevos pueden señalar deficiencias en la documentación que quienes están cerca del proyecto no notan.

11. **Crea un ejemplo** : No hay ningún proyecto que tenga demasiados ejemplos prácticos.
Ya sea una API web, una biblioteca de rutinas, una aplicación GUI como Gimp o una herramienta de línea de comandos,
un buen ejemplo de uso adecuado puede explicar más clara y rápidamente el uso adecuado del software que las páginas de documentación.
Para una API o biblioteca, cree un programa de ejemplo que utilice la herramienta. Esto incluso podría extraerse del código que haya escrito y reducirlo a lo estrictamente necesario.
Para una herramienta, muestre ejemplos del mundo real de cómo la ha utilizado en su vida diaria. Si estás orientado visualmente,
Considere la posibilidad de crear una captura de pantalla de un proceso importante, como por ejemplo cómo instalar la aplicación.

Trabajar con la comunidad
El código abierto se trata sólo en parte de código. La comunidad hace que el código abierto funcione. A continuación le presentamos formas en las que puede ayudar a desarrollarlo.

12. **Responda una pregunta** : La mejor manera de ayudar a construir la comunidad es ayudando a los demás.
Responder una pregunta, especialmente de alguien que recién se está iniciando, es crucial para ayudar a que el proyecto crezca y prospere.
El tiempo que se toma para ayudar a un principiante, incluso si está haciendo una pregunta en la que fácilmente se podría responder con un rápido "RTFM", vale la pena en el futuro para conseguir otro miembro activo de la comunidad.
Todo el mundo empieza en alguna parte y los proyectos necesitan un flujo constante de personas para que sigan siendo vitales.

13. **Escribe una publicación de blog** :
Si tienes un blog, escribe sobre tus experiencias con el proyecto que estás utilizando.
Cuéntanos sobre un problema que enfrentaste al usar el software y qué hiciste para resolverlo.
Ayudarás de dos maneras: ayudando a mantener el proyecto en la mente de quienes te rodean,
y creando un registro para cualquier otra persona que tenga su problema en el futuro y busque la respuesta en la web.
(Un blog de sus aventuras técnicas también es una excelente manera de mostrar su experiencia en el mundo real con el software en cuestión la próxima vez que busque trabajo usándolo).

14. **Mejorar un sitio web** :
Si tiene habilidades en diseño web y puede ayudar a mejorar el sitio web y, por lo tanto, la imagen pública del proyecto, es tiempo bien invertido.
Quizás el proyecto podría necesitar una revisión gráfica o un logotipo para identificarlo.
Estas pueden ser habilidades que faltan en la comunidad. Sé que me encantaría poder obtener ayuda con el diseño gráfico de los sitios web de mis proyectos.
  
15. **Escribir documentación técnica**
Si puede escribir sobre cómo funciona una aplicación o software, puede escribir documentación técnica al respecto. Especialmente proyectos de código abierto que buscan actualizar, renovar, ampliar o crear documentos técnicos para que los lea el público en general. Cuanto más escribas en inglés sencillo, mejor. La mejor parte es que no es necesario ser programador para escribir documentos técnicos.

Sobre todo, escuche lo que discuten las personas que lo rodean. Vea si puede reconocer una necesidad urgente. Por ejemplo, recientemente en la lista de correo de los desarrolladores de Parrot, se decidió utilizar GitHub como sistema de notificación de problemas, abandonando la antigua instalación de Trac que tenían. Algunas personas estaban en contra de la medida porque no había forma de convertir los tickets al sistema de GitHub. Después de un día de discusiones de ida y vuelta, hablé y dije: "¿Qué tal si escribo un convertidor?" La gente estaba encantada con la idea. Dediqué tiempo a escribir un programa de conversión para más de 450 boletos, por lo que no perdimos nada de nuestro historial de boletos. Fue un gran éxito. Pude colaborar y los desarrolladores principales se mantuvieron concentrados en el negocio de trabajar en Parrot.

15. **Enseñar y ayudar a otros** :
La mejor manera de aprender más sobre un tema es intentar enseñarlo.
El mejor profesor es el que puede explicar cosas complejas con ejemplos sencillos. Por lo tanto, debes intentar ser el mejor maestro para ser el mejor alumno y el mejor en tu mundo de programación. Enseñar a otros te hará sentir mejor contigo mismo y te ayudará a adquirir mejores habilidades y conocimientos en tu profesión. Cuando reciba ayuda de alguien, no se la guarde para usted, compártala con los demás. Hacer el mundo un lugar mejor para vivir .
