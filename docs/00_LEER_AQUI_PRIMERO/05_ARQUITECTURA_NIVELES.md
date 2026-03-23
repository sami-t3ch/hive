# 05 ARQUITECTURA POR NIVELES DE PRIORIDAD

La arquitectura del ecosistema **Aden (Hive)** se divide en un modelo de Sistemas Multi-Agentes Orientados a Objetivos (Goal-Driven). La siguiente estructuración clasifica los módulos del _core framework_ (`core/framework/`) por su criticidad operativa:

---

## 🔴 1. ESENCIAL (El corazón del sistema)
Sin estos módulos, el framework es inoperable. Definen la estructura de pensamiento, los esquemas de datos y el motor de ejecución interno.

*   **`runtime/`**: Contiene `agent_runtime.py` y `execution_stream.py`. Es el motor base (event-loop) que mantiene vivos y en comunicación a los agentes. Administra los ciclos de vida de cada tarea.
*   **`graph/`**: El enrutador. Al no haber conexiones fijas predefinidas entre tareas, este módulo determina la lógica de cómo un agente pasa su resultado al siguiente (los Edges y Nodes generados dinámicamente).
*   **`schemas/`**: Los planos estructurales. Define estrictamente con _Pydantic_ la forma exacta que debe tener cada dato que entra y sale, garantizando que los LLMs no rompan el formato de datos durante la ejecución.

---

## 🟠 2. IMPERANTE (La orquestación)
Son los cerebros principales que conectan los hilos, leen las instrucciones del usuario y lanzan las misiones.

*   **`agents/` (Queen/Zeta):** Contiene a los Agentes Codificadores / Coordinadores principales. Son las IAs meta-cognitivas encargadas de leer el objetivo (goal) del usuario y escribir el grafo interactivo (JSON) de manera dinámica.
*   **`runner/`**: Incluye el `AgentRunner`. Su trabajo es compilar el archivo generado por los agentes (`agent.json`, `tools.py`) en memoria y comenzar su inyección ininterrumpida hacia el motor `runtime`.
*   **`llm/`**: El puente traductor. Adapta la comunicación vía LiteLLM para que el sistema opere indistintamente con OpenAI, Anthropic (Claude), Gemini local o cualquier otro proveedor de modelos.

---

## 🟡 3. CRÍTICO (Memoria y Seguridad)
Estos módulos aseguran que el framework sea confiable, predecible y retenga el contexto conversacional sin explotar por exceso de tokens. Perderlos significa perder la sesión.

*   **`server/`**: Incluye el `session_manager.py`. Maneja múltiples sesiones paralelas, evitando cruces de datos (sangrado de memoria) entre el Agente A y el Agente B.
*   **`credentials/`**: La bóveda. Gestiona de forma local y segura el acceso a las llaves maestras de las herramientas externas (Tokens de GitHub, Discord, APIs comerciales, etc.).
*   **`storage/`**: Archiva el historial de mensajes de la memoria RLM para las "memorias compartidas", pilar fundamental para operar el Patrón de Punteros en documentos grandes.

---

## ⚠️ 4. ADVERTENCIA (Sistemas Inestables / Externos)
Módulos dependientes de factores externos (latencia de red, configuración del host). Son los puntos de fallo más comunes al operar y requieren monitoreo constante.

*   **`tools/` y `skills/`**: Incluye los envoltorios (SDK-wrapped nodes) correspondientes a herramientas de búsqueda web, manipulación de archivos y navegación. Es el principal vector de error por "alucinación de herramientas" del LLM.
*   **`mcp/` (Model Context Protocol):** La conexión en vivo hacia servidores externos, bases de datos u otras máquinas. Alta probabilidad de fallos si Docker, WSL o los puertos de red están mal mapeados.
*   **`observability/` & `monitoring/`**: Rastrean, evalúan salud y analizan errores. Si el `Judge` (juez evaluador) tiene latencias, el agente puede quedarse colgado (stalled) en un bucle ciego.

---

## ⚪ 5. SIN / OPCIONALES (Soporte Periférico)
Módulos puramente utilitarios para el desarrollador, pruebas individuales o interfaces gráficas. El código backend _headless_ puede operar sin ellos.

*   **`cli.py` / `tui/`**: Las interfaces ricas de línea de comandos y el dashboard interactivo de terminal local (`hive tui`).
*   **`debugger/` y `testing/`**: Utilidades para inyectar y forzar fallos (Constraint tests, Success tests) durante la fase de validación de un agente con `uv run python -m ... test`.
*   **`specializers/` y `utils/`**: Prompts de sistema adicionales y funciones matemáticas/string de normalización de punteros que operan en segundo plano de modo silencioso.
