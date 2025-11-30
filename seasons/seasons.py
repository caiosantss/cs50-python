import datetime

date_iso_format = "2025-12-25"

#Converte para date object -- Somente a data
print(datetime.date.fromisoformat(date_iso_format))

#converte para datetime object - Data + Hora(00:00:00)
data_convertida = datetime.datetime.strptime(date_iso_format, "%Y-%m-%d")
print(data_convertida)

agora = datetime.datetime.now()
agora_hora_zerada = agora.replace(hour=0, minute=0, second=0, microsecond=0)
# print(agora)
print(agora_hora_zerada)

#Diferença entre datas
diferenca = data_convertida - agora_hora_zerada
print(diferenca)

minutos = diferenca.total_seconds() / 60
print(f"{minutos:.2f}")
