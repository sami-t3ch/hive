# Flujo de Trabajo Multi-Repositorio (Git Workflow)

Esta guía explica cómo mantener sincronizados de manera segura tus repositorios locales con el framework original de AdenHQ (`upstream`), tu fork (`origin`) y el de colaboraciones (`sami`).

## Los Remotos (Orígenes) Configurados

- **`upstream`**: `https://github.com/aden-hive/hive` (El repositorio oficial original. De aquí provienen las actualizaciones de los creadores).
- **`origin`**: `https://github.com/ssolis-ti/hive` (Tu bifurcación/fork principal actual).
- **`sami`**: `https://github.com/sami-t3ch/hive` (Tu bifurcación de integraciones).

---

## 🛑 Regla de Oro
**NUNCA** hagas cambios directamente ni corras `git commit` en la rama `main`.
La rama `main` de tu computadora solo sirve para reflejar exactamente lo que existe en `upstream/main`.

---

## Operaciones Diarias

### 1. Actualizar tu entorno con la última versión oficial (adenhq)
Haz esto antes de empezar a trabajar para tener las últimas novedades del framework sin conflictos:

```bash
git checkout main
git pull upstream main
```
*Si quieres, puedes mantener tu propio `main` de GitHub actualizado con un `git push origin main` y/o `git push sami main`.*

### 2. Crear un nuevo ajuste o característica (Feature Branch)
Cuando vayas a crear mejoras visuales, scripts de Zeta, configurar Docker, etc:

```bash
# 1. Asegúrate de estar en main y actualizado
git checkout main

# 2. Crea tu rama y salta hacia ella
git checkout -b feature/nombre-del-ajuste
```

### 3. Trabajar en tu rama (Guardar Cambios)
Mientras trabajas en tu característica:

```bash
git add .
git commit -m "feat: agregando mejoras visuales y dockers"
```

### 4. Mantener tu característica actualizada con AdenHQ
Si has estado trabajando semanas en un ajuste y el framework oficial se actualizó, trae esos cambios a tu rama para que no se rompa nada:

```bash
# Actualizas main
git checkout main
git pull upstream main

# Vuelves a tu característica y la actualizas
git checkout feature/tu-rama
git merge main
```

### 5. Subir tus ramas a GitHub
Una vez que hayas verificado localmente que todo funciona (con `uv run python -m ... test` o ejecutando los contenedores), guárdalos en la nube:

```bash
# Para guardarlo en el fork 'sami'
git push -u sami feature/tu-rama

# Opcionalmente, para guardarlo en el fork 'origin'
git push -u origin feature/tu-rama
```

### 6. Contribuir Oficialmente (Pull Request)
Cuando estés listo, entras a GitHub usando el navegador web (a tu repositorio `sami-t3ch/hive` o `ssolis-ti/hive`), cambias a tu rama `feature/tu-rama`, y haces clic en el botón de "Compare & Pull Request". Esto propondrá tus cambios al equipo oficial de `adenhq`.
