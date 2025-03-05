# Fixitly - Plataforma de Autónomos para Oficios 🛠️

**Fixitly** es una plataforma innovadora que conecta a clientes con autónomos especializados en oficios como fontanería, electricidad, carpintería y pintura. Con un enfoque en rapidez 🚀, confianza 🔒 y tecnología 🌐, Fixitly ofrece cotizaciones automáticas con IA, mapas en vivo, seguimiento en tiempo real y un proceso de contratación simplificado.

Este repositorio contiene el código fuente del proyecto, con un frontend en **React** y un backend en **Flask**, todo contenerizado con **Docker** para un despliegue fácil y consistente.

## Características principales ✨
- **Cotizaciones inteligentes** 🤖: Estimaciones automáticas basadas en datos históricos e IA.
- **Mapa interactivo** 🗺️: Autónomos disponibles en tiempo real según ubicación.
- **Seguimiento en vivo** ⏱️: Actualizaciones del estado del trabajo para clientes.
- **Perfiles verificados** ✅: Certificaciones y reseñas para generar confianza.
- **Pagos seguros** 💳: Integración para transacciones protegidas.

## Tecnologías utilizadas 🛠️

### Backend
- ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask) **Flask**: Framework ligero para la API REST.
- ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF6F61?style=flat) **SQLAlchemy**: ORM para interactuar con la base de datos PostgreSQL.
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql) **PostgreSQL**: Base de datos relacional para almacenar usuarios, trabajos y reseñas.
- ![Pydantic](https://img.shields.io/badge/Pydantic-FF6F61?style=flat) **Pydantic**: Validación de datos y esquemas.
- ![Flask-JWT-Extended](https://img.shields.io/badge/Flask--JWT-000000?style=flat) **Flask-JWT-Extended**: Autenticación basada en JWT.
- ![Flask-CORS](https://img.shields.io/badge/Flask--CORS-000000?style=flat) **Flask-CORS**: Soporte para solicitudes cross-origin.

### Frontend
- ![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react) **React**: Biblioteca para interfaces dinámicas y responsivas.
- ![Material-UI](https://img.shields.io/badge/Material--UI-0081CB?style=flat&logo=mui) **Material-UI**: Componentes estilizados para un diseño moderno y consistente.
- ![Redux Toolkit](https://img.shields.io/badge/Redux_Toolkit-764ABC?style=flat&logo=redux) **Redux Toolkit**: Gestión eficiente del estado global de la aplicación.
- ![React Router](https://img.shields.io/badge/React_Router-CA4245?style=flat) **React Router**: Navegación entre páginas y rutas.

### Infraestructura
- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker) **Docker**: Contenerización para desarrollo y producción.

## Requisitos previos 📋
- ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker) Docker y Docker Compose instalados.
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python) Python 3.9+ (si ejecutas sin Docker).
- ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs) Node.js y npm (para el frontend).

## Instalación y configuración 🚀
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/fixitly.git
   cd fixitly