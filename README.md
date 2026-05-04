# Autoencoders aplicados a la clasificación de ciberataques

> Proyecto final — Machine Learning II · Grado en Matemáticas · UNIE Universidad

---

## Descripción

Este proyecto implementa una solución de Deep Learning diseñada para la clasificación de amenazas en entornos de red. La arquitectura utiliza un enfoque híbrido para maximizar la eficiencia y precisión:

* Reducción de Dimensionalidad: Implementación de un Autoencoder para comprimir el espacio de características, filtrando el ruido y extrayendo las representaciones más latentes del dataset de ciberseguridad.

* Clasificación: Un Perceptrón Multicapa (\textbf{MLP}) integrado que utiliza las características optimizadas para categorizar con alta precisión los diferentes tipos de ataques.

## Instalación

  ```bash
  git clone https://github.com/PabloDelaFuenteArteaga/autoencoders-ciberseguridad.git
  cd autoencoders-ciberseguridad
  pip install uv
  uv sync --group dev
  ```

## Data Download

La base de datos no está incluida en el proyecto. Para descargarla se deberá acceder a:

**[OpenML](https://www.openml.org/search?type=data&sort=runs&id=45279&status=active)**


## Estructura del proyecto

  ```
  autoencoders-ciberseguridad/
  ├── notebooks/                                   # Notebooks about preprocessing
  ├── scripts                                      # Data filters
  ├── .gitignore
  ├── Contexto_del_problema_y_estado_del_arte.pdf  # State of the art
  └── README.md
  ```

## Autores

**Pablo De la Fuente Arteaga** · [github.com/PabloDelaFuenteArteaga](https://github.com/PabloDelaFuenteArteaga)
**Rubén Torres Rodríguez** · [github.com/Ruben-2004](https://github.com/Ruben-2004)
**Alfonso González Avinzini** · [github.com/fonsiga03-droid](https://github.com/fonsiga03-droid)
