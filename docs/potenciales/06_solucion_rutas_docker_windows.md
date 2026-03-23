# 🐳 Solución de Rutas y Volúmenes: Docker vs Windows

Esta guía resuelve los problemas de sincronización de archivos y resolución de rutas que surgen al trabajar con **Aden Hive** en un entorno mixto (Host Windows / Contenedor Linux).

## 1. El Problema: "Archivo No Encontrado"

Cuando Aden Hive corre en Docker, vive en un sistema Linux aislado. Dos errores comunes ocurren:
1.  **Rutas Absolutas de Windows:** El contenedor no entiende qué es `C:\Users\Proyecto Z\...`. 
2.  **Aislamiento del Host:** Los archivos guardados en el contenedor (ej. un PDF generado) no aparecen en Windows, y los cambios en Windows (ej. editar una herramienta) no se ven en el contenedor.

## 2. La Solución: Mapeo de Volúmenes (Mounts)

La forma correcta de conectar ambos mundos es mediante el archivo `docker-compose.yaml`. Debemos definir **volúmenes** que actúen como "puentes".

### Configuración Recomendada
En los servicios `backend` y `tools`, asegúrate de tener estos mapeos:

```yaml
services:
  backend:
    volumes:
      - ./.hive:/root/.hive          # Persistencia de sesiones y DB
      - ./tools:/app/tools           # Sincroniza cambios en herramientas
      - ../MPBOTINFO:/app/mpbotinfo  # Acceso a datos externos (fuera del repo)
```

> [!IMPORTANT]
> Si tu carpeta de datos (`MPBOTINFO`) está al mismo nivel que la carpeta del proyecto (`hive-main`), usa `../MPBOTINFO`. Si está dentro, usa `./MPBOTINFO`.

## 3. Reglas de Oro para Rutas

Para que los agentes y herramientas funcionen sin errores:

1.  **Usa Rutas Relativas:** Siempre usa rutas relativas al directorio de trabajo del contenedor (`/app`).
2.  **Evita `docker cp` para Producción:** Usar `docker cp` es manual y se pierde si el contenedor se recrea. Los volúmenes son automáticos y persistentes.
3.  **Referencia en Prompts:** Indica al agente que busque datos en rutas locales del contenedor, como `/app/mpbotinfo`, no en rutas de Windows.

## 4. Cómo Aplicar Cambios

Si editas el `docker-compose.yaml` para añadir un volumen:
1.  **Detén los servicios:** `docker-compose down`
2.  **Inicia de nuevo:** `docker-compose up -d`

Esto recreará los contenedores con los nuevos "puentes" hacia tu sistema de archivos de Windows.

**"Un enjambre sin puentes está ciego. Los volúmenes son los ojos que conectan la mente de la colmena con la realidad de tus archivos. Te observo."**
