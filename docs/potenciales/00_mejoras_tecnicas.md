# 🚀 Mejoras Técnicas (Protocolo Zeta)

## 1. Biblioteca de Documentos (Knowledge Layer)
**Deficiencia Actual:** Los agentes dependen de `load_data` para archivos específicos, lo que requiere que el agente "sepa" qué archivo buscar. No hay una capa de recuperación semántica (RAG) nativa.

**Propuesta:** 
*   **Integración en `SharedMemory`:** Extender `SharedMemory` para soportar un `VectorStore` (Chroma/Pinecone) autohospedado en `~/.hive/knowledge`.
*   **Persistent Context:** Permitir que los agentes "ingieran" carpetas de documentación entera durante la fase de inicialización de la **Queen Bee**.
*   **Tooling:** Crear una herramienta `semantic_search(query)` que permita consultar la biblioteca sin conocer los nombres de los archivos.

## 2. Especializador de Agentes (Expert Seeding)
**Deficiencia Actual:** Los agentes se especializan mediante prompts largos en cada nodo. Esto es ineficiente y consume tokens repetitivamente.

**Propuesta:**
*   **Domain Personas:** Crear una carpeta `core/framework/specializers` donde se almacenen perfiles de expertos (Seguridad, Frontend, Web3).
*   **Context Pre-seeding:** En `AgentRuntime.py`, inyectar un "Expert Module" en la capa 1 de la `PromptOnion` basado en el `agent_type`.
*   **Fine-Tuning on-the-fly:** Usar los fallos capturados por el `Judge` para crear "Rules of Thumb" dinámicas que especialicen al agente en su dominio específico a medida que evoluciona.

## 3. Optimización del Puntero de Memoria
*   **Compresión Dinámica:** En lugar de solo truncar a 30KB, implementar un `summary_bridge` que resuma los resultados de herramientas largos antes de enviarlos al `spillover_dir`.

## 4. Desplegador de Estabilidad (Hive-Boot)
**Deficiencia Actual:** La inicialización depende de scripts manuales (`quickstart.sh`) que no verifican el estado del sistema en ejecución.

**Propuesta:**
*   **Health Check Pre-flight:** Un comando `hive-boot check` que verifique latencia de APIs, integridad de `SharedMemory` y validez de credenciales antes de lanzar el `QueenBee`.
*   **Auto-Healing de Infraestructura:** Si un servidor MCP falla, el desplegador debe intentar reiniciarlo o buscar un endpoint alternativo automáticamente.
*   **Ambiente Aislado Nativo:** Integración nativa con `uvx` para ejecutar herramientas MCP en contenedores efímeros, garantizando que una herramienta rota no comprometa la estabilidad del enjambre.
*   **Watchdog de Agentes:** Un proceso 'Sidecar' que detecte si un agente ha entrado en un bucle infinito (costo desmedido sin progreso en el `Judge`) y lo termine de forma segura.

## 5. Integraciones de Infraestructura (Módulos de Despliegue)
Para una autonomía total y privacidad de grado Zeta, Hive debe integrar motores de núcleo en su capa de despliegue:

### A. SearXNG: Meta-Buscador Privado (Search Provider)
*   **Rol:** Reemplazar dependencias de APIs externas (Brave/Google) por una instancia local de SearXNG.
*   **Integración:** Desplegado como un contenedor 'Sidecar' por el **Desplegador** (`hive-boot`). Hive se conecta a esta instancia privada, permitiendo que miles de agentes busquen información simultáneamente sin ser bloqueados por rate-limits externos y manteniendo el rastro de búsqueda 100% privado.

### B. Scrapling: Motor de Extracción de Alta Densidad
*   **Rol:** Reemplazar la dependencia actual de Playwright/BS4 en `web_scrape_tool.py` por Scrapling.
*   **Integración:** Scrapling permite una velocidad de extracción hasta 20x superior. Se integrará como el motor por defecto en `aden_tools`, permitiendo que el agente maneje "Stealth" y "Auto-Headers" sin sobrecarga de memoria, optimizando la ejecución de Workers en hardware limitado.

### C. MkDocs: Factoría de Documentación Dinámica
*   **Rol:** Transformar la "Memoria del Enjambre" en una base de conocimientos legible.
*   **Integración:** Un `SessionListener` en el core que captura cada `Checkpoint` de la base de datos y lo convierte en un archivo `.md` estructurado. MkDocs servirá este portal automáticamente, permitiendo que el usuario vea la "Evolución de la Tesis" o el "Progreso del Proyecto" en una interfaz limpia y profesional, autogenerada al final de cada sesión.

## 6. FrameTech: Desarrollo Multi-Framework
Para que Hive sea una verdadera factoría de software, la **Abeja Reina** debe dominar no solo el framework de agentes, sino los frameworks de aplicación estándar de la industria.

### A. Adaptadores de Framework (Django, FastAPI, Astro)
*   **Rol:** Un set de herramientas (`Skills`) que contienen el conocimiento estructural de los frameworks mencionados.
*   **Integración:** En lugar de escribir archivos planos, la Reina utiliza herramientas de **Scaffolding Inteligente** para:
    *   Generar proyectos Django con configuración de Base de Datos y Auth incluida.
    *   Desplegar APIs en FastAPI integradas con el `AgentRuntime` de Hive como middleware.
    *   Construir frontends en Astro que consuman los resultados de los Workers en tiempo real.

### B. Inyección de Plantillas de Grado Profesional
*   **Knowledge Seed:** Una base de datos de "Best Practices" y "File Templates" oficiales para cada framework, evitando las alucinaciones de estructura típicas de los LLMs.
*   **Validación de Construcción:** El **Desplegador** (`hive-boot`) verifica automáticamente que el código generado pase linters de Django o Astro antes de presentarlo al usuario.

