import json 
import streamlit as st

try:
    with open('plantilla_fc27.json', encoding='utf-8') as f:
        datos = json.load(f)
        print(datos['jugadores'])
except json.JSONDecodeError:
    print("Error al cargar el archivo JSON")
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Error: {e}")


st.set_page_config(page_title="Formulario de Inscripción", page_icon=":tada:", layout="wide")
st.title("Formulario de Inscripción")
st.subheader("Por favor, ingrese sus datos")

with st.form("inscripcion_form", clear_on_submit=True):
    c1, c2, c3 = st.columns(3)

    with c1:
        nombre = st.text_input("Nombre del jugador")
        posicion = st.selectbox("Posición del jugador", ["POR", "DFC", "LD", "LI", "MCD", "MC", "MCO", "ED", "EI", "DC"])
        edad = st.number_input("Edad del jugador", min_value=15, max_value=50, value=15, step=1)

    with c2:
        overall = st.number_input("Overall del jugador", min_value=1, max_value=100, value=50, step=1)
        potencial = st.number_input("Potencial del jugador", min_value=1, max_value=100, value=50, step=1)
        ritmo = st.number_input("Ritmo del jugador", min_value=1, max_value=100, value=50, step=1)


    with c3:
        pase = st.number_input("Pase del jugador", min_value=1, max_value=100, value=50, step=1)
        regate = st.number_input("Regate del jugador", min_value=1, max_value=100, value=50, step=1)

    guardar = st.form_submit_button("Guardar jugador")

    if guardar:
        if nombre and posicion and edad:
            datos['jugadores'].append({
                "nombre": nombre,
                "posicion": posicion,
                "edad": edad,
                "overall": overall,
                "potencial": potencial,
                "ritmo": ritmo,
                "pase": pase,
                "regate": regate,
            })
            with open('plantilla_fc27.json', 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
            st.success("Jugador guardado correctamente")
            st.write(datos['jugadores'])
        else:
            st.error("Por favor, complete todos los campos")