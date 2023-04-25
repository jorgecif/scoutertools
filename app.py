import streamlit as st
from streamlit_option_menu import option_menu
import PIL.Image
import unicodedata
import string



# Page config
st.set_page_config(
	page_title="Scouter Tools",
	page_icon="random",
	layout="centered",
	initial_sidebar_state="expanded",
	)

# Oculto botones de Streamlit - fondo de sidebar
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid=stSidebar] {
                background-color: #6E20A0;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# Color morado #9b51e0


# Funciones



# Logo sidebar
image =  PIL.Image.open('logoscoutscol.png')
st.sidebar.image(image,width=None, use_column_width=None )

with st.sidebar:
    selected = option_menu(
            menu_title="Scouter tools",  # required
            options=["Home", "Traductor de claves", "Jefe Scout Virtual", "Contacto"],  # required
            icons=["house", "caret-right-fill",  "caret-right-fill","envelope"],  # optional
            menu_icon="upc-scan",  # optional
            default_index=0,  # optional
        )


if selected == "Home":
    st.title("Herramientas para dirigentes scouts ")
    st.write("Esta aplicación recopila algunas herramientas para apoyar a los dirigentes scout en la elaboración del programa scout.")

    st.write("Selecciona la herramienta del menú de la izquierda para iniciar")



if selected == "Traductor de claves":
    st.title(f"Herramienta:  {selected}")
    image =  PIL.Image.open('cifrado.jpg')
    st.image(image,width=None, use_column_width=True )
    url = 'https://clavescout.streamlit.app/'

    st.markdown(f'''
    <div style="text-align:center">
    <a href={url}><button style="
    background-color:#ff4b4b;
    color:#ffff;
    ">Abrir traductor de claves scout</button></a>
    </div>

    ''',
    unsafe_allow_html=True)
    # Get user input


if selected == "Jefe Scout Virtual":
    st.title(f"Herramienta:  {selected}")
    image =  PIL.Image.open('cifrado.jpg')
    st.image(image,width=None, use_column_width=True )
    # Get user input


    url = "https://ora.sh/fierce-turquoise-lxym/jefescoutvirtual"

    st.markdown(f'''
    <div style="text-align:center">
    <a href={url}><button style="
    background-color:#ff4b4b;
    color:#ffff;
    ">Contactar al Jefe Scout Virtual</button></a>
    </div>
    ''',
    unsafe_allow_html=True)

if selected == "opcion2":
    st.title(f"You have selected {selected}")


if selected == "opcion3":
    st.title(f"You have selected {selected}")

if selected == "Contacto":
    st.title(f"Créditos y {selected}")
    st.subheader("Esta aplicación ha sido desarrollada por Jorge O. Cifuentes (Águila Vigilante)")
    st.subheader("Grupo 10 Meraki - Girón, Santander")
    st.write('Email: *jorgecif@gmail.com* :heart: :fleur_de_lis:')
    st.write("Scouter Tools")
    st.write("Version 1.0")
    st.text("")
