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

tab_ver, tab_guardar = st.tabs(["Ver jugadores", "Guardar jugador"])

with tab_ver:
    if datos and 'jugadores' in datos:
        st.dataframe(datos['jugadores'])
    else:
        st.write("No hay jugadores registrados")

with tab_guardar:
    with st.form("inscripcion_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)

        with c1:
            nombre = st.text_input("Nombre del jugador")
            pie = st.selectbox("Pie del jugador", ["Izquierdo", "Derecho"])
            pieDebil = st.number_input("Pie débil del jugador", min_value=0.0, max_value=5.0, value=2.5, step=0.1)
            st.empty()
            ritmo = st.number_input("Ritmo del jugador", min_value=1, max_value=100, value=50, step=1)
            aceleracion = st.number_input("Aceleración del jugador", min_value=1, max_value=100, value=50, step=1)
            velocidad = st.number_input("Velocidad del jugador", min_value=1, max_value=100, value=50, step=1)
            st.empty()
            regate = st.number_input("Regate del jugador", min_value=1, max_value=100, value=50, step=1)
            agilidad = st.number_input("Agilidad del jugador", min_value=1, max_value=100, value=50, step=1)
            equilibrio = st.number_input("Equilibrio del jugador", min_value=1, max_value=100, value=50, step=1)
            reacciones = st.number_input("Reacciones del jugador", min_value=1, max_value=100, value=50, step=1)
            controlBalon = st.number_input("Control de balón del jugador", min_value=1, max_value=100, value=50, step=1)
            regatesBalon = st.number_input("Regates de balón del jugador", min_value=1, max_value=100, value=50, step=1)
            compostura = st.number_input("Compostura del jugador", min_value=1, max_value=100, value=50, step=1)
            playStyles = st.selectbox("Play styles del jugador", ["Pase Largo"])

        with c2:
            overall = st.number_input("Overall del jugador", min_value=1, max_value=100, value=50, step=1)
            posicion = st.selectbox("Posición del jugador", ["POR", "DFC", "LD", "LI", "MCD", "MC", "MCO", "ED", "EI", "DC"])
            movimientoHabilidad = st.number_input("Movimiento de habilidad del jugador", min_value=0.0, max_value=5.0, value=2.5, step=0.1)
            st.empty()
            tiro = st.number_input("Tiro del jugador", min_value=1, max_value=100, value=50, step=1)
            posicionTiro = st.selectbox("Posición de tiro del jugador", min_value=1, max_value=100, value=50, step=1)
            definicion = st.number_input("Definición del jugador", min_value=1, max_value=100, value=50, step=1)
            fuerzaTiro = st.number_input("Fuerza de tiro del jugador", min_value=1, max_value=100, value=50, step=1)
            tirosLargos = st.number_input("Tiros largos del jugador", min_value=1, max_value=100, value=50, step=1)
            voleas = st.number_input("Voleas del jugador", min_value=1, max_value=100, value=50, step=1)
            penales = st.number_input("Penales del jugador", min_value=1, max_value=100, value=50, step=1)
            st.empty()
            defensa = st.number_input("Defensa del jugador", min_value=1, max_value=100, value=50, step=1)
            intercepciones = st.number_input("Intercepciones del jugador", min_value=1, max_value=100, value=50, step=1)
            precisionCabeceo = st.number_input("Precisión de cabeceo del jugador", min_value=1, max_value=100, value=50, step=1)
            percepcionDefensiva = st.number_input("Percepción defensiva del jugador", min_value=1, max_value=100, value=50, step=1)
            entradaFrente = st.number_input("Entrada frente del jugador", min_value=1, max_value=100, value=50, step=1)
            barrida = st.number_input("Barrida del jugador", min_value=1, max_value=100, value=50, step=1)


        with c3:
            edad = st.number_input("Edad del jugador", min_value=15, max_value=50, value=15, step=1)
            potencial = st.number_input("Potencial del jugador", min_value=1, max_value=100, value=50, step=1)
            posicionesAlternativas = st.multiselect("Posiciones alternativas del jugador", ["POR", "DFC", "LD", "LI", "MCD", "MC", "MCO", "ED", "EI", "DC"])
            st.empty()
            pase = st.number_input("Pase del jugador", min_value=1, max_value=100, value=50, step=1)
            vision = st.number_input("Vision del jugador", min_value=1, max_value=100, value=50, step=1)
            centro = st.number_input("Centro del jugador", min_value=1, max_value=100, value=50, step=1)
            precisionTiroLibre = st.number_input("Precisión de tiro libre del jugador", min_value=1, max_value=100, value=50, step=1)
            pasesCortos = st.number_input("Pases cortos del jugador", min_value=1, max_value=100, value=50, step=1)
            pasesLargos = st.number_input("Pases largos del jugador", min_value=1, max_value=100, value=50, step=1)
            efecto = st.number_input("Efecto del jugador", min_value=1, max_value=100, value=50, step=1)
            st.empty()
            fisico = st.number_input("Fisico del jugador", min_value=1, max_value=100, value=50, step=1)
            salto = st.number_input("Salto del jugador", min_value=1, max_value=100, value=50, step=1)
            energia = st.number_input("Energía del jugador", min_value=1, max_value=100, value=50, step=1)
            fuerzaFisica = st.number_input("Fuerza física del jugador", min_value=1, max_value=100, value=50, step=1)
            agresion = st.number_input("Agresión del jugador", min_value=1, max_value=100, value=50, step=1)


        guardar = st.form_submit_button("Guardar jugador")

        if guardar:
            if nombre and posicion and edad:
                crecimiento = potencial - overall
                datos['jugadores'].append({
                    "nombre": nombre,
                    "pie": pie,
                    "pieDebil": pieDebil,
                    "ritmo": ritmo,
                    "aceleracion": aceleracion,
                    "velocidad": velocidad,
                    "regate": regate,
                    "agilidad": agilidad,
                    "equilibrio": equilibrio,
                    "reacciones": reacciones,
                    "controlBalon": controlBalon,
                    "regatesBalon": regatesBalon,
                    "compostura": compostura,
                    "playStyles": playStyles,
                    "overall": overall,
                    "posicion": posicion,
                    "movimientoHabilidad": movimientoHabilidad,
                    "tiro": tiro,
                    "definicion": definicion,
                    "fuerzaTiro": fuerzaTiro,
                    "tirosLargos": tirosLargos,
                    "voleas": voleas,
                    "penales": penales,
                    "defensa": defensa,
                    "intercepciones": intercepciones,
                    "precisionCabeceo": precisionCabeceo,
                    "percepcionDefensiva": percepcionDefensiva,
                    "entradaFrente": entradaFrente,
                    "barrida": barrida,
                    "edad": edad,
                    "potencial": potencial,
                    "posicionesAlternativas": posicionesAlternativas,
                    "pase": pase,
                    "vision": vision,
                    "centro": centro,
                    "precisionTiroLibre": precisionTiroLibre,
                    "pasesCortos": pasesCortos,
                    "pasesLargos": pasesLargos,
                    "efecto": efecto,
                    "fisico": fisico,
                    "salto": salto,
                    "energia": energia,
                    "fuerzaFisica": fuerzaFisica,
                    "agresion": agresion,
                    "crecimiento": crecimiento
                })
                with open('plantilla_fc27.json', 'w', encoding='utf-8') as f:
                    json.dump(datos, f, ensure_ascii=False, indent=4)
                st.success("Jugador guardado correctamente")
                st.write(datos['jugadores'])
            else:
                st.error("Por favor, complete todos los campos")