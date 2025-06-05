# 🏢 Sistema de Gestión Empresarial - Backend

Backend del sistema de gestión empresarial desarrollado con Django y MySQL.

## ⚡ Tecnologías Principales

- 🐍 Python 3.11+
- 🎯 Django 4.2+
- 🗄️ MySQL 8.0+
- 🔄 Django REST Framework
- 🔒 JWT Authentication
- 📝 Swagger/OpenAPI

## 📋 Requisitos Previos

- 🐍 Python 3.11+
- 🗄️ MySQL 8.0+
- 📦 Git

## 🚀 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/RegencyRRHH/HorasSistem.git
cd HorasSistem_Backend
```

2. **Crear y activar el entorno virtual:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
   - 📝 Crear archivo `.env` en la raíz
   - ⚙️ Configurar las siguientes variables:
```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=horassistema
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

5. **Ejecutar migraciones:**
```bash
python manage.py migrate
```

6. **Crear superusuario:**
```bash
python manage.py createsuperuser
```

7. **Iniciar servidor:**
```bash
python manage.py runserver
```

## 📚 Documentación API

- 📘 Swagger UI: `http://localhost:8000/swagger/`
- 📗 ReDoc: `http://localhost:8000/redoc/`

## 📁 Estructura del Proyecto

```
HorasSistem_Backend/
├── 📂 empresas/          # Gestión empresarial
├── 👥 usuarios/          # Autenticación y usuarios
├── ⚙️ horas_sistema/     # Configuración principal
│   ├── settings/        # Configuraciones
│   ├── urls.py         # URLs principales
│   └── wsgi.py         # Config WSGI
├── 📝 requirements/     # Requisitos
└── ⚡ manage.py         # Script admin
```

## 🔑 Características Principales

- 🔒 Autenticación JWT
- 📊 Panel administrativo personalizado
- 🌐 API REST completa
- 📝 Documentación automática
- 🛡️ CORS configurado
- 🔐 Gestión de permisos

## 🛣️ Endpoints Principales

- 🏢 `/api/empresas/` - Gestión de empresas
- 📊 `/api/unidades/` - Unidades de negocio
- 📋 `/api/proyectos/` - Gestión de proyectos
- 🏗️ `/api/centros-operativos/` - Centros operativos
- 👥 `/api/cargos/` - Catálogo de cargos

## 🤝 Contribución

1. **Crear rama feature:**
```bash
git checkout -b feature/nueva-funcionalidad
```

2. **Commits significativos:**
```bash
git commit -m "feat: añade nueva funcionalidad"
```

3. **Push de cambios:**
```bash
git push origin feature/nueva-funcionalidad
```

## 📜 Convenciones

- 📝 Commits siguiendo [Conventional Commits](https://www.conventionalcommits.org/)
- 🐍 Código siguiendo [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- 📚 Documentación en español

## ⚖️ Licencia

Este proyecto está bajo la Licencia Regency SaS.




