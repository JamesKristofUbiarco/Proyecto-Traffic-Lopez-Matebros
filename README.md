# 🚦 Proyecto-Traffic-Lopez-Matebros

**Proyecto Final para la Asignatura de Programación II**

---

## 🎯 Descripción del Problema

Este proyecto simula un **Sistema de Gestión para una Avenida Inteligente** (simulando Av. López Mateos). El objetivo principal es la **coordinación y respuesta automatizada** ante incidentes viales y el **monitoreo de vehículos en tiempo real**.

El software permite:
* ✅ Registrar vehículos y monitorear su velocidad.
* ⚠️ Reportar diversos tipos de incidentes (choques, baches, tráfico).
* 🚨 Generar **alertas automáticas y contextualizadas** (ej. si el incidente ocurre dentro de un túnel).

---

## 💡 Justificación de Programación Orientada a Objetos (POO)

El problema de gestión de tráfico es un caso de estudio ideal para la **Programación Orientada a Objetos** debido a los siguientes pilares:

* **Objetos Interactivos:** Las entidades `Vehículos` e `Incidentes` son objetos con estados (ubicación, velocidad) y comportamientos (generar_alerta, recibir_alerta).
* **Herencia:** Se manejan diferentes tipos de incidentes (`Accidente`, `CondicionVial`, `Trafico`) que comparten características base (`Incidente`) pero tienen implementaciones específicas.
* **Polimorfismo:** El método de generación de alertas actúa de forma diferente según el tipo de incidente, permitiendo un manejo flexible y extensible de las notificaciones.

---

## 🏗️ Estructura del Proyecto

### 🗺️ Diagrama de Flujo (FlowChart)

<img src="https://i.ibb.co/MwGw5Zx/diagrama-de-flujo.png" alt="diagrama-de-flujo" border="0" style="max-width: 800px; display: block; margin: 0 auto;">

### 📊 Diagrama de Clases (UML)

<img src="https://i.ibb.co/Kz5NdnJF/UML.png" alt="UML" border="0" style="max-width: 800px; display: block; margin: 0 auto;">

> 📝 **Nota:** La arquitectura principal se centra en el `GestorAvenida`, que funciona como un *contenedor* y motor de lógica, administrando las colecciones de `Vehiculos` y `Incidentes`.

### 🔑 Clases Principales

| Clase | Descripción | Responsabilidad Clave |
| :--- | :--- | :--- |
| **`GestorAvenida`** | Clase Contenedora y de Lógica Central. | Administra colecciones, detecta cercanía de eventos/autos y dispara las alertas. |
| **`Vehiculo`** | Actor Móvil del Sistema. | Representa a un auto, mantiene su estado (velocidad, ubicación) y recibe las alertas. |
| **`Incidente`** | **Superclase Abstracta** para eventos en la vía. | Define la estructura base (`ubicación`, `tipo`) para todas las alertas. |
| **`Accidente`** | Subclase de `Incidente`. | Eventos críticos (choques). Genera alertas con instrucciones de emergencia. |
| **`CondicionVial`** | Subclase de `Incidente`. | Estado del camino (baches, deslaves). |
| **`Trafico`** | Subclase de `Incidente`. | Congestión o alta densidad vehicular. |
| **`AlertaConductor`**| Subclase de `Incidente`. | Avisos directos al conductor (ej. exceso de velocidad). |

---

## ✨ Implementación del Polimorfismo

El polimorfismo se demuestra en el método central **`generar_alerta()`**:

1.  El `GestorAvenida` simplemente itera sobre su lista de `Incidentes` y llama a `incidente.generar_alerta()`.
2.  El sistema de Python ejecuta dinámicamente la versión correcta del método (el **Polimorfismo de Inclusión**):
    * Si es un objeto **`Accidente`**: La alerta incluye **instrucciones de emergencia y seguridad**.
    * Si es un objeto **`Trafico`**: La alerta sugiere **acciones menos críticas** como apagar el motor.
3.  Además, todas las subclases de `Incidente` verifican **polimórficamente** si la ubicación del evento corresponde a un túnel mediante el método heredado **`tunel()`**, permitiendo que la alerta sea *contextualizada*.
"
## Instrucciones de Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/JamesKristofUbiarco/Proyecto-Traffic-Lopez-Matebros.git](https://github.com/JamesKristofUbiarco/Proyecto-Traffic-Lopez-Matebros.git)
    ```
2.  **Navegar a la carpeta:**
    ```bash
    cd Proyecto-Traffic-Lopez-Matebros
    ```
3.  **Ejecutar la simulación:**
    ```bash
    python main.py
    ```

**Salida esperada:**
El programa inicializará el gestor, creará vehículos, simulará un exceso de velocidad y reportará un choque, mostrando las alertas correspondientes en consola.

## Organización del Equipo y Roles

El equipo está conformado por 4 integrantes, distribuyendo las responsabilidades para asegurar la calidad del código y la documentación:

| Miembro | Rol | Responsabilidades Principales |
| :--- | :--- | :--- |
| **James Kristof Ubiarco Rodriguez** | Arquitecto de Software / Líder | Diseño de la estructura de clases (`Gestor`, `Main`), integración del código y supervisión del diseño UML. |
| **José Ángel Gutiérrez Lomelí** | Desarrollador Backend (Lógica) | Implementación de la lógica de `Incidentes` y el manejo de coordenadas en el sistema de túneles. |
| **Juan Alexander Rodríguez Nájera** | Desarrollador Backend (Objetos) | Desarrollo de la clase `Vehiculo` y la lógica de recepción de alertas y actualización de estados. |
| **Esteban Ramírez Bailón** | Especialista en Documentación y QA | Redacción del README, creación de diagramas de flujo, y pruebas de los casos de polimorfismo (Pruebas manuales). |

---
*Proyecto final para la asignatura de Programación II.*