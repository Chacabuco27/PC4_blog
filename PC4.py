# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 

print("Sunim")
# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run PC4.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>El mundo de Chacabuco 📝</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    # Columna izquierda: texto 
    # col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
    # col1.image("Fotografía.jpg", caption='Desde mi lado sincero y divertido', width=300)
    texto = """
    <p>Mi nombre es Sunim Cardenas y me encuentro cursando el sexto ciclo de la carrera de Periodismo en la Pontificia Universidad Católica del Perú (PUCP). En el pasado, me cuestioné si era la elección adecuada y también si era mi pasión. No llegué a ninguna conclusión, pero a diferencia de antes, hoy disfruto del proceso y cada vez me interesan esos aspectos periodísticos, como la crónica y la fotografía. 

<p>Aunque no parezca por mi rostro de eterna quinceañera, estoy próxima a cumplir veinte años el 27 de agosto. Si bien no tengo un apodo para mis amistades, en general, me gusta que se refieran a mi como Suni o Su. Incluso, mi padre suele llamarme de diversas maneras dependiendo de su humor. Los más usados cuando está feliz y tranquilo son Chuky, Chacabuco o Chacabuquito, Tasmania y la lista continúa. 

<p>En mi casa, somos cuatro: mi papá, mi abuela, Gamora (mi perro) y yo. Lamentablemente, mi mamá falleció cuando tenía siete años; a pesar de ello, me siento feliz y agradecida con mi familia, sobre todo con el señor Juan (mi padre), quien me ha inculcado valores como el respeto y la responsabilidad. Recuerdo que en lugar de ver dibujos animados, mi mamá Justina (abuela) y yo nos sentábamos a las 6 de la tarde para ver “La Rosa de Guadalupe”. Así fue como crecí con el melodrama, parte fundamental en mi personalidad.
                 
<p>De esa manera, desarrollé mi afinidad por las novelas desde muy pequeña. Mi preferida es una novela turca: “¿Qué culpa tiene Fatmagul?” Al llegar a la universidad, me interesaron las lecturas feministas y, con el curso de Narrativa dictado por la profesora Wurst en Letras, descubrí mi pasión por la literatura; especialmente por los cuentos escritos por autoras latinoamericanas como Mónica Ojeda, Agustina Bazterrica, Fernanda Ampuero, Samanta Schweblin y Mariana Enríquez. Toda esta influencia femenina, me han direccionado al estudio de géneros, al punto de cuestionarme constantemente qué es ser mujer. """
    
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
    
    col2.image("Fotografía.jpg", caption='Desde mi lado sincero y divertido', width=300)
    texto_3 = """ 
    <p>Me gusta leer distintos géneros, entre mis preferidos distopías y horror; Las cosas que perdimos en el fuego de Enríquez y la Subasta de Ampuero, son mis preferidas por referirse al cuerpo femenino desde lo abyecto. La motivación hacia estos temas, hizo que escribiera un ensayo sobre la maternidad ominosa para Los Juegos Florales el año pasado, obteniendo así el segundo puesto en la categoría ensayo. 

<p>Asimismo, desarrollé una fascinación por las películas del UCM a los 10 años en el preciso instante que miré La Era de Ultron. A pesar de su poco acogida por la audiencia, cada minuto estuve al borde de la silla y al finalizar solo quería saber más de esos superhéroes a los que jamás había prestado atención. También, me agrada realizar actividades en compañía de mis amigas y mi familia, especialmente mis primos y primas. A veces, simplemente nos juntamos en mi casa para ver una película o en otros casos salimos a algún lugar sin objetivo más que mero entretenimiento. Considero que son esas personas, incluida mi familia nuclear, las más importantes en mi vida. """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Mis personas favoritas")
    col3, col4 , col5, col6= st.columns(4)
    col3.image("abuelita.jpg", width=300)
    col3.image("amix3.jpg", width=300)
    col4.image("amix2.jpg", width=300)
    col5.image("amix1.jpg", width=300)
    col6.image("gamora.jpg",width=300)
    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>No es tan complicado programar cuando tienes apoyo 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    <p>En un inicio, escribir fechas o simplemente ejecutar una palabra con print era tan sencillo. Al avanzar las prácticas, el nivel se incrementó y mi aprendizaje se vio en jaque al no entender que estábamos haciendo. No obstante, el desempeño de la jefa de práctica Luisa incidió en la solución de los ejercicios planteados. Desde mi experiencia, su predisposición con sus estudiantes aportó en el interés por el curso. Su compromiso, dedicación y entre otras cualidades facilitaron la comprensión de lo complejo que resultaban algunos códigos. 
 
