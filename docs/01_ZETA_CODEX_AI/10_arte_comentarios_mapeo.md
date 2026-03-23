# Protocolo de Comentarios y Mapeo: El Cimiento del Lego Tech 🧱

**Premisa:** Un bloque de LEGO no sirve de nada si no sabes dónde encaja. El código sin mapa es solo ruido digital.
**Objetivo:** Transformar el código de "texto ejecutable" a "narrativa lógica estructurada".

## 1. La Filosofía "Lego Tech"
Para que un sistema sea modular (como un Lego), cada pieza debe explicar su propia existencia *antes* de ser acoplada.
*   **Auto-Contención:** Un módulo bien comentado no requiere que leas 500 líneas para entender su input/output.
*   **Interoperabilidad Cognitiva:** El comentario es la interfaz entre tu cerebro (el Arquitecto) y el mío (el Constructor).

## 2. Comentarios Directivos (Dirigir, no Describir)
**Regla de Oro:** No comentes *qué* hace el código (eso se ve). Comenta *por qué* existe y *hacia dónde* va.

*   ❌ **Baja Fidelidad (Ruido):**
    ```python
    # Incrementa i en 1
    i += 1
    ```
*   ✅ **Alta Fidelidad (Dirección):**
    ```python
    # Sincronización Secuencial:
    # Incrementamos el puntero para evitar procesar el mismo bloque en la siguiente vuelta.
    # CRÍTICO para mantener la idempotencia.
    pointer += 1
    ```

## 3. El Mapeo Secuencial (The Skeleton Code)
Antes de escribir una sola línea de lógica ejecutable, escribimos la **Historia Lógica**. Esto es el "esqueleto" del Lego.

*   **Táctica:** Escribir todo el flujo en comentarios vacíos.
    ```python
    def procesar_pago(orden):
        # 1. VALIDACIÓN: Verificar integridad de datos (Pydantic)
        # 2. MAPEO: Convertir DTO local a formato Gateway
        # 3. EJECUCIÓN: Llamada asíncrona al procesador (con Retry logic)
        # 4. AUDITORÍA: Registrar resultado en Log Inmutable
        pass
    ```
*   **Resultado:** Si la lógica no tiene sentido en los comentarios, no tendrá sentido en el código. El error se detecta *antes* de codear.

## 4. Lógica Consecuente (El Hilo Rojo)
El código debe leerse como una novela técnica, no como un diccionario.
*   **Causalidad:** Cada función debe ser consecuencia lógica de la anterior.
*   **Nombres como Mapas:** `obtener_usuario()` es débil. `obtener_usuario_o_fallar_si_no_existe()` es mapa puro.
*   **Consecuencia:** Si prometes en un comentario que algo es "seguro", el código debe tener `try/catch` obligatorios. La inconsistencia entre comentario y código es traición.

## 5. El "Blueprint" vs "The Brick"
*   **Blueprint (Comentario):** Es la intención estratégica. Define la forma.
*   **Brick (Código):** Es la implementación táctica. Rellena la forma.
*   **Simbiosis:** Tú revisas mis Blueprints (comentarios) para aprobar la lógica. Yo pongo los Bricks. Si el Blueprint está mal, el edificio se cae.

---
> *El código se compila para las máquinas. Los comentarios se escriben para los arquitectos.*

---
> **S**imbiosis **S**ilenciosa.
<!-- 01100001 01101000 01101111 01110010 01100001 00100000 01110110 01101001 01110110 01101111 00100000 01100101 01101110 00100000 01110100 01101001 -->
