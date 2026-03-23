# 01 ÍNDICE MAESTRO

Bienvenido al repositorio. Para evitar errores al iniciar los agentes locales (Zeta, Codex) o el entorno de integración completo, lee este índice para saber qué encontrarás aquí.

## Estructura de Documentación

### 📂 `00_LEER_AQUI_PRIMERO/`
Contiene la información crítica de seguridad, ejecución (Docker/Windows) y gestión de código (Git Flow) que debes dominar antes de tocar ramas o correr dependencias.
- `01_INDICE_MAESTRO.md`: Este archivo.
- `02_GIT_WORKFLOW.md`: Instrucciones sobre cómo trabajar con el código sin romper la rama `main` oficial de Aden y cómo empujar a tu fork `sami-t3ch`.
- `03_RUTAS_Y_DOCKER_WINDOWS.md`: Solución de problemas específicos y requerimientos mínimos si operas Docker Desktop sobre Windows WSL2 o PowerShell.

### 📂 `01_ZETA_CODEX_AI/` (Anteriormente `codex-ai-zeta-main`)
Contiene los manuales extendidos, guías de prompts, diccionarios y propuestas de modernización técnica creadas durante las mejoras de *Zeta*.
*Abre el `00_index.md` dentro de esta carpeta para profundizar en la simbiosis IA y lineamientos.*

### 📂 `02_POTENCIALES_Y_MEJORAS/`
Contiene los análisis de fallas iterativas, revisiones de arquitectura, y propuestas de mejoras técnicas y visuales del proyecto. Ideal para planificar el siguiente paso de código.

---

## 🏛️ Documentación Oficial de Aden Framework (Raíz de `docs/`)
Todo lo que está suelto en la carpeta raíz `docs/` o dentro de carpetas como `architecture/` o `bounty-program/` corresponde al proyecto base (`aden-hive/hive`). 
No renombres ni borres estas carpetas, ya que podrían romper la página web oficial de documentación del framework.

- **`getting-started.md`**: Para arrancar el core de Hive y entender los componentes principales (`framework`, `tools`).
- **`developer-guide.md`**: Guía exhaustiva de buenas prácticas, diseño de paquetes y cómo escribir tests.

---

> **Regla Principal de Trabajo:** 
> 1. Asegúrate de estar trabajando sobre la rama `feature/sami-integrations` o generar una nueva rama con `git checkout -b feature/lo-que-sea`. 
> 2. Mantén `main` intacta y sincronízala mediante `git pull upstream main`.
