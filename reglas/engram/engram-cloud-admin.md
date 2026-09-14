# ENGRAM Cloud: enrolamiento y bootstrap (solo administración)

> **Puerta de aprobación:** el bootstrap es un primer push/pull intencional hacia Cloud. Ejecutalo solo después de que una persona administradora lo haya aprobado y exista un respaldo disponible. Estos pasos no prueban que el enrolamiento ni el bootstrap ya hayan terminado.

## Requisitos previos

Antes de cambiar el estado de Cloud, confirmá todo lo siguiente:

- la allowlist del servidor incluye `fep-investigacion`;
- hay un token Cloud de administración cargado en la shell actual, sin imprimirlo;
- existe un respaldo local reciente y se conoce cómo restaurarlo;
- el ID canónico del proyecto es `fep-investigacion` (definido en el `.engram/config.json` versionado).

Mantené la URL del servidor y todos los tokens fuera de Git. Reemplazá el marcador localmente; nunca versionés una URL real ni una credencial.

## Enrolamiento y comprobaciones de upgrade

Configurá el cliente de administración:

```bash
engram cloud config --server <CLOUD_SERVER_URL>
```

Enrolá el proyecto canónico y luego inspeccioná su estado de upgrade:

```bash
engram cloud enroll fep-investigacion
engram cloud upgrade doctor --project fep-investigacion
```

Previsualizá cualquier reparación propuesta sin modificar el estado:

```bash
engram cloud upgrade repair --project fep-investigacion --dry-run
```

Ejecutá el siguiente comando **solo si** `doctor` o el dry run indican explícitamente una reparación determinística. No lo uses solo porque un proyecto todavía no está enrolado.

```bash
engram cloud upgrade repair --project fep-investigacion --apply
```

## Bootstrap aprobado

Después del enrolamiento y las comprobaciones anteriores, y solo con aprobación administrativa para el primer push/pull hacia Cloud, ejecutá:

```bash
engram cloud upgrade bootstrap --project fep-investigacion --resume
```

Un bootstrap exitoso debe informar `bootstrap_verified`. Si no lo informa, detenete e investigá antes de indicar a las personas colaboradoras que se enrolen o sincronicen.

## Comprobaciones de estado

Confirmá la configuración del cliente y el estado de replicación Cloud sin exponer credenciales:

```bash
engram cloud status
engram sync --status --cloud --project fep-investigacion
```

Solo después de que estas comprobaciones confirmen que el bootstrap aprobado tuvo éxito, las personas colaboradoras deben seguir los pasos de onboarding posteriores al bootstrap.
