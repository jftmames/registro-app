import streamlit as st
import yaml
import hashlib
from pathlib import Path

# Configuración inicial
st.set_page_config(page_title="App Registro Jurídico", layout="centered")

# Cargar reglas desde YAML
def load_rules():
    with open("data/rules.yml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Evaluador simple: busca reglas que coincidan con los hechos
def evaluate_case(facts, rules):
    triggered = []
    analysis = []
    for rule in rules.get("reglas", []):
        if rule["id"] in facts.get("tipo_caso", ""):
            triggered.append(rule["id"])
            analysis.append(rule["analisis"])
    return triggered, "\n".join(analysis)

# Cargar plantilla
def load_template():
    with open("data/templates/dictamen.md", "r", encoding="utf-8") as f:
        return f.read()

# Generar dictamen en Markdown
def build_dictamen(facts, analysis, conclusion):
    template = load_template()
    md = template.format(
        hechos=facts.get("detalle", ""),
        cuestiones=facts.get("tipo_caso", ""),
        analisis=analysis,
        conclusion=conclusion,
        riesgos="Revisar posibles impugnaciones o litigios.",
        pasos="Consultar Registro e iniciar medidas preventivas."
    )
    return md

# Calcular hash
def calculate_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# Casos demo
demo_cases = {
    "Doble venta": {"tipo_caso": "doble_venta", "detalle": "Se vendió el mismo inmueble a dos compradores."},
    "Administrador no inscrito": {"tipo_caso": "admin_no_inscrito", "detalle": "Administrador no inscrito actúa en nombre de la sociedad."}
}

st.title("📑 App Registro Jurídico")
st.markdown("Tema: **B2 Registro: prioridad, publicidad, oponibilidad, tracto** (España/UE)")

rules = load_rules()

# Selección de demo o manual
modo = st.radio("Selecciona modo de entrada:", ["Manual", "Caso demo"])

facts = {}
if modo == "Manual":
    facts["tipo_caso"] = st.text_input("Tipo de caso (ej: doble_venta, admin_no_inscrito)", placeholder="doble_venta")
    facts["detalle"] = st.text_area("Detalle del caso", placeholder="Describe brevemente los hechos relevantes...")
else:
    demo = st.selectbox("Elige un caso demo:", list(demo_cases.keys()))
    facts = demo_cases[demo]
    st.write("**Hechos cargados:**", facts)

if st.button("Evaluar"):
    triggered, analysis = evaluate_case(facts, rules)
    if not triggered:
        st.warning("No se activaron reglas. Revisa el tipo de caso.")
    else:
        st.success(f"Reglas activadas: {', '.join(triggered)}")
        dictamen = build_dictamen(facts, analysis, conclusion="Dictamen generado según reglas registrales.")
        h = calculate_hash(dictamen)

        st.subheader("📄 Dictamen")
        st.markdown(dictamen)

        st.subheader("🔒 Hash SHA-256")
        st.code(h)

        st.download_button("Descargar dictamen .md", dictamen, file_name="dictamen.md", mime="text/markdown")
