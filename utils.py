from pyspark.sql.functions import struct, collect_list, to_json
import json

def spark_df_to_json_serializable(df, limit=100):
    
    # Converte um DataFrame Spark em uma string JSON que pode ser enviada via API.
    # Retorna uma lista de dicionários Python.
    
    # Limita o DataFrame para não enviar dados excessivos
    limited_df = df.limit(limit)
    
    # Usa o método nativo do Spark para converter para uma string JSON de um array de objetos
    json_string = limited_df.agg(
        to_json(collect_list(struct(*limited_df.columns)))
    ).first()[0]
    
    # Se o resultado for nulo ou vazio, retorna uma lista vazia
    if not json_string:
        return []
        
    # Converte a string JSON de volta para um objeto Python (lista de dicionários)
    return json.loads(json_string)