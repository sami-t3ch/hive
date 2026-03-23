# 04 MANUAL DE OPTIMIZACIÓN PRÁCTICA (QUEEN BEE & TOKENS)

Este manual aborda los problemas más comunes al usar el framework Hive (Aden) en la práctica: **el gasto excesivo de tokens, las preguntas técnicas repetitivas de la "Queen Bee" y la dificultad para cargar documentación de contexto.**

---

## 🛑 Problema 1: La Queen Bee hace demasiadas preguntas técnicas
La "Queen Bee" (agente codificador) está programada para generar el código y el grafo exacto de tu agente. Si le das una instrucción vaga ("Crea un agente de ventas"), intentará llenar los huecos de arquitectura haciéndote decenas de preguntas técnicas.

### ✅ Solución: "Goal-Driven" Estricto
No hables con la Queen Bee como si fuera ChatGPT. Entrégale un **"Briefing" completo** desde el primer mensaje que incluya:
1. **Objetivo (Goal):** Qué debe lograr el agente.
2. **Criterio de Éxito:** Cómo saber que terminó satisfactoriamente.
3. **Restricciones Técnicas:** Qué herramientas tiene permitido usar y cuáles no.
4. **Nodos (Pasos):** Un resumen general de los pasos. 

**Ejemplo de Prompt Óptimo:**
> "Quiero construir un agente llamado 'TicketHandler'. Su objetivo es categorizar tickets de soporte. Debe tener 2 nodos: uno para 'analizar_texto' y otro para 'asignar_prioridad'. Usa las herramientas estándar. No me preguntes por edge-cases, asume configuraciones por defecto para todo y genera el código del agente ahora."

---

## 🛑 Problema 2: Gasto masivo de Tokens (Explosión de Contexto)
Si intentas pasarle un PDF gigante de 50 páginas o el historial de logs directo en la conversación, el contexto (y tu presupuesto) colapsará rápidamente, y el agente se volverá lento y propenso a alucinaciones.

### ✅ Solución: El Patrón de Punteros (Pointer Pattern)
Nunca inyectes datos completos en el prompt. Hive tiene herramientas del sistema de archivos (`file_system_toolkits`).
1. Guarda tu documentación de ejemplo en la carpeta raíz (por ejemplo: `mi_documentacion.txt`).
2. Asígnale al agente la herramienta de lectura de archivos.
3. En el prompt del nodo, dile: *"Usa la herramienta de lectura para analizar el archivo `mi_documentacion.txt` línea por línea solo cuando sea necesario"*.

Esto obliga al nodo trabajador a acceder a la información a demanda (Memoria RLM) en lugar de cargar los 30,000 tokens en la memoria de la Queen Bee durante la fase de ensamblaje.

---

## 🛑 Problema 3: Complejidad para probar un agente recién creado
A veces la Queen Bee genera el agente en la carpeta `exports/`, pero al intentar ejecutarlo manualmente falla por falta de importaciones o configuraciones.

### ✅ Solución: TUI y Scripts Automatizados
No intentes ensamblar los comandos de consola manualmente. 
1. Usa el script interactivo proporcionado por Zeta: `python scripts/zeta/hive_boot.py` o los blueprints automáticos.
2. Usa el Dashboard interactivo escribiendo `hive tui` en tu terminal para probar los agentes visualmente.
3. Si el agente requiere validación, corre `uv run python -m exports.tu_agente validate`, lo cual limpiará errores tontos de dependencias antes de gastar tokens en ejecución real.
