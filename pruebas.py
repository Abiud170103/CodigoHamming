import time
import random
import psutil
import os
from memory_profiler import profile

def esPotenciaDeDos(numero):
    """Función auxiliar copiada de hamming.py"""
    if((numero & (numero-1)) == 0 ):
        return True
    else:
        return False

def simular_hamming(datosEntrada):
    """Simula el proceso principal del código de Hamming"""
    inicio_total = time.time()
    
    # Convertir entrada a lista de enteros
    datosEnLista = [int(bit) for bit in datosEntrada]
    m = len(datosEnLista)
    
    if m == 0:
        return None, 0
    
    # Crear estructura de ubicaciones
    ubicaciones = []
    bitsDePosicionInfo = []
    contador = 1
    
    while ubicaciones.count("I") != m:
        if(esPotenciaDeDos(contador)):
            ubicaciones.append("P")
        else:
            ubicaciones.append("I")
            bitsDePosicionInfo.append(bin(contador)[2:])
        contador = contador + 1
    
    # Calcular bits de paridad (simulado)
    bitsDeParidad = []
    idPosicion = -1 
    filasAContar = (len(ubicaciones)- len(bitsDePosicionInfo))
    
    for bucleUno in range(0, filasAContar): 
        contadorParidad = 0   
        for bucleDos in range(0, len(datosEnLista)):
            if(len(bitsDePosicionInfo[bucleDos]) >= ( -1*idPosicion)):
                try:
                    if( int(bitsDePosicionInfo[bucleDos][idPosicion]) == 1):
                        if(int(datosEnLista[bucleDos]) == 1):
                            contadorParidad = contadorParidad + 1
                except IndexError:
                    pass  # Evitar errores de índice
        
        if(contadorParidad % 2 == 0):
            bitsDeParidad.append(0)
        else:
            bitsDeParidad.append(1)
        idPosicion = idPosicion - 1
    
    fin_total = time.time()
    return ubicaciones, fin_total - inicio_total

def prueba_estres_basica():
    """Prueba con diferentes tamaños de entrada"""
    print("=== PRUEBA DE ESTRÉS BÁSICA ===")
    tamaños = [4, 8, 16, 32, 64, 100, 200, 300, 500]
    
    resultados = []
    
    for tamaño in tamaños:
        # Generar cadena binaria aleatoria
        cadena = ''.join(random.choice('01') for _ in range(tamaño))
        
        print(f"\n📊 Probando con {tamaño} bits")
        print(f"Muestra: {cadena[:20]}{'...' if len(cadena) > 20 else ''}")
        
        try:
            resultado, tiempo = simular_hamming(cadena)
            
            if resultado:
                bits_paridad = resultado.count('P') if isinstance(resultado[0], str) else len([x for x in resultado if x == 'P'])
                bits_totales = len(resultado) if resultado else 0
                
                print(f"✅ Tiempo: {tiempo:.4f}s")
                print(f"   Bits de información: {tamaño}")
                print(f"   Bits de paridad: {bits_paridad}")
                print(f"   Bits totales: {bits_totales}")
                
                resultados.append({
                    'tamaño': tamaño,
                    'tiempo': tiempo,
                    'bits_paridad': bits_paridad,
                    'bits_totales': bits_totales
                })
                
                if tiempo > 5:  # Si tarda más de 5 segundos
                    print("⚠️  ADVERTENCIA: Tiempo excesivo, deteniendo pruebas")
                    break
            else:
                print("❌ Error en el procesamiento")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            break
    
    return resultados

