import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def copy_s3_file(source_bucket, source_key, destination_bucket, destination_key):
    # Inicializar el cliente S3
    s3_client = boto3.client('s3')
    
    try:
        # Descargar el archivo desde el bucket de origen
        print(f"Descargando {source_key} desde {source_bucket}...")
        s3_client.download_file(source_bucket, source_key, '/tmp/tempfile')
        
        # Subir el archivo al bucket de destino
        print(f"Subiendo {destination_key} a {destination_bucket}...")
        s3_client.upload_file('/tmp/tempfile', destination_bucket, destination_key)
        
        print("Archivo copiado exitosamente!")
    
    except NoCredentialsError:
        print("Error: No se encontraron las credenciales de AWS.")
    except ClientError as e:
        print(f"Error al copiar el archivo: {e}")

if __name__ == "__main__":
    # Variables de ejemplo (modifícalas según tus necesidades)
    source_bucket = 'mi-bucket-origen'
    source_key = 'ruta/al/archivo.txt'
    destination_bucket = 'mi-bucket-destino'
    destination_key = 'ruta/nueva/archivo_copiado.txt'
    
    # Llamar a la función para copiar el archivo
    copy_s3_file(source_bucket, source_key, destination_bucket, destination_key)
