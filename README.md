# 📑 App Registro Jurídico (España/UE)

Aplicación en **Streamlit** para juristas sobre **B2 Registro: prioridad, publicidad, oponibilidad, tracto**.  
Permite capturar hechos de caso, evaluar reglas desde YAML, generar dictamen descargable en Markdown y calcular su hash SHA-256 como evidencia de integridad.

---

## 🚀 Pasos para desplegar en la web

1. **Crear repositorio en GitHub**
   - Ve a [GitHub](https://github.com) y crea un repo nuevo, por ejemplo: `registro-app`.
   - Sube los archivos indicados en este proyecto con la misma estructura de carpetas.

2. **Estructura mínima de archivos**

registro-app/
├── README.md
├── requirements.txt
├── app.py
├── data/
│ ├── rules.yml
│ └── templates/
│ └── dictamen.md
└── .streamlit/
└── config.toml



3. **Configurar Streamlit Cloud**
- Entra en [Streamlit Cloud](https://streamlit.io/cloud).
- Crea nueva app y conecta con tu repo de GitHub.
- Selecciona `app.py` como archivo principal.

4. **Probar con los escenarios de ejemplo**
- Una vez desplegado, abre tu app en la URL que genere Streamlit.
- Carga un caso manualmente o usa los **2 casos demo precargados** (ver abajo).

---

## 🧪 Escenarios de prueba

### Escenario 1: Doble venta de inmueble
- **Hechos introducidos:**
- Tipo de caso: `doble_venta`
- Detalle: "Se vendió el mismo inmueble a dos compradores distintos."
- **Conclusión esperada:**
- El comprador que inscribió primero adquiere prioridad registral.
- Riesgo: posible litigio del comprador no protegido.

### Escenario 2: Administrador no inscrito
- **Hechos introducidos:**
- Tipo de caso: `admin_no_inscrito`
- Detalle: "Administrador nombrado no consta en el Registro Mercantil."
- **Conclusión esperada:**
- El acto realizado carece de eficacia frente a terceros.
- Riesgo: impugnación por defecto de representación.

---
