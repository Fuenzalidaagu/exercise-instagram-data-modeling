import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    nombre_usuario = Column(String)
    contraseña = Column(String)
    foto_perfil = Column(String)
    fecha_nacimiento = Column(DateTime)
    genero = Column(String)
    pais = Column(String)
    ciudad = Column(String)
    descripcion_perfil = Column(String)
    fecha_registro = Column(DateTime)
    ultimo_inicio_sesion = Column(DateTime)
    
class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    contenido = Column(String)
    fecha_hora = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship("Usuario", back_populates="publicaciones")
    
class Comentario(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    contenido = Column(String)
    fecha_hora = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id'))
    usuario = relationship("Usuario", back_populates="comentarios")
    publicacion = relationship("Publicacion", back_populates="comentarios")
    
class MeGusta(Base):
    __tablename__ = 'me_gusta'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id'))
    fecha_hora = Column(DateTime)
    usuario = relationship("Usuario", back_populates="me_gusta")
    publicacion = relationship("Publicacion", back_populates="me_gusta")

class Notificacion(Base):
    __tablename__ = 'notificaciones'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    fecha_hora = Column(DateTime)
    id_usuario_envio = Column(Integer, ForeignKey('usuarios.id'))
    id_usuario_recepcion = Column(Integer, ForeignKey('usuarios.id'))
    usuario_envio = relationship("Usuario", foreign_keys=[id_usuario_envio])
    usuario_recepcion = relationship("Usuario", foreign_keys=[id_usuario_recepcion])
    
class Seguidor(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)
    id_usuario_seguidor = Column(Integer, ForeignKey('usuarios.id'))
    id_usuario_seguido = Column(Integer, ForeignKey('usuarios.id'))
    fecha_hora = Column(DateTime)
    usuario_seguidor = relationship("Usuario", foreign_keys=[id_usuario_seguidor])
    usuario_seguido = relationship("Usuario", foreign_keys=[id_usuario_seguido])
    
class Etiqueta(Base):
    __tablename__ = 'etiquetas'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id'))
    usuario = relationship("Usuario")
    publicacion = relationship("Publicacion")
    
class Bloqueado(Base):
    __tablename__ = 'bloqueados'
    id = Column(Integer, primary_key=True)
    id_usuario_bloqueador = Column(Integer, ForeignKey('usuarios.id'))
    id_usuario_bloqueado = Column(Integer, ForeignKey('usuarios.id'))
    fecha_hora = Column(DateTime)
    usuario_bloqueador = relationship("Usuario", foreign_keys=[id_usuario_bloqueador])
    usuario_bloqueado = relationship("Usuario", foreign_keys=[id_usuario_bloqueado])

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