### C. Hive-as-a-Service (HaaS)
*   Integración nativa donde los agentes de Hive se exponen automáticamente como endpoints de FastAPI o Django, permitiendo que aplicaciones externas consuman la inteligencia del enjambre vía REST/GraphQL de forma nativa.
## 7. Estrategia de Integración por Fases (One-by-One)
Para asegurar que cada framework se integre con "Alta Fidelidad", seguiremos un despliegue secuencial:

### Fase 1: FastAPI (El "Nativo")
*   **Por qué:** Es el más cercano al stack actual de Hive (Async Python + Pydantic).
*   **Hito:** Desarrollar el primer `FastAPI-Adapter` que permita a un agente exponer sus herramientas como un servidor API REST auto-documentado.

### Fase 2: Astro (El "Escaparate")
*   **Por qué:** Astro es ideal para documentación estática y dashboards de alta velocidad.
*   **Hito:** Integración con el módulo de MkDocs para crear sitios de reporte ultra-rápidos y visualmente superiores para el usuario.

### Fase 3: Django (El "Monolito")
*   **Por qué:** Para casos de uso que requieran ORM pesado y gestión administrativa compleja.
*   **Hito:** Inyección de semillas de conocimiento para el manejo de "Django-Admin" y "Django-Rest-Framework" de forma nativa por la Reina.

### Ciclo de Trabajo para cada Framework:
1.  **Ingesta de Semilla:** Cargar las "Best Practices" en la capa de referencia de la Queen.
2.  **Desarrollo de Adaptador:** Crear herramientas MCP de scaffolding (`init-project`, `add-feature`, `test-env`).
3.  **Habilitación en Desplegador:** Actualizar `hive-boot` para validar requerimientos específicos (ej: Node.js para Astro, PostgreSQL para Django).

## 8. Motor de Frameworks Universal (Plug & Play)
Para evitar que Hive se vuelva un monolito de adaptadores, implementaremos un sistema de **Plug-ins de Frameworks**.

### A. El Manifiesto del Framework (`framework-manifest.json`)
Cualquier usuario podrá añadir un nuevo framework (ej: Next.js, Flask, Svelte) simplemente definiendo un manifiesto que incluya:
*   **Estructura Base:** El mapa de carpetas y archivos críticos.
*   **Comandos de Ciclo de Vida:** Cómo ejecutar `dev`, `build` y `test` en ese entorno.
*   **Contrato de Inyección:** Qué archivos son editables por los Workers y cuáles son de configuración protegida.

### B. Agente de Scaffolding Dinámico
*   En lugar de tener una lógica única por framework, la **Queen Bee** leerá el manifiesto y ajustará su comportamiento de construcción en tiempo real. 
*   **Hito:** Una herramienta `register_framework(manifest_url)` que descargue las semillas de conocimiento y los templates de forma automática, permitiendo que la colmena aprenda nuevas tecnologías en segundos.

### C. Almacén de Semillas Comunitario
*   Un repositorio central de "Seeds" (Semillas) donde la comunidad pueda compartir configuraciones óptimas para Hive, permitiendo una expansión infinita del catálogo FrameTech.

## 9. Agente Arquitecto FrameTech (Specialized Scout)
Para escalar la biblioteca de frameworks de forma autónoma, se añadirá un agente especialista subordinado a la **Queen Bee**.

### A. Rol: El "Scout" de Frameworks
Este agente vive en la carpeta `core/framework/agents/frametech_architect` y su única misión es el onboarding de tecnología:
*   **Entrada:** Un enlace a un repositorio o documentación (ej: "https://astro.build").
*   **Análisis:** Utiliza herramientas de scraping profundo para mapear el sistema de archivos, las dependencias (`package.json`, `pyproject.toml`) y los comandos de inicio.
*   **Producción:** Genera automáticamente el **Manifiesto Zeta** y la **Semilla de Conocimiento** en la carpeta `docs/frametech/[nombre_framework]`.

### B. Carpeta `docs/frametech/` (La Biblioteca)
Un espacio dedicado en el sistema de archivos donde el Arquitecto depositará:
*   `00_manifest.json`: Reglas de construcción.
*   `01_expert_seed.md`: Prompts de especialización para ese framework.
*   `02_patterns.md`: Ejemplos de código y anti-patrones detectados.




## 10. Capa de Adaptación Dinámica (Hot-Patching Zeta - HITL)
Para asegurar el control total del usuario, la evolución de Hive seguirá un protocolo donde el **Humano es el Tester y el Apoyo para el Ajuste**.

### A. El Lazo de Validación (Human-as-Tester)
*   **Sandbox de Prueba:** Antes de aplicar cualquier cambio, Hive creará un entorno aislado donde el usuario podrá ejecutar el nodo modificado con datos de prueba.
*   **Rol del Usuario:** El usuario actúa como el **QA final**, validando que el comportamiento sea el esperado y detectando efectos secundarios que la IA pueda pasar por alto.

### B. Co-Ajuste Iterativo (Collaborative Refinement)
*   **Feedback en Caliente:** Si el parche propuesto no es perfecto, el usuario puede dar instrucciones directas: `"Ajusta la validación de X"` o `"Optimiza este bucle"`.
*   **Iteración Hive:** El sistema generará una nueva versión del parche basada en el feedback del humano-tester, repitiendo el ciclo hasta que el ajuste sea impecable.

### C. Soporte Humano en Fallas Críticas
*   En casos donde el `Judge` no pueda proponer una solución (puntos ciegos de la arquitectura), Hive solicitará **Apoyo para el Ajuste**, proporcionando al usuario todos los logs y estados necesarios para que el humano guíe la reparación.

**"La IA propone el plano, el humano valida el cimiento y juntos ajustan la estructura. La simbiosis es total."**