def prueba_memoria():
    """Monitorea el uso de memoria"""
    print("\n=== PRUEBA DE MEMORIA ===")
    proceso = psutil.Process(os.getpid())
    
    tamaños = [10, 50, 100, 200, 500, 1000]
    
    for tamaño in tamaños:
        memoria_inicial = proceso.memory_info().rss / 1024 / 1024  # MB
        
        # Generar datos de prueba
        cadena = '1' * tamaño
        
        try:
            # Simular las estructuras de datos del código
            datosEnLista = [int(bit) for bit in cadena]
            ubicaciones = []
            bitsDePosicionInfo = []
            
            contador = 1
            while ubicaciones.count("I") != len(datosEnLista):
                if esPotenciaDeDos(contador):
                    ubicaciones.append("P")
                else:
                    ubicaciones.append("I")
                    bitsDePosicionInfo.append(bin(contador)[2:])
                contador += 1
            
            memoria_final = proceso.memory_info().rss / 1024 / 1024  # MB
            memoria_usada = memoria_final - memoria_inicial
            
            print(f"📊 Tamaño: {tamaño:4d} bits - Memoria: {memoria_usada:6.2f} MB - Total: {len(ubicaciones)} bits")
            
            if memoria_usada > 50:  # Si usa más de 50MB
                print("⚠️  ADVERTENCIA: Uso excesivo de memoria")
                break
                
        except MemoryError:
            print(f"❌ Error de memoria en tamaño {tamaño}")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def prueba_casos_extremos():
    """Prueba casos que pueden romper el código"""
    print("\n=== PRUEBA DE CASOS EXTREMOS ===")
    
    casos_extremos = [
        ("1", "Un solo bit (1)"),
        ("0", "Un solo bit (0)"),
        ("10", "Dos bits"),
        ("0" * 100, "100 zeros"),
        ("1" * 100, "100 unos"),
        ("01" * 50, "Patrón alternado 100 bits"),
        ("001100" * 17, "Patrón repetitivo ~100 bits"),
        ("1010101010", "Patrón alternado corto"),
        ("1111000011110000", "Patrón en bloques")
    ]
    
    for cadena, descripcion in casos_extremos:
        print(f"\n🧪 {descripcion}")
        print(f"   Longitud: {len(cadena)} bits")
        print(f"   Muestra: {cadena[:30]}{'...' if len(cadena) > 30 else ''}")
        
        try:
            resultado, tiempo = simular_hamming(cadena)
            
            if resultado:
                bits_paridad = len([x for x in resultado if x == 'P']) if isinstance(resultado[0], str) else 0
                print(f"   ✅ Tiempo: {tiempo:.4f}s - Bits paridad: {bits_paridad}")
            else:
                print(f"   ❌ Error en procesamiento")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")

def prueba_rendimiento_detallada():
    """Análisis detallado de rendimiento"""
    print("\n=== ANÁLISIS DE RENDIMIENTO DETALLADO ===")
    
    tamaños = list(range(4, 101, 8))  # 4, 12, 20, ..., 100
    tiempos = []
    complejidades = []
    
    print("Tamaño | Tiempo (s) | Bits Paridad | Complejidad")
    print("-" * 50)
    
    for tamaño in tamaños:
        cadena = ''.join(random.choice('01') for _ in range(tamaño))
        
        try:
            resultado, tiempo = simular_hamming(cadena)
            
            if resultado:
                # Calcular bits de paridad necesarios
                r = 0
                m = tamaño
                while (2**r) < (m + r + 1):
                    r += 1
                
                complejidad_teorica = m * r  # O(m*r) aproximadamente
                
                tiempos.append(tiempo)
                complejidades.append(complejidad_teorica)
                
                print(f"{tamaño:6d} | {tiempo:9.4f} | {r:11d} | {complejidad_teorica:10d}")
            
        except Exception as e:
            print(f"{tamaño:6d} | ERROR: {e}")
    
    if tiempos:
        print(f"\n📈 Estadísticas:")
        print(f"   Tiempo promedio: {sum(tiempos)/len(tiempos):.4f}s")
        print(f"   Tiempo máximo: {max(tiempos):.4f}s")
        print(f"   Tiempo mínimo: {min(tiempos):.4f}s")

def encontrar_limite_practico():
    """Encuentra el límite práctico del código"""
    print("\n=== BÚSQUEDA DE LÍMITE PRÁCTICO ===")
    
    tamaño = 100
    limite_tiempo = 10  # segundos
    
    while True:
        cadena = '1' * tamaño
        print(f"🔍 Probando con {tamaño} bits...", end=" ")
        
        try:
            resultado, tiempo = simular_hamming(cadena)
            
            print(f"Tiempo: {tiempo:.4f}s")
            
            if tiempo > limite_tiempo:
                print(f"⚠️  LÍMITE ALCANZADO: {tamaño} bits toma {tiempo:.2f}s")
                print(f"   Límite práctico recomendado: {tamaño//2} bits")
                break
            elif tiempo > limite_tiempo/2:
                print(f"⚠️  Acercándose al límite")
            
            tamaño += 100
            
            if tamaño > 2000:  # Límite de seguridad
                print("🛑 Límite de seguridad alcanzado (2000 bits)")
                break
                
        except Exception as e:
            print(f"❌ Error: {e}")
            break

# Ejecutar todas las pruebas
if __name__ == "__main__":
    print("🧪 PRUEBAS DE RENDIMIENTO - CÓDIGO HAMMING")
    print("=" * 50)
    
    # Ejecutar solo la prueba de rendimiento
    prueba_rendimiento_detallada()
    
    print("\n" + "=" * 50)
    print("✅ PRUEBA DE RENDIMIENTO COMPLETADA")