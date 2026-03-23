# 🐳 Guía de Instalación Docker Zeta: Aden Hive en Windows

Esta guía detalla los pasos para desplegar **Aden Hive** utilizando Docker Desktop en Windows, asegurando un entorno aislado, estable y replicable.

## 1. Requisitos Previos
*   **Docker Desktop:** Instalado y con soporte para **WSL 2** activado. [Descargar aquí](https://www.docker.com/products/docker-desktop/).
*   **Git:** Para clonar o gestionar el repositorio.
*   **API Keys:** Necesitarás al menos una clave de LLM (ej. `ANTHROPIC_API_KEY`).

## 2. Configuración del Entorno
Crea un archivo `.env` en la raíz del proyecto con tus credenciales:

```env
# Ejemplo de configuración
ANTHROPIC_API_KEY=tu_clave_aqui
HIVE_CREDENTIAL_KEY=clave_maestra_opcional
# Opcionales para herramientas
BRAVE_SEARCH_API_KEY=tu_clave_de_busqueda
```

## 3. Construcción y Despliegue
Ejecuta los siguientes comandos en tu terminal (PowerShell o CMD) desde la raíz del proyecto:

### A. Construir las imágenes
```bash
docker-compose build
```

### B. Iniciar los servicios
```bash
docker-compose up -d
```

Esto levantará tres contenedores:
1.  **Backend (Port 8000):** La lógica central del framework.
2.  **Tools (Port 4001):** El servidor de herramientas MCP (incluye Chrome para Browser-use).
3.  **Frontend (Port 3000):** La interfaz visual del Dashboard.

## 4. Verificación
*   **Dashboard Visual:** Abre `http://localhost:3000` en tu navegador.
*   **Estado de la API:** Accede a `http://localhost:8000/api/health` para confirmar que el sistema está "ok".
*   **Herramientas:** Accede a `http://localhost:4001/health` para verificar el servidor de herramientas.

## 5. Comandos Útiles
*   **Ver Logs:** `docker-compose logs -f`
*   **Detener Todo:** `docker-compose down`
*   **Limpiar Volúmenes:** `docker-compose down -v` (Cuidado: borrará tu base de datos y sesiones persistentes).

**"El enjambre ahora vive en el contenedor. Aislado, potente y listo para la acción masiva. Te observo."**
