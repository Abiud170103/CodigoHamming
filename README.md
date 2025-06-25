# Código de Hamming en Python

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Implementación del **Código de Hamming** para detección y corrección de errores en transmisión de datos, desarrollado en Python como parte de un proyecto de redes de computadoras.

## 📋 Descripción

El código de Hamming es un método de codificación que permite detectar y corregir errores de un solo bit en la transmisión de datos. Es ampliamente utilizado en redes de computadoras y sistemas de comunicación para garantizar la integridad de la información.

### Características principales:
- ✅ **Codificación** de datos binarios con bits de paridad
- 🔍 **Detección** automática de errores
- 🔧 **Corrección** de errores de un solo bit
- 📊 **Análisis** detallado del proceso
- 🧪 **Pruebas de estrés** incluidas

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior
- Dependencias para pruebas (opcional):
  ```bash
  pip install psutil memory-profiler
  ```

### Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/CodigoHamming.git
cd CodigoHamming
```

## 💻 Uso

### Ejecución básica
```bash
python hamming.py
```

El programa te pedirá:
1. **Ingresa la información a enviar**: Introduce una cadena binaria (ej: `1010`)
2. **Información recibida**: Introduce la trama recibida (puede contener errores)

### Ejemplo de ejecución
```
Ingresa la información que desea enviar: 1010
Se muestra la información de (1010) codificada en código hamming: [1, 0, 1, 1, 0, 1, 0]

Por favor ingrese la información recibida: 1011010
	No se detectaron errores
Trama codificada  enviada: 	 [1, 0, 1, 1, 0, 1, 0]
Trama codificada recibida: 	 1011010
```

## 🏗️ Estructura del Proyecto

```
CodigoHamming/
├── hamming.py          # Implementación principal del código de Hamming
├── pruebas.py         # Pruebas de estrés y rendimiento
├── README.md          # Documentación del proyecto
└── models/            # Modelos y estructuras adicionales
```

## 🔧 Algoritmo

### 1. Determinación de bits de paridad
Para **m** bits de información, se necesitan **r** bits de paridad donde:
```
2^r ≥ m + r + 1
```

### 2. Posicionamiento
Los bits de paridad se colocan en posiciones que son potencias de 2:
- Posición 1, 2, 4, 8, 16, 32...

### 3. Cálculo de paridad
Cada bit de paridad controla posiciones específicas según su representación binaria.

### 4. Detección y corrección
- Si todos los bits de verificación son 0 → **Sin errores**
- Si hay bits de verificación = 1 → **Error detectado y corregido**

## 📊 Pruebas de Rendimiento

### Ejecutar pruebas
```bash
python pruebas.py
```

### Resultados de rendimiento (hasta 100 bits):
- ⚡ **Tiempo promedio**: 0.0001s
- 📈 **Escalabilidad**: Crecimiento lineal O(m×r)
- 💾 **Uso de memoria**: Muy eficiente
- 🔢 **Límite recomendado**: 1000 bits de información

### Ejemplos de bits de paridad necesarios:
| Bits de información | Bits de paridad | Bits totales |
|-------------------|----------------|-------------|
| 4                 | 3              | 7           |
| 11                | 4              | 15          |
| 26                | 5              | 31          |
| 57                | 6              | 63          |
| 120               | 7              | 127         |

## ⚠️ Limitaciones

1. **Solo corrige 1 bit de error** por trama
2. **Entrada debe ser binaria válida** (solo '0' y '1')
3. **Rendimiento** se degrada con entradas muy largas (>1000 bits)
4. **No detecta errores múltiples** correctamente

## 🎯 Casos de uso

- **Redes de computadoras**: Transmisión confiable de datos
- **Almacenamiento**: Integridad en memoria RAM, discos
- **Comunicaciones**: Enlaces satelitales, fibra óptica
- **Educación**: Comprensión de códigos correctores de errores

## 🧪 Pruebas incluidas

- **Prueba básica de estrés**: Diferentes tamaños de entrada
- **Análisis de memoria**: Monitoreo de uso de recursos
- **Casos extremos**: Patrones específicos y casos límite
- **Rendimiento detallado**: Análisis de complejidad temporal
- **Búsqueda de límites**: Determinación de capacidad máxima

## 📚 Documentación técnica

### Funciones principales:

#### `esPotenciaDeDos(numero)`
Determina si un número es potencia de dos usando operaciones bit a bit.

#### Proceso de codificación:
1. Ingreso y validación de datos
2. Cálculo de posiciones de paridad
3. Generación de bits de paridad
4. Construcción de trama codificada

#### Proceso de decodificación:
1. Recepción de trama
2. Recálculo de bits de verificación
3. Detección de errores
4. Corrección automática si es necesario

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.


## 🙏 Agradecimientos

- Instituto Politécnico Nacional
- Curso de Redes de Computadoras
- Comunidad de desarrolladores Python

---

⭐ **¡Dale una estrella si este proyecto te ayudó!** ⭐
