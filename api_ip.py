import requests
import json

def obtener_info_ip(ip):
    url = "http://ip-api.com/json/" + ip
    try:
        data = requests.get(url).json()
        if data['status'] == 'success':
            return {
                "IP": ip,
                "Pais": data.get('country'),
                "Region": data.get('regionName'),
                "ISP": data.get('isp'),
                "Coordenadas": {
                    "Latitud": data.get('lat'),
                    "Longitud": data.get('lon')
                }
            }
        else:
            return {"IP": ip, "Error": "IP no encontrada o invalida"}
    except Exception as e:
        return {"IP": ip, "Error": str(e)}

resultados = []
while True:
    ip = input("Ingresa una IP publica (o escribe 'exit' para salir): ")
    if ip.lower() == 'exit':
        break
    info = obtener_info_ip(ip)
    resultados.append(info)
    print(json.dumps(info, indent=4))

archivo = open("ip_api_publica.json", "w")
json.dump(resultados, archivo, indent=4)
archivo.close()

print("Resultados guardados en ip_api_publica.json")
