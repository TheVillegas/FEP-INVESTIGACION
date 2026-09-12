# Inicio rápido: ENGRAM Cloud y acceso interno (Windows CMD, Linux y macOS Bash)

Configurá tu token individual y el acceso por Tailscale antes de usar los recursos internos del equipo. No compartas credenciales ni contenido sensible.

## Camino feliz: Windows CMD

1. Pedile al administrador tu token individual de ENGRAM Cloud y la invitación al tailnet.
2. En una ventana de **CMD**, guardá el token:

   ```cmd
   setx ENGRAM_CLOUD_TOKEN "<TOKEN_PRIVATE>"
   ```

   El cambio se aplica solo a ventanas de CMD nuevas. Cerrá esta ventana, abrí otra y verificá su presencia sin mostrar el valor:

   ```cmd
   if defined ENGRAM_CLOUD_TOKEN (echo ENGRAM_CLOUD_TOKEN configurado) else (echo ENGRAM_CLOUD_TOKEN no configurado)
   ```

   **Resultado esperado:** `ENGRAM_CLOUD_TOKEN configurado`.
3. Iniciá sesión en Tailscale con tu propia cuenta aprobada mediante la invitación del administrador al tailnet.
4. Confirmá la conexión:

   ```cmd
   tailscale status
   ```

   **Resultado esperado:** el comando muestra el estado de la red. Confirmá con el administrador que tenés acceso a los recursos internos autorizados.

## Camino feliz: Linux y macOS Bash

1. Pedile al administrador tu token individual de ENGRAM Cloud y la invitación al tailnet.
2. Para la terminal actual, configurá el token:

   ```bash
   export ENGRAM_CLOUD_TOKEN="<TOKEN_PRIVATE>"
   ```

   No ejecutes comandos que muestren, registren o hagan eco del valor.
3. Para conservarlo solo en tu cuenta de usuario, creá el directorio privado:

   ```bash
   mkdir -p ~/.config/engram-cloud
   chmod 700 ~/.config/engram-cloud
   ```

   Con un editor local, guardá la única línea `export ENGRAM_CLOUD_TOKEN="<TOKEN_PRIVATE>"` en `~/.config/engram-cloud/env`, usando el token recibido por un canal privado y sin copiarlo al repositorio. Luego restringí sus permisos:

   ```bash
   chmod 600 ~/.config/engram-cloud/env
   ```

   Agregá esta única línea a tu archivo de inicio de shell (por ejemplo, `~/.bashrc` o `~/.zshrc`):

   ```bash
   source ~/.config/engram-cloud/env
   ```

   Cerrá y abrí una terminal nueva para que se cargue el archivo de inicio. Luego verificá únicamente que esté presente, sin imprimir su valor:

   ```bash
   if [ -n "${ENGRAM_CLOUD_TOKEN:-}" ]; then echo "ENGRAM_CLOUD_TOKEN configured"; else echo "ENGRAM_CLOUD_TOKEN not configured"; fi
   ```

   **Resultado esperado:** `ENGRAM_CLOUD_TOKEN configured`.
4. Iniciá sesión en Tailscale con tu propia cuenta aprobada mediante la invitación del administrador al tailnet y confirmá la conexión:

   ```bash
   tailscale status
   ```

   **Resultado esperado:** el comando muestra el estado de la red. Confirmá con el administrador que tenés acceso a los recursos internos autorizados.

## Excepción por límite de asientos

Todas las personas usuarias normales se autentican con su propia cuenta aprobada. Como excepción temporal, puede haber **como máximo una** persona y estación de trabajo específicamente designadas por administración que usen la identidad de administrador OneByte por una restricción de asientos.

- El administrador aprovisiona ese inicio de sesión fuera de este repositorio.
- El administrador registra la persona y el dispositivo asignados, y rota el acceso cuando cambia cualquiera de los dos.
- Esa cuenta se restringe únicamente a Tailscale.
- No documentes ni solicites en el repositorio la dirección de identidad, contraseña, códigos MFA o de recuperación de esa cuenta.

## Después del bootstrap aprobado por administración

Ejecutá estos pasos **solo después de que el administrador confirme que el bootstrap terminó correctamente**. El bootstrap no activa la sincronización automática de tu equipo.

1. Configurá tu cliente local con la URL privada que te indique el administrador:

   ```bash
   engram cloud config --server <CLOUD_SERVER_URL>
   ```

2. Conservá tu token individual fuera de Git, como se indica arriba, y enrolá el ID canónico del proyecto. Luego sincronizá y verificá el estado:

   ```bash
   engram cloud enroll fep-investigacion
   engram sync --cloud --project fep-investigacion
   engram sync --status --cloud --project fep-investigacion
   ```

3. La sincronización automática es opcional. Para habilitarla, antes de iniciar tu proceso habitual `engram serve` o `engram mcp`, definí **las tres** variables en tu entorno local:

   ```bash
   export ENGRAM_CLOUD_AUTOSYNC=1
   export ENGRAM_CLOUD_TOKEN="<TOKEN_PRIVATE>"
   export ENGRAM_CLOUD_SERVER="<CLOUD_SERVER_URL>"
   ```

   En Windows CMD, definilas con `setx` y abrí una ventana nueva antes de iniciar ese proceso. Nunca agregues estas variables, tokens ni URL al repositorio.

## Protección de credenciales y datos internos

- Nunca hagas commit de un token, contraseña, código MFA o código de recuperación.
- Nunca pegues un token, contraseña o código en chat ni lo imprimas o registres en la terminal.
- Cada token es individual, por persona, y el administrador lo distribuye de forma privada.
- Recibí los nombres de equipos y direcciones de servicios internos únicamente del administrador y no los agregues al repositorio.
- Si sospechás exposición, avisá al administrador para que reemplace o rote el acceso.

## Trazabilidad del uso de IA

Registrá cada uso real de IA en la [bitácora de investigación](templates/research-log.md) y completá el [anexo de declaración de uso de IA](../Anexo%20Declaraci%C3%B3n%20de%20Uso%20de%20IA%20-%20ONEBYTE%20-%20TI-06.md). Para cada interacción, conservá:

- prompt exacto;
- herramienta y versión, e identificador del modelo;
- fecha;
- decisión relevante tomada a partir de la interacción (o "sin decisión");
- fundamento o evidencia de la decisión;
- enlace a la salida o evidencia verificable;
- revisión humana (responsable, fecha y resultado).

No incorporés contenido generado por IA en las secciones del curso que lo prohíben: análisis comparativo y criterios, conclusiones y recomendaciones, aporte propio o discusión crítica, ni redacción o justificaciones del cuestionario. Esas partes son de autoría humana exclusiva.

## Si algo falla

| Situación | Acción segura |
| --- | --- |
| Token no configurado | En CMD, abrí una ventana nueva. En Bash, iniciá una terminal nueva o cargá el archivo de inicio. Si continúa, configurá el token privado recibido; no lo envíes como evidencia. |
| Tailscale no muestra acceso a recursos internos | Confirmá que iniciaste sesión con tu cuenta aprobada y que aceptaste la invitación al tailnet. Pedile al administrador que confirme tu acceso y los datos internos. |

## Checklist

- [ ] Token individual guardado y verificado sin revelarlo.
- [ ] Sesión de Tailscale iniciada con cuenta propia aprobada, salvo la única excepción temporal asignada por administración.
- [ ] Datos internos recibidos del administrador y no incorporados al repositorio.
- [ ] Uso de IA y revisión humana registrados antes de integrar trabajo.
