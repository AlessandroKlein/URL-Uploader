class Translation(object):
    START_TEXT = """Hola,
¡Este es un bot de subida de URL de Telegram!

<b> Por favor, envíeme cualquier enlace de URL de descarga directa, puedo subirlo a Telegram como Archivo / Video </b>
Escribe /help para más detalles.

➟ <b>Hecho por @</b>"""
    RENAME_403_ERR = "Lo siento. No se le permite cambiar el nombre de este archivo."
    ABS_TEXT = " Por favor no seas egoísta."
    UPGRADE_TEXT = "<b>👉 Crear su propio bot de clonación.. </b>  \n\n<a href='https://youtu.be/'>Haga clic aquí, Fork and Deploy!!</a>"
    FORMAT_SELECTION = "<b>Seleccione el formato deseado:</b> <a href='{}'>el tamaño del archivo puede ser aproximado</a> \n<b>Si desea configurar una miniatura personalizada, </b> envíe la foto antes o rápidamente después de tocar cualquiera de los botones a continuación.\nPuedes usar /deletethumbnail para eliminar la miniatura generada automáticamente."
    SET_CUSTOM_USERNAME_PASSWORD = """<b>Si desea descargar videos premium, </b> proporcione en el siguiente formato:
<b>URL | filename | username | password</b>"""
    NOYES_URL = "@robot URL detectada. Utilice https://shrtz.me/PtsVnf6 y consígame una URL rápida para que pueda subir a Telegram, sin que me ralentice para otros usuarios.."
    DOWNLOAD_START = "<b>📥 Descargando...</b>"
    UPLOAD_START = "<b>Subiendo ahora... 📤</b>"
    RCHD_BOT_API_LIMIT = "tamaño mayor que el tamaño máximo permitido (50 MB). Sin embargo, intentando subir."
    RCHD_TG_API_LIMIT = "Descargado en {} segundos.\nTamaño de archivo detectado: {}\nLo siento. Pero no puedo subir archivos de más de 1,5 GB debido a las limitaciones de la API de Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Por favor califíqueme si me encuentra útil. Únete: @"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dautocargado en {} segundos. \n<b>Comparte y apóyame :</b> [👉 Share]() \nSubido en {} segundos."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Tamaño de archivo detectado: {}. Los usuarios gratuitos solo pueden cargar: {}\nPor favor /upgrade su suscripción.\nSi cree que se trata de un error, comuníquese con <a href='https://telegram.dog/'>@</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Cguardar miniatura de archivo / video personalizado. Esta imagen se utilizará en el video / archivo.."
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ Miniatura personalizada borrada correctamente.</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "<b>✅ Los medios se borraron correctamente.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Documento descargado correctamente.</b>"
    CUSTOM_CAPTION_UL_FILE = "<b>Comparte y apóyame:</b> [Share]()"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No se encontraron miniaturas guardadas!!\n\nEnvía una imagen para guardarla como tu miniatura de forma permanente.</b>"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> dicho: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> Añadido a {} hasta {}."
    CURENT_PLAN_DETAILS = """<b>Detalles del plan actual</b>
--------
Telegram ID: <code>{}</code>
"""
    HELP_USER = """<b> Hola, soy el robot de subida de URL. </b>
    
1. Enviar URL (Enlace | Nuevo nombre con extensión).
2. Enviar miniatura personalizada (opcional).
3. Seleccione el botón.
    SVideo - Dar archivo como video con capturas de pantalla
    DFile - Dar archivo con capturas de pantalla
    Video: entregar archivo como video sin capturas de pantalla
    DFile: entregar archivo sin capturas de pantalla
   
--------
Envíeme a conocer los detalles del plan actual

➟ <b> Hecho por @ </b>
"""
    REPLY_TO_DOC_GET_LINK = "Responda a un medio de Telegram para obtener un enlace de descarga directa de alta velocidad"
    REPLY_TO_DOC_FOR_C2V = "Responder a un medio de Telegram para convertir"
    REPLY_TO_DOC_FOR_SCSS = "Responde a un medio de Telegram para obtener capturas de pantalla"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Responder a un medio de Telegram / cambiar el nombre con soporte de miniaturas personalizadas"
    AFTER_GET_DL_LINK = "Enlace directo <a href='{}'> generado </a> válido por {} días.\n© @"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Sintaxis: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "Primero envía /downloadmedia a cualquier medio para que pueda descargarse a mi local. \nEnvía /storageinfo para conocer los medios que se descargan actualmente."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Duración del video: {}\nEnvía /clearffmpegmedia para eliminar este medio, de mi almacenamiento.\nEnvía /trim HH:MM:SS [HH:MM:SS] para cortar una pequeña foto / video, de los medios anteriores."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Ya existe un medio guardado. Por favor envíe /storageinfo para conocer los detalles actuales de los medios."
    USER_DELETED_FROM_DB = "Usuario <a href='tg://user?id={}'>{}</a> eliminado de la base de datos."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Responder a un medio de Telegram (MKV), para extraer transmisiones incrustadas"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Respuesta /generatecustomthumbnail a un álbum multimedia, para generar una miniatura personalizada"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "El álbum multimedia debe contener solo dos fotos. Vuelva a enviar el álbum multimedia y vuelva a intentarlo o envíe solo dos fotos en un álbum.."
    INVALID_UPLOAD_BOT_URL_FORMAT = "El formato de URL es incorrecto. asegúrese de que su URL comience con http: // o https: //. Puede establecer un nombre de archivo personalizado utilizando el enlace de formato | file_name.extension"
    ABUSIVE_USERS = "No se le permite utilizar este bot. Si cree que se trata de un error, marque /me para eliminar esta restricción."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/"
    EXTRACT_ZIP_INTRO_ONE = "Primero envíe un archivo comprimido, luego responda /unzip comando al archivo."
    EXTRACT_ZIP_INTRO_THREE = "Analizando archivo recibido. ⚠️ Esto puede llevar algún tiempo. Por favor sea paciente. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Lo siento. Se produjeron errores al procesar el archivo comprimido. Vuelve a comprobarlo todo dos veces y, si el problema persiste, infórmalo a <a href='https://t.me/'>Support Group</a>"
    EXTRACT_ZIP_STEP_TWO = """Seleccione file_name para cargar de las siguientes opciones.
Puedes usar /rename comando después de recibir el archivo para cambiarle el nombre con soporte de miniaturas personalizadas."""
    CANCEL_STR = "Proceso cancelado"
    ZIP_UPLOADED_STR = "Subió {} archivos en {} segundos"
    FREE_USER_LIMIT_Q_SZE = """No se puede procesar.
Usuarios gratuitos solo 1 solicitud cada 30 minutos.
/upgrade o intente 1800 segundos más tarde."""
    SLOW_URL_DECED = "Dios, eso parece ser una URL muy lenta. Como estabas jodiendo mi casa, no estoy de humor para descargar este archivo. Mientras tanto, ¿por qué no intentas esto: ==> https://shrtz.me/PtsVnf6 y me consigues una URL rápida para que pueda subir a Telegram, sin que me desacelere para otros usuarios?."
