# Acceso al proyecto Cloud `fep`

Esta guía permite acceder al proyecto Cloud ya autorizado `fep`. **No es el proyecto de este repositorio:** su ID canónico es `fep-investigacion`, sigue bloqueado por la allowlist y no debe usarse en estos comandos.

## Requisitos

- Ser integrante autorizado por la administración para acceder al proyecto `fep`.
- Estar conectado a Tailscale.
- Tener un token personal válido para el servidor Cloud.
- Ejecutar los comandos desde el repositorio o flujo de trabajo de FEP, nunca como sustituto del enrollment de este repositorio de investigación.

## Configurar el cliente

### Windows CMD

```cmd
engram cloud config --server <CLOUD_SERVER_URL>
set ENGRAM_CLOUD_TOKEN=<PERSONAL_VALID_TOKEN>
engram cloud enroll fep
```

### Linux/macOS Bash

```bash
engram cloud config --server <CLOUD_SERVER_URL>
export ENGRAM_CLOUD_TOKEN="<PERSONAL_VALID_TOKEN>"
engram cloud enroll fep
```

El token es personal: no lo compartas ni lo agregues al repositorio.

## Sincronización inicial y consulta de estado

```bash
engram sync --cloud --project fep
engram sync --cloud --status --project fep
```

El segundo comando es de solo lectura y permite verificar el estado de sincronización.

## Autosync opcional

Solo para trabajo real que deba quedar registrado, activá autosync antes de iniciar tu proceso habitual de `engram serve` o `engram mcp`:

```bash
export ENGRAM_CLOUD_AUTOSYNC=1
engram serve
# o: engram mcp
```

En Windows CMD:

```cmd
set ENGRAM_CLOUD_AUTOSYNC=1
engram serve
REM o: engram mcp
```

> **Advertencia:** autosync no habilita acceso público, no reemplaza Tailscale ni el token personal, y no anula las restricciones académicas de este repositorio. No uses `fep` ni estos comandos para enrollar o registrar `fep-investigacion`.