<p>Mi parte favorita, y a la vez frustrante, era desarrollar los ejercicios de repaso para las primeras PCs. Pasé noches enteras tratando de arreglar el código y de entender el porqué del error. El tema de importar un PDF o una base de datos me sacaron ojeras por una semana, sumado a ello la desesperación, mientras que la solución se hallaba en la ortografía. Con la compañía de Luisa, programar en Colab y Visual Studio Code se convirtió en entretenido: el mundo de la programación simplifica nuestra realidad, aunque te compliques toda una vida. 

<p>Aparte de la JP, mi enamorado fue pieza clave en este curso. Sus conocimientos en programación adquiridos por su carrera de Ingeniería Mecatrónica simplificaron los ejercicios a entendibles, incluso cuando parecían imposibles. Un café Kirma y su presencia en las madrugadas determinaron la compresión de temas como las condicionales (if-elif-else) y los bucles (for y while) por una sola razón: mi salud mental se vio trastocada al punto de converger en la locura debido a la funcionalidad de range  y break. 

<p>Hoy en día, considero que el lenguaje de programación resulta beneficioso para todo ámbito. En un futuro, me gustaría generar un juego multijugador que permita mejorar los cuatros ejes básicos para aprender el idioma: reading, listening, writing y speaking. La particularidad de este producto radica en que cada jugador puede escoger la temática que mejor dominé; de esa manera, puede generar un equipo con sus amigos y así empezar por un camino que requiera cada una de sus habilidades. 
 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Jugar y programar: Una fusión única 🎥</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://www.youtube.com/watch?v=kKu_u58KoUY")
    
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    # st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Estadística con Python resulta más sencillo e interactivo</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Word Cloud on fact-checking', 'Gráfico de barras horizontales de familias lingüísticas', 'Mapa 5 películas favoritas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Word Cloud on fact-checking':
        st.markdown("<div style='text-align: justify; font-size: 20px;'> <p>¿Cómo tener la certeza de que una noticia sobre el COVID-19 expuesta en las redes sociales está certificada por un especialista de la salud? Por medio de un recurso interactivo como una nube de palabras creada con el programa Python, el usuario podrá identificar palabras clave en un contenido de salud difundido en la red social que contenga información veraz. De esta manera, se logrará determinar el grado de credibilidad de la información expuesta en distintos medios que ofrece Internet. <p>Con Word Cloud on fact-checking, la clasificación de contenidos informativos y desinformativos contribuye a dimensionar el impacto de la desinformación en variadas plataformas. A partir de esta herramienta, se busca destacar la importancia de implementar estrategias de verificación de información (fact-checking) y alfabetización digital como medidas necesarias para contrarrestar la propagación de noticias falsas sobre salud en redes sociales.</div>", unsafe_allow_html=True)
        st.image("nube_fact_checking.png", caption='Nube de palabras: Identificación veraz de noticias sobre salud', width=700)
        pass
    elif grafico_seleccionado == 'Gráfico de barras horizontales de familias lingüísticas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'> <p>Sabías que existieron 102 lenguas originarias y actualmente solo quedan 47. Según el registro oficial del Ministerio de Cultura, reconoce el uso activo de 47 lenguas, aunque algunas de ellas se encuentren en peligro de extinción; mientras que el primer dato incluye a lenguas ya extintas. Sin embargo, esta clasificación extensa deriva de las variantes dialectales que algunos académicos consideran pertinente. Loukotka (1968) reconocía más de 90 familias lingüísticas con subdivisiones en el área amazónica. <p>A partir de una base de datos, que identifica 102 lenguas originarias, se realizó un gráfico de barras de la cantidad de lenguas originarias por Familias Lingüísticas. Este recurso fue creado con Python, lo cual permitió sintetizar la información de manera didáctica para la comprensión del lector. Asimismo, se identificó un número de 17 familias, entre ellas Quechuan, la cual agrupa alrededor de 35 lenguas originarias.</div>", unsafe_allow_html=True)
        st.image("lenguas_originarias.png", caption='Gráfico de familias lingüísticas', width=700)
        pass
    elif grafico_seleccionado == 'Mapa 5 películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>Si eres un amante del cine, esta herramienta te gustará, ya que podrás identificar la diversidad de producciones alrededor del mundo. Imagina tu top 5 de películas y distribuyelas en puntos sobre el globo terráqueo. Esta imagen preconcebida es posible con el programa Python a partir de importar la librería Folium. De esta manera, ubiqué los films de mi preferencia en un mapa, después de desarrollar una lista, aunque infinita, seleccioné producciones significativas para mí: The Shape of Water de Guillermo del Toro, Amelie de Jean-Pierre Jeunet, La vita e bella de Roberto Benigni, Before Sunrise de Richard Linklater y The Pianist de Roman Polanski. </div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_descargar.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    
