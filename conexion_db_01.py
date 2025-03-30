from tkinter import messagebox
import tkinter as tk

import mysql.connector
from reportes_pdf import*

import mysql.connector
from datetime import timedelta
from datetime import datetime

import mysql.connector
#from mysql.connector import Error

import pymysql

class ConexConexion:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                user='root',
                host='localhost',
                database='gestion_inscripcion',
                password='',  # Asegúrate de que este valor es correcto
                port=3306
            )
            if self.connection:
                print("Conexión exitosa a la base de datos")
        # Cambiamos mysql.connector.Error por pymysql.MySQLError
        except pymysql.MySQLError as e:
            print(f"Error al conectar a MySQL: {e}")
            self.connection = None  # Asignar None si la conexión falla

    def __enter__(self):
        if self.connection:
            self.micursor = self.connection.cursor()  # Crea el cursor aquí
            return self  # Devuelve la instancia de la clase
        else:
            raise RuntimeError("No se pudo establecer la conexión a la base de datos")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.micursor:  # Cierra el cursor si existe
            self.micursor.close()
        if self.connection:  # Cierra la conexión
            self.connection.close()





#                                                       CARGAR DATOS EN EL TREEVIEW
def mostrar_ambiente_en_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "pensum"
        sql_select = "SELECT Id, Ambiente, Seccion, dia FROM ambiente"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_ambiente.get_children():
            self.treeview_ambiente.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_ambiente.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 1.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:", e)

def mostrar_horas_en_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "pensum"
        sql_select = "SELECT id, hora_inicial, hora_final FROM horas"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_horas.get_children():
             self.treeview_horas.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
             self.treeview_horas.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 2.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview: 2", e)

def mostrar_asignacion_hr_amb_en_treeview(self):
    try:
        # Consulta para obtener los registros con los JOIN necesarios
        sql_select = """
        SELECT 
            asignacion_hr_amb.id, 
            asignacion_hr_amb.id_hora, 
            asignacion_hr_amb.id_ambiente, 
            horas.hora_inicial, 
            horas.hora_final, 
            ambiente.ambiente, 
            ambiente.seccion, 
            ambiente.dia
        FROM 
            asignacion_hr_amb
        JOIN 
            horas ON asignacion_hr_amb.id_hora = horas.id
        JOIN 
            ambiente ON asignacion_hr_amb.id_ambiente = ambiente.id;

        """
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_hr_amb.get_children():
            self.treeview_hr_amb.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_hr_amb.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 3.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview: 3", e)

        

def mostrar_asig_faci_hora_treeview(self):
    try:
        sql_select = """               
                                  SELECT 
    afc.id AS 'Id',                      -- ID de asignacion_facilitador_curso
    f.cedula AS 'Cedula',                -- Cedula del facilitador
    f.nombre AS 'Nombre',                -- Nombre del facilitador
    f.apellido AS 'Apellido',            -- Apellido del facilitador
    afc.id_asignacion_hr_amb AS 'Id_asig_hr_amb',  -- ID de asignacion_hr_amb
    h.hora_inicial AS 'Hora Inicial',    -- Hora inicial de la asignacion_hr_amb
    h.hora_final AS 'Hora Final',        -- Hora final de la asignacion_hr_amb
    a.ambiente AS 'Ambiente',            -- Ambiente de la asignacion_hr_amb
    a.seccion AS 'Seccion',              -- Sección de la asignacion_hr_amb
    a.dia AS 'Dia',                      -- Día de la asignacion_hr_amb
    p.codigo AS 'Codigo',                -- Código del pensum
    p.curso AS 'Curso',                  -- Curso del pensum
    p.ciclo AS 'Ciclo'                   -- Ciclo del pensum
FROM 
    asignacion_facilitador_curso afc
JOIN 
    facilitador f ON afc.cedula_facilitador = f.cedula
JOIN 
    asignacion_hr_amb aha ON afc.id_asignacion_hr_amb = aha.id
JOIN 
    horas h ON aha.id_hora = h.id          -- Unirse a la tabla horas para obtener hora_inicial y hora_final
JOIN 
    ambiente a ON aha.id_ambiente = a.id
JOIN 
    pensum p ON afc.codigo_pensum = p.codigo;



                 """
  
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_asig_faci_hora.get_children():
            self.treeview_asig_faci_hora.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_asig_faci_hora.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview.6")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:6", e)

def mostrar_facilitador_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "facilitdor"
        sql_select = "SELECT cedula, nombre, apellido, horas_de_clase FROM facilitador"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_facilitador.get_children():
            self.treeview_facilitador.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_facilitador.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 7.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:7", e)


def mostrar_pensum_en_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "pensum"
        sql_select = "SELECT codigo, curso, credito, ciclo, carrera, mencion FROM pensum"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros
            
        # Limpiar Treeview
        for row in self.treeview_pensum.get_children():
            self.treeview_pensum.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_pensum.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 8.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:8", e)

def mostrar_participante_treeview(self):
    try:
            # Consulta para obtener los registros de la tabla "participante"
        sql_select = sql_select = """
    SELECT cedula, nombre, apellido, sexo, edad, telefono, correo, estado, municipio, parroquia,
           discapacidad, grupo_i, programa, creditos_g, cursos_g, sistema
    FROM participante
"""


        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros

            # Limpiar Treeview
        for row in self.treeview_participante.get_children():
            self.treeview_participante.delete(row)

            # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_participante.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 9.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:9", e)



def mostrar_inscripcion_treeview(self): 
    try:
        # Consulta SQL para mostrar inscripciones
        sql_select =sql_select = """ 
    SELECT 
    p.cedula AS Cedula_Participante, 
    p.nombre AS Nombre_Participante, 
    p.apellido AS Apellido_Participante,
    afc.id AS Id_Asig_Fac_Curso, 
    f.cedula AS Cedula_Facilitador, 
    f.nombre AS Nombre_Facilitador, 
    f.apellido AS Apellido_Facilitador,
    hr.hora_inicial AS Hora_Inicial,
    hr.hora_final AS Hora_Final,
    a.ambiente AS Ambiente,
    a.dia AS Dia,
    a.seccion AS Seccion,
    pen.codigo AS Codigo_Pensum,
    pen.curso AS Curso,
    pen.ciclo AS Ciclo,
    ip.nombre AS Nombre_Periodo_Inscripcion,
    r.total_cursos AS Total_Cursos,
    r.total_creditos AS Total_Creditos,
    i.validada AS Validada
FROM 
    participante p 
JOIN 
    inscripcion i ON p.cedula = i.cedula_participante
JOIN 
    asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
JOIN 
    facilitador f ON afc.cedula_facilitador = f.cedula
JOIN 
    asignacion_hr_amb ah ON afc.id_asignacion_hr_amb = ah.id
JOIN 
    horas hr ON ah.id_hora = hr.id
JOIN 
    ambiente a ON ah.id_ambiente = a.id
JOIN 
    pensum pen ON afc.codigo_pensum = pen.codigo
LEFT JOIN 
    inscripcion_periodo ip ON i.nombre_inscripcion_periodo = ip.nombre
LEFT JOIN (
    SELECT 
        cedula_participante, 
        nombre_inscripcion_periodo, 
        MAX(total_cursos) AS total_cursos, 
        MAX(total_creditos) AS total_creditos
    FROM 
        resumen_participante_periodo
    GROUP BY 
        cedula_participante, 
        nombre_inscripcion_periodo
) r ON p.cedula = r.cedula_participante AND i.nombre_inscripcion_periodo = r.nombre_inscripcion_periodo  
GROUP BY 
    p.cedula, afc.id, i.nombre_inscripcion_periodo
ORDER BY 
    i.nombre_inscripcion_periodo;

"""

        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros

            # Imprimir los registros en consola
            print(f"Número de registros recuperados: {len(registros)}")
            for registro in registros:
                print(registro)  # Imprime cada registro en consola

        # Limpiar Treeview antes de insertar los registros
        for row in self.treeview_inscripcion.get_children():
            self.treeview_inscripcion.delete(row)

        # Insertar los registros en el Treeview
        for registro in registros:
            self.treeview_inscripcion.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview.")
        
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview INSCRIPCION:", e)

def mostrar_preseleccion_treeview(self):
        try:
            # Consulta para obtener los registros de la tabla "preseleccion"
            sql_select = """SELECT 
    pc.id AS "Id",
    pc.cedula_participante AS "Cedula Participante",
    pc.id_preseleccion_periodo AS "Id Periodo",
    p.fecha_inicio AS "Inicio",
    p.fecha_fin AS "Fin",
    pe.codigo AS "Codigo",
    pe.curso AS "Curso"
FROM 
    preseleccion_curso pc
JOIN 
    preseleccion_periodo p ON pc.id_preseleccion_periodo = p.id
JOIN 
    pensum pe ON pc.codigo_pensum = pe.codigo;


"""

            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_select)
                registros = conexion.micursor.fetchall()  # Obtiene todos los registros

                # Limpiar Treeview
                for row in self.treeview_preseleccion.get_children():
                    self.treeview_preseleccion.delete(row)

                # Insertar los registros en el Treeview
                for registro in registros:
                    self.treeview_preseleccion.insert("", "end", values=registro)

            print("Registros mostrados en el Treeview 11.")
        except mysql.connector.Error as e:
            print("Error al mostrar registros en el Treeview:11", e)

def mostrar_periodo_pre_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "periodo de preseleccion"
        sql_select = "SELECT id, fecha_inicio, fecha_fin FROM preseleccion_periodo"

        # Abre una conexión a la base de datos
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros

            # Limpiar Treeview
            for row in self.treeview_pre_periodo.get_children():
                self.treeview_pre_periodo.delete(row)

            # Insertar los registros en el Treeview
            for registro in registros:
                self.treeview_pre_periodo.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview.12")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:12", e)
    except Exception as e:
        print("Error inesperado:", e)

def mostrar_periodo_academico_treeview(self):
    try:
        # Consulta para obtener los registros de la tabla "periodo de preseleccion"
        sql_select = "SELECT nombre, fecha_inicio, fecha_fin FROM inscripcion_periodo"

        # Abre una conexión a la base de datos
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()  # Obtiene todos los registros

            # Limpiar Treeview
            for row in self.treeview_periodo_academico.get_children():
                self.treeview_periodo_academico.delete(row)

            # Insertar los registros en el Treeview
            for registro in registros:
                self.treeview_periodo_academico.insert("", "end", values=registro)

        print("Registros mostrados en el Treeview 13.")
    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview 13:", e)
    except Exception as e:
        print("Error inesperado:", e)



#                                                       CREAR REGISTROS
def crear_horas(self, id, hora_inicial, hora_final):
    try:
        # Inserta datos en la tabla "horas"
        sql_insert = "INSERT INTO horas (id, hora_inicial, hora_final) VALUES (%s, %s, %s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (id, hora_inicial, hora_final))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'Horas'.")
        self.mostrar_horas_en_treeview()

        # Limpiar los campos después de la inserción
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'horas':", e)
        return False  # Indica que hubo un error durante la inserción
    
def crear_ambiente(self, id, ambiente, seccion, dia):
    try:
        # Inserta datos en la tabla "pensum"
        sql_insert = "INSERT INTO ambiente (id, ambiente, seccion, dia) VALUES (%s, %s, %s,%s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (id, ambiente, seccion, dia))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'ambiente'.")
        self.mostrar_ambiente_en_treeview()
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'ambiente':", e)
        return False  # Indica que hubo un error durante la inserción
    
def crear_asignacion_hr_amb(self, id, id_hora, id_ambiente):
    try:
        # Inserta datos en la tabla "pensum"
        sql_insert = "INSERT INTO asignacion_hr_amb (id, id_hora, id_ambiente) VALUES (%s, %s,%s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (id, id_hora, id_ambiente))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'asignacion_hr_amb'.")
        self.mostrar_asignacion_hr_amb_en_treeview()
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'asignacion_hr_amb':", e)
        return False  # Indica que hubo un error durante la inserción
    


def crear_facilitador(self, cedula, nombre, apellido, horas_de_clase):
    try:
        # Inserta datos en la tabla "facilitador"
        sql_insert = "INSERT INTO facilitador (cedula, nombre, apellido, horas_de_clase) VALUES (%s, %s, %s, %s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (cedula, nombre, apellido, horas_de_clase))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'facilitador'.")
        self.mostrar_facilitador_treeview()  # Actualiza el TreeView de facilitadores
        self.limpiar_campos()
        cargar_datos_combobox_facilitador(self.cedulaf_cuadro)


        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'facilitador':", e)
        return False  # Indica que hubo un error durante la inserción



def crear_asignacion_facilitador_horario(self, id, cedula_facilitador, id_asignacion_hr_amb, codigo_pensum):
    try:
        # Inserta datos en la tabla "asignacion_facilitador_curso"
        sql_insert = "INSERT INTO asignacion_facilitador_curso (id, cedula_facilitador, id_asignacion_hr_amb, codigo_pensum) VALUES (%s, %s, %s, %s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (id, cedula_facilitador, id_asignacion_hr_amb, codigo_pensum))
            conexion.connection.commit()
        
        print("Datos insertados en la tabla 'asignacion_facilitador_curso'.")

        # Actualizar el TreeView de asignaciones y horarios
        self.mostrar_asig_faci_hora_treeview()
        
        # Actualizar el TreeView de facilitadores
        self.mostrar_facilitador_treeview()
        
        # Limpiar campos
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'asignacion_facilitador_curso':", e)
        return False  # Indica que hubo un error durante la inserción

def crear_pensum(self, codigo, curso, credito, ciclo, cupos, carrera, mencion):
    try:
        # Inserta datos en la tabla "pensum"
        sql_insert = "INSERT INTO pensum (codigo, curso, credito, ciclo, carrera, mencion) VALUES ( %s, %s, %s,%s,%s,%s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (codigo, curso, credito, ciclo, carrera, mencion))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'pensum'.")
        self.mostrar_pensum_en_treeview()
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'participante':", e)
        return False  # Indica que hubo un error durante la inserción
    

def crear_participante(self, cedula, nombre, apellido,sexo,edad,telefono,correo,estado,municipio,parroquia,discapacidad,grupo_i,programa, sistema):
        try:
            # Inserta datos en la tabla "participante"
            sql_insert = "INSERT INTO PARTICIPANTE (cedula, nombre, apellido, sexo, edad, telefono, correo, estado, municipio, parroquia, discapacidad, grupo_i, programa, sistema) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_insert, (cedula, nombre, apellido, sexo,edad,telefono,correo,estado,municipio,parroquia,discapacidad,grupo_i,programa,sistema))
                conexion.connection.commit()
            print("Datos insertados en la tabla 'participante'.")
            self.mostrar_participante_treeview()  # Actualizar Treeview después de la inserción
            self.limpiar_campos()
            cargar_datos_combobox_participante(self.cedulap_cuadro)


            return True  # Indica que la inserción fue exitosa

        except mysql.connector.Error as e:
            print("Error al insertar datos en la tabla 'participante':", e)
            return False  # Indica que hubo un error durante la inserción


def crear_inscripcion(self, cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo):
    try:
        with ConexConexion() as conexion:
            # Verifica si ya existe el registro
            sql_check = "SELECT COUNT(*) FROM inscripcion WHERE cedula_participante = %s AND id_asignacion_facilitador_curso = %s AND nombre_inscripcion_periodo = %s"
            conexion.micursor.execute(sql_check, (cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo))
            count = conexion.micursor.fetchone()[0]

            if count > 0:
                print("El registro ya existe.")
                return False  # Registro ya existe, no se inserta

            # Inserta datos en la tabla "inscripcion"
            sql_insert = "INSERT INTO inscripcion (cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo) VALUES (%s, %s, %s)"
            conexion.micursor.execute(sql_insert, (cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo))

            # Confirma la transacción
            conexion.connection.commit()

        print("Datos insertados en la tabla 'Inscripcion'.")
        
        # Limpia el Treeview antes de mostrar nuevos registros
        self.mostrar_inscripcion_treeview()
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'Inscripcion':", e)
        return False  # Indica que hubo un error durante la inserción


def crear_periodo_aca(self, nombre,fecha_inicio, fecha_fin):
    try:
        with ConexConexion() as conexion:
            # Inserta datos en la tabla "inscripcion_periodo"
            sql_insert = "INSERT INTO inscripcion_periodo (nombre,fecha_inicio, fecha_fin) VALUES (%s, %s, %s)"
            conexion.micursor.execute(sql_insert, (nombre,fecha_inicio, fecha_fin))

            # Confirma la transacción
            conexion.connection.commit()

        print("Datos insertados en la tabla 'inscripcion_periodo'.")
        self.mostrar_periodo_academico_treeview()  # Actualizar Treeview de inscripciones
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'inscripcion_periodo':", e)
        return False  # Indica que hubo un error durante la inserción

def crear_preseleccion(self, cedula_participante, id_preseleccion_periodo, codigo_pensum):
    try:
         # Inserta datos en la tabla "preseleccion_curso"
        sql_insert = "INSERT INTO preseleccion_curso (cedula_participante,id_preseleccion_periodo, codigo_pensum) VALUES (%s, %s, %s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (cedula_participante,id_preseleccion_periodo, codigo_pensum ))
            # Confirma la transacción
            conexion.connection.commit()
        print("Datos insertados en la tabla 'preseleccion_curso'.")
        self.mostrar_preseleccion_treeview()# Actualizar Treeview de preseleccion
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'preseleccion_curso':", e)
        return False  # Indica que hubo un error durante la inserción


def crear_periodo_preseleccion(self, fecha_inicio, fecha_fin):
    try:
        # Inserta datos en la tabla "preseleccion_periodo"
        sql_insert = "INSERT INTO preseleccion_periodo ( fecha_inicio, fecha_fin) VALUES (%s, %s)"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_insert, (fecha_inicio, fecha_fin))
            conexion.connection.commit()
        print("Datos insertados en la tabla 'preseleccion_periodo'.")
        self.mostrar_periodo_pre_treeview()
        self.limpiar_campos()

        return True  # Indica que la inserción fue exitosa

    except mysql.connector.Error as e:
        print("Error al insertar datos en la tabla 'preseleccion_periodo':", e)
        return False  # Indica que hubo un error durante la inserción
    

#                       REPORTES PDF
def generar_reporte_inscripciones_general():
    try:
        sql_select = """SELECT 
    p.cedula AS cedula_participante,
    p.nombre AS nombre_participante,
    p.apellido AS apellido_participante,
    f.cedula AS cedula_facilitador,
    f.nombre AS nombre_facilitador,
    f.apellido AS apellido_facilitador,
    h.hora_inicial,
    h.hora_final,
    a.ambiente,
    a.dia,
    a.seccion,
    pn.codigo AS codigo_pensum,
    pn.curso,
    pn.ciclo,
    ip.nombre AS nombre_periodo
FROM 
    inscripcion i
JOIN 
    participante p ON i.cedula_participante = p.cedula
JOIN 
    asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
JOIN 
    facilitador f ON afc.cedula_facilitador = f.cedula
JOIN 
    pensum pn ON afc.codigo_pensum = pn.codigo
JOIN 
    asignacion_hr_amb aha ON afc.id_asignacion_hr_amb = aha.id
JOIN 
    horas h ON aha.id_hora = h.id
JOIN 
    ambiente a ON aha.id_ambiente = a.id
JOIN 
    inscripcion_periodo ip ON i.nombre_inscripcion_periodo = ip.nombre

                    """
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()

        # Llamar a la función específica para generar el reporte general
        ruta_archivo = generar_reporte_general_pdf(registros)

        if ruta_archivo:
            messagebox.showinfo("Éxito", "Reporte general generado con éxito.")
            abrir_pdf(ruta_archivo)
        else:
            messagebox.showerror("Error", "Hubo un error al generar el reporte general.")
        
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte general: {e}")

def generar_reporte_inscripcion_individual(cedula_participante, nombre_inscripcion_periodo):
    try:
        sql_select = """
            SELECT 
    p.cedula,
    p.nombre,
    p.apellido,
    p.programa,
    f.cedula AS cedula_facilitador,
    f.nombre AS nombre_facilitador,
    f.apellido AS apellido_facilitador,
    h.hora_inicial,
    h.hora_final,
    a.ambiente,
    a.dia,
    a.seccion,
    p2.codigo AS codigo_pensum,
    p2.curso,
    p2.ciclo,
    ip.nombre AS nombre_periodo,
    r.total_cursos,
    r.total_creditos
FROM 
    inscripcion i
JOIN 
    participante p ON i.cedula_participante = p.cedula
JOIN 
    asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
JOIN 
    facilitador f ON afc.cedula_facilitador = f.cedula
JOIN 
    pensum p2 ON afc.codigo_pensum = p2.codigo
JOIN 
    asignacion_hr_amb aha ON afc.id_asignacion_hr_amb = aha.id
JOIN 
    horas h ON aha.id_hora = h.id
JOIN 
    ambiente a ON aha.id_ambiente = a.id
JOIN 
    inscripcion_periodo ip ON i.nombre_inscripcion_periodo = ip.nombre
LEFT JOIN 
    resumen_participante_periodo r ON p.cedula = r.cedula_participante AND i.nombre_inscripcion_periodo = r.nombre_inscripcion_periodo
WHERE 
    p.cedula = %s AND ip.nombre = %s;
        """
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (cedula_participante, nombre_inscripcion_periodo))
            registros = conexion.micursor.fetchall()

        # Depuración: Imprimir registros obtenidos
        for registro in registros:
            print(registro)

        if registros:
            ruta_archivo = generar_reporte_individual_pdf(registros, cedula_participante)
            if ruta_archivo:
                messagebox.showinfo("Éxito", f"Reporte individual generado con éxito: {ruta_archivo}")
                abrir_pdf(ruta_archivo)
            else:
                messagebox.showerror("Error", "Hubo un error al generar el reporte individual.")
        else:
            messagebox.showwarning("Advertencia", "No se encontró el participante con la cédula y el periodo proporcionados.")
        
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte individual: {e}")


def obtener_datos_preseleccion():
    try:
        with ConexConexion() as conn:
            query = """
            SELECT 
                p.cedula,
                pp.fecha_inicio,
                pp.fecha_fin,
                pe.codigo,
                pe.curso
            FROM 
                preseleccion_curso pc
            JOIN 
                participante p ON pc.cedula_participante = p.cedula
            JOIN 
                preseleccion_periodo pp ON pc.id_preseleccion_periodo = pp.id
            JOIN 
                pensum pe ON pc.codigo_pensum = pe.codigo;
            """
            conn.micursor.execute(query)  # Usa el cursor de la conexión
            datos = conn.micursor.fetchall()  # Usa el cursor de la conexión
            print(f"Datos obtenidos: {datos}")  # Debug: Verificar los datos obtenidos
            return datos
    except Exception as e:
        print(f"Error al obtener datos de preselección: {e}")
        return []


def generar_reporte_participantes():
    try:
        sql_select = """
        SELECT 
    cedula, 
    nombre, 
    apellido, 
    sexo, 
    edad, 
    telefono, 
    correo, 
    estado, 
    municipio, 
    parroquia, 
    discapacidad, 
    grupo_i, 
    programa, 
    cursos_g AS total_cursos,  -- Actualizado según la nueva columna cursos_g
    creditos_g AS total_creditos,  -- Actualizado según la nueva columna creditos_g
    sistema
FROM 
    participante;

        """

        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select)
            registros = conexion.micursor.fetchall()

        # Validar la cantidad de columnas antes de generar el reporte
        if registros and len(registros[0]) != 16:  # Verificar que haya 16 columnas en cada registro
            raise ValueError("El número de columnas en los registros no coincide con el esperado.")

        ruta_archivo = generar_reporte_participante_pdf(registros, "reporte_participantes")
        
        if ruta_archivo:
            messagebox.showinfo("Éxito", "Reporte de participantes generado con éxito.")
            abrir_pdf(ruta_archivo)
        else:
            messagebox.showerror("Error", "Hubo un error al generar el reporte de participantes.")
        
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte de participantes: {e}")





#                                    BUSCAR DATOS

def buscar_ambiente_por_nombre(main_app_instance, nombre_ambiente):
    try:
        sql_select = "SELECT id, ambiente, seccion, dia FROM ambiente WHERE ambiente = %s"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (nombre_ambiente,))
            registros = conexion.micursor.fetchall()
        
        # Limpiar el Treeview
        for row in main_app_instance.treeview_ambiente.get_children():
            main_app_instance.treeview_ambiente.delete(row)

        # Insertar los registros en el Treeview y cargar en los Entry
        if registros:
            for registro in registros:
                main_app_instance.treeview_ambiente.insert("", "end", values=registro)
                
                # Cargar los datos en los Entry
                main_app_instance.idamb_cuadro_var.set(registro[0])  # ID
                main_app_instance.ambiente_cuadro_var.set(registro[1])  # Ambiente
                main_app_instance.seccion_cuadro_var.set(registro[2])  # Sección
                main_app_instance.dia_cuadro_var.set(registro[3])  # Día
            
            print("Registros mostrados en el Treeview y datos cargados en los Entry.")
        else:
            print("No se encontraron registros.")
        
        return True  # Indica que la búsqueda fue exitosa

    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:", e)
        return False  # Indica que hubo un error durante la búsqueda


def buscar_asignacion_hr_amb_por_id(self, id):
    try:
        # Selecciona datos de la tabla "asignacion_hr_amb" donde el id coincida
        sql_select = "SELECT id_hora, id_ambiente FROM asignacion_hr_amb WHERE id = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (id,))
            resultado = conexion.micursor.fetchone()  # Obtiene un solo registro

        if resultado:
            print("Registro encontrado:", resultado)
            return resultado  # Devuelve el registro encontrado
        else:
            print("No se encontró ningún registro con el id:", id)
            return None  # No se encontró registro

    except mysql.connector.Error as e:
        print("Error al buscar datos en la tabla 'asignacion_hr_amb':", e)
        return None  # Indica que hubo un error durante la búsqueda

def buscar_participante_por_cedula(self, cedula):
    try:
        sql_select = "SELECT * FROM participante WHERE cedula = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (cedula,))
            resultado = conexion.micursor.fetchone()
            print(resultado)  # Imprimir el resultado para verificar
            if resultado:
                return resultado
            else:
                print(f"No se encontró ningún registro con la cédula {cedula}")
                return None
    except mysql.connector.Error as e:
        print(f"Error al buscar el participante con la cédula {cedula}: {e}")
        return None



def buscar_hora(self, id_hora):
    try:
        # Consulta para buscar una hora por su ID
        sql_select = "SELECT * FROM horas WHERE id = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (id_hora,))
            resultado = conexion.micursor.fetchone()  # Recupera el primer resultado que coincida

        if resultado:
            id_hora, hora_inicial, hora_final = resultado

            # Convertir timedelta a formato 'HH:MM:SS' manualmente
            hora_inicial_str = str(hora_inicial)  # Convierte directamente a string 'HH:MM:SS'
            hora_final_str = str(hora_final)  # Convierte directamente a string 'HH:MM:SS'

            print(f"Hora encontrada: ID={id_hora}, Hora Inicial={hora_inicial_str}, Hora Final={hora_final_str}")
            return id_hora, hora_inicial_str, hora_final_str  # Devolver el formato de hora legible

        else:
            print(f"No se encontró ninguna hora con ID: {id_hora}")
            return None  # Indica que no se encontró ninguna hora

    except mysql.connector.Error as e:
        print(f"Error al buscar hora con ID {id_hora}: {e}")
        return None  # Indica que hubo un error durante la búsqueda

def buscar_pensum_por_codigo(self, codigo):
    try:
        # Consulta SQL para buscar un registro por código en la tabla "pensum"
        sql_select = "SELECT * FROM pensum WHERE codigo = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (codigo,))
            resultado = conexion.micursor.fetchone()  # fetchone para obtener un solo resultado
            if resultado:
                return resultado  # Devuelve el registro encontrado
            else:
                print(f"No se encontró ningún registro con el código {codigo}")
                return None

    except mysql.connector.Error as e:
        print(f"Error al buscar el pensum con el código {codigo}: {e}")
        return None

def buscar_asignacion_facilitador_horario(self, id=None, cedula_facilitador=None, id_asignacion_hr_amb=None):
    try:
        if id:
            # Buscar por ID
            sql_select = "SELECT * FROM asignacion_facilitador_curso WHERE id = %s"
            parametros = (id,)
        elif cedula_facilitador:
            # Buscar por cédula del facilitador
            sql_select = "SELECT * FROM asignacion_facilitador_curso WHERE cedula_facilitador = %s"
            parametros = (cedula_facilitador,)
        elif id_asignacion_hr_amb:
            # Buscar por id_asignacion_hr_amb
            sql_select = "SELECT * FROM asignacion_facilitador_curso WHERE id_asignacion_hr_amb = %s"
            parametros = (id_asignacion_hr_amb,)
        else:
            print("No se proporcionó un criterio de búsqueda válido.")
            return None
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, parametros)
            resultado = conexion.micursor.fetchone()  # Traer un solo resultado
        
        if resultado:
            print(f"Registro encontrado: {resultado}")
            return resultado
        else:
            print("No se encontró ningún registro con los datos proporcionados.")
            return None

    except mysql.connector.Error as e:
        print("Error al buscar datos en la tabla 'asignacion_facilitador_curso':", e)
        return None

def buscar_inscripcion_periodo_por_nombre(self, nombre):
    try:
        # Consulta SQL para buscar una inscripción por nombre en la tabla "inscripcion_periodo"
        sql_select = "SELECT * FROM inscripcion_periodo WHERE nombre = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (nombre,))
            resultado = conexion.micursor.fetchone()  # Obtener un solo resultado
            if resultado:
                return resultado  # Devuelve el registro encontrado
            else:
                print(f"No se encontró ninguna inscripción con el nombre {nombre}")
                return None
    except mysql.connector.Error as e:
        print(f"Error al buscar la inscripción con el nombre {nombre}: {e}")
        return None

def buscar_preesleccion_curso_por_cedula(self, cedula):
    try:
        # Consulta SQL para buscar un registro por cédula y devolver solo los campos deseados
        sql_select = """
            SELECT 
                cedula_participante, 
                id_preseleccion_periodo, 
                codigo_pensum 
            FROM 
                preseleccion_curso 
            WHERE 
                cedula_participante = %s
        """
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (cedula,))
            resultado = conexion.micursor.fetchone()  # Obtener un solo resultado
            if resultado:
                return resultado  # Devuelve solo los registros encontrados
            else:
                print(f"No se encontró ninguna preselección con la cédula {cedula}")
                return None
    except mysql.connector.Error as e:
        print(f"Error al buscar la preselección con la cédula {cedula}: {e}")
        return None

def buscar_inscripcion_por_cedula(self, cedula_busqueda, periodo_busqueda=None):
    try:
        # Consulta SQL ajustada para permitir búsqueda por cédula o por cédula y período
        sql_select = """
SELECT DISTINCT
    i.cedula_participante AS Cedula_Participante, 
    p.nombre AS Nombre_Participante, 
    p.apellido AS Apellido_Participante,
    afc.id AS Id_Asig_Fac_Curso, 
    f.cedula AS Cedula_Facilitador, 
    f.nombre AS Nombre_Facilitador, 
    f.apellido AS Apellido_Facilitador,
    h.hora_inicial AS Hora_Inicial,
    h.hora_final AS Hora_Final,
    a.ambiente AS Ambiente,
    a.dia AS Dia,
    a.seccion AS Seccion,
    c.codigo AS Codigo_Pensum,
    c.curso AS Curso,
    c.ciclo AS Ciclo,
    ip.nombre AS Nombre_Periodo_Inscripcion,
    rpp.total_cursos AS Total_Cursos,
    rpp.total_creditos AS Total_Creditos,
    i.validada AS Validada
FROM 
    inscripcion i
JOIN 
    participante p ON i.cedula_participante = p.cedula
JOIN 
    asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
JOIN 
    facilitador f ON afc.cedula_facilitador = f.cedula
JOIN 
    asignacion_hr_amb ah ON afc.id_asignacion_hr_amb = ah.id
JOIN 
    horas h ON ah.id_hora = h.id
JOIN 
    ambiente a ON ah.id_ambiente = a.id
JOIN 
    pensum c ON afc.codigo_pensum = c.codigo
JOIN 
    inscripcion_periodo ip ON i.nombre_inscripcion_periodo = ip.nombre
LEFT JOIN (
    SELECT 
        cedula_participante, 
        nombre_inscripcion_periodo, 
        MAX(total_cursos) AS total_cursos, 
        MAX(total_creditos) AS total_creditos
    FROM 
        resumen_participante_periodo
    GROUP BY 
        cedula_participante, 
        nombre_inscripcion_periodo
) rpp ON i.cedula_participante = rpp.cedula_participante 
   AND i.nombre_inscripcion_periodo = rpp.nombre_inscripcion_periodo
WHERE 
    p.cedula = %s
    """ 
        
        # Si el periodo_busqueda es proporcionado, añadimos la condición en la consulta
        if periodo_busqueda:
            sql_select += " AND i.nombre_inscripcion_periodo = %s"
        sql_select += " ORDER BY i.nombre_inscripcion_periodo;"

        with ConexConexion() as conexion:
            # Ejecutar la consulta dependiendo si el período fue proporcionado o no
            if periodo_busqueda:
                conexion.micursor.execute(sql_select, (cedula_busqueda, periodo_busqueda))
            else:
                conexion.micursor.execute(sql_select, (cedula_busqueda,))
            
            registros = conexion.micursor.fetchall()  # Obtener todos los registros

            print("Registros recuperados:", registros)  # Imprimir los registros recuperados
            
            # Limpiar Treeview antes de insertar los registros
            for row in self.treeview_inscripcion.get_children():
                self.treeview_inscripcion.delete(row)

            # Insertar los registros en el Treeview
            for registro in registros:
                self.treeview_inscripcion.insert("", "end", values=registro)

            print(f"Número de registros recuperados: {len(registros)}")
            if len(registros) == 0:
                print("No se encontraron registros para la cédula proporcionada.")

    except mysql.connector.Error as e:
        print("Error al buscar inscripciones:", e)


def buscar_facilitador_por_cedula(main_app_instance, cedula):
    try:
        sql_select = "SELECT cedula, nombre, apellido, horas_de_clase FROM facilitador WHERE cedula = %s"
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_select, (cedula,))
            registros = conexion.micursor.fetchall()
        
        # Limpiar el Treeview
        for row in main_app_instance.treeview_facilitador.get_children():
            main_app_instance.treeview_facilitador.delete(row)

        # Insertar los registros en el Treeview
        if registros:
            for registro in registros:
                main_app_instance.treeview_facilitador.insert("", "end", values=registro)
            print("Registros mostrados en el Treeview.")
        else:
            print("No se encontraron registros.")
        
        return True  # Indica que la búsqueda fue exitosa

    except mysql.connector.Error as e:
        print("Error al mostrar registros en el Treeview:", e)
        return False  # Indica que hubo un error durante la búsqueda



                #COMBOBOX
# Función para cargar datos en el Combobox
def cargar_datos_combobox_horas(combobox):
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT id, CONCAT(hora_inicial, ' - ', hora_final) AS hora FROM horas")
        datos = conn.micursor.fetchall()
    
    combobox['values'] = [f"{fila[0]} - {fila[1]}" for fila in datos]

# Función para actualizar los campos asociados
def actualizar_campos_horas(event, combobox, hora_i_entry, hora_f_entry):
    id_seleccionado = combobox.get().split(" - ")[0]  # Obtener solo el ID
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT hora_inicial, hora_final FROM horas WHERE id = %s", (id_seleccionado,))
        datos = conn.micursor.fetchone()
    
    if datos:
        hora_i_entry.delete(0, 'end')
        hora_f_entry.delete(0, 'end')
        hora_i_entry.insert(0, datos[0])
        hora_f_entry.insert(0, datos[1])

# Función para cargar datos en el Combobox
def cargar_datos_combobox_amb(combobox):
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT id, ambiente FROM ambiente")
        datos = conn.micursor.fetchall()
    
    combobox['values'] = [f"{fila[0]} - {fila[1]}" for fila in datos]

# Función para actualizar los campos asociados
def actualizar_campos_amb(event, combobox, ambiente_entry, seccion_entry, dia_entry):
    id_seleccionado = combobox.get().split(" - ")[0]  # Obtener solo el ID
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT ambiente, seccion, dia FROM ambiente WHERE id = %s", (id_seleccionado,))
        datos = conn.micursor.fetchone()
    
    if datos:
        ambiente_entry.delete(0, 'end')
        seccion_entry.delete(0, 'end')
        dia_entry.delete(0, 'end')
        ambiente_entry.insert(0, datos[0])
        seccion_entry.insert(0, datos[1])
        dia_entry.insert(0, datos[2])

# Función para cargar datos en el Combobox
def cargar_datos_combobox_facilitador(combobox):
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT cedula FROM facilitador")
        datos = conn.micursor.fetchall()
    
    combobox['values'] = [fila[0] for fila in datos]

# Función para actualizar los campos asociados
def actualizar_campos_facilitador(event, combobox, nombres_entry, apellidos_entry, horas_clase_entry):
    cedula_seleccionada = combobox.get()
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT nombre, apellido, horas_de_clase FROM facilitador WHERE cedula = %s", (cedula_seleccionada,))
        datos = conn.micursor.fetchone()
    
    if datos:
        nombres_entry.delete(0, 'end')
        apellidos_entry.delete(0, 'end')
        horas_clase_entry.delete(0, 'end')
        nombres_entry.insert(0, datos[0])
        apellidos_entry.insert(0, datos[1])
        horas_clase_entry.insert(0, datos[2])

# Función para cargar datos en el Combobox
def cargar_datos_combobox_participante(combobox):
    try:
        with ConexConexion() as conn:
            conn.micursor.execute("SELECT cedula FROM participante")
            resultados = conn.micursor.fetchall()
        
        cedulas = [str(fila[0]) for fila in resultados]
        print(cedulas)  # Verifica que las cédulas están siendo recuperadas
        combobox['values'] = cedulas
    except Exception as e:
        print(f"Error al cargar los datos: {e}")



# Función para actualizar los campos asociados
# Función para actualizar los campos asociados
def actualizar_campos_participante(event, combobox, nombres_var, apellidos_var, total_cre_var, total_cursos_var, 
                                   sexo_var, edad_var, telefono_var, correo_var, estado_var, municipio_var, parroquia_var, 
                                   grupo_i_var, programa_var, sistema_var, discapacidadp_var):
    cedula_seleccionada = combobox.get()
    with ConexConexion() as conn:
        conn.micursor.execute("""
            SELECT nombre, apellido, creditos_g, cursos_g, sexo, edad, telefono, correo, estado, municipio, parroquia, 
                   grupo_i, programa, sistema, discapacidad
            FROM participante
            WHERE cedula = %s
        """, (cedula_seleccionada,))
        datos = conn.micursor.fetchone()

    if datos:
        # Asignar los valores recuperados a las variables correspondientes
        nombres_var.set(datos[0])
        apellidos_var.set(datos[1])
        total_cre_var.set(datos[2])
        total_cursos_var.set(datos[3])
        sexo_var.set(datos[4])
        edad_var.set(datos[5])
        telefono_var.set(datos[6])
        correo_var.set(datos[7])
        estado_var.set(datos[8])
        municipio_var.set(datos[9])
        parroquia_var.set(datos[10])
        grupo_i_var.set(datos[11])
        programa_var.set(datos[12])
        sistema_var.set(datos[13])
        discapacidadp_var.set(datos[14])  # Asignar la discapacidad a su variable
    else:
        # Limpiar los campos si no se encuentra el participante
        nombres_var.set("")             
        apellidos_var.set("")
        total_cre_var.set(0)
        total_cursos_var.set(0)
        sexo_var.set("")
        edad_var.set(0)
        telefono_var.set("")
        correo_var.set("")
        estado_var.set("")
        municipio_var.set("")
        parroquia_var.set("")
        grupo_i_var.set("")
        programa_var.set("")
        sistema_var.set("")
        discapacidadp_var.set("")  # Limpiar el campo discapacidad


# Función para actualizar los datos de los Combobox
def cargar_datos_pensum(self):
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT DISTINCT carrera FROM pensum")
        carreras = [row[0] for row in conn.micursor.fetchall()]
        self.carrera_cuadro['values'] = carreras
        
def actualizar_mencion_codigo(self, event):
    carrera_seleccionada = self.carrera_cuadro.get()
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT DISTINCT mencion FROM pensum WHERE carrera = %s", (carrera_seleccionada,))
        menciones = [row[0] for row in conn.micursor.fetchall()]
        self.mencion_cuadro['values'] = menciones
        
        conn.micursor.execute("SELECT DISTINCT codigo FROM pensum WHERE carrera = %s", (carrera_seleccionada,))
        codigos = [row[0] for row in conn.micursor.fetchall()]
        self.codigo_cuadro['values'] = codigos

def actualizar_codigo(self, event):
    mencion_seleccionada = self.mencion_cuadro.get()
    with ConexConexion() as conn:
        conn.micursor.execute("SELECT DISTINCT codigo FROM pensum WHERE mencion = %s", (mencion_seleccionada,))
        codigos = [row[0] for row in conn.micursor.fetchall()]
        self.codigo_cuadro['values'] = codigos


#                                     ACTUALIZAR DATOS

def actualizar_facilitador(self, cedula, nombre, apellido, horas_de_clase):
    try:
        # Actualiza los datos en la tabla "facilitador"
        sql_update = """
            UPDATE facilitador
            SET nombre = %s, apellido = %s, horas_de_clase = %s
            WHERE cedula = %s
        """
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (nombre, apellido, horas_de_clase, cedula))
            conexion.connection.commit()
        print("Datos actualizados en la tabla 'facilitador'.")
        self.mostrar_facilitador_treeview()  # Actualiza el TreeView de facilitadores
        self.limpiar_campos()

        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print("Error al actualizar datos en la tabla 'facilitador':", e)
        return False  # Indica que hubo un error durante la actualización

def actualizar_hora(main_app_instance, id_hora, hora_inicial, hora_final):
    try:
        # Convertir hora_inicial y hora_final a objetos de tiempo si son cadenas
        if isinstance(hora_inicial, str):
            hora_inicial = datetime.strptime(hora_inicial, '%H:%M:%S').time()
        if isinstance(hora_final, str):
            hora_final = datetime.strptime(hora_final, '%H:%M:%S').time()

        # Formatear horas a cadena para la base de datos
        hora_inicial_str = hora_inicial.strftime('%H:%M:%S')
        hora_final_str = hora_final.strftime('%H:%M:%S')

        # Consulta SQL para actualizar la hora
        sql_update = """
            UPDATE horas
            SET hora_inicial = %s, hora_final = %s
            WHERE id = %s
        """

        # Abre la conexión a la base de datos usando la clase ConexConexion
        with ConexConexion() as conexion:
            # Ejecutar la consulta con los parámetros
            conexion.micursor.execute(sql_update, (hora_inicial_str, hora_final_str, id_hora))
            conexion.connection.commit()  # Confirmar los cambios en la base de datos

        print("Hora actualizada correctamente.")
        return True  # Indicar que la actualización fue exitosa

    except mysql.connector.Error as e:
        print(f"Error al actualizar la hora con id {id_hora}: {e}")
        return False  # Indicar que hubo un error durante la actualización

def actualizar_ambiente(main_app_instance, id_ambiente, ambiente, seccion, dia):
    try:
        # Consulta SQL para actualizar los valores en la tabla 'ambiente'
        sql_update = """
            UPDATE ambiente
            SET ambiente = %s, seccion = %s, dia = %s
            WHERE id = %s
        """

        # Abre la conexión a la base de datos usando la clase ConexConexion
        with ConexConexion() as conexion:
            # Ejecutar la consulta con los parámetros
            conexion.micursor.execute(sql_update, (ambiente, seccion, dia, id_ambiente))
            conexion.connection.commit()  # Confirmar los cambios en la base de datos

        print("Ambiente actualizado correctamente.")

        # Actualizar el TreeView y limpiar los campos después de la actualización
        main_app_instance.mostrar_ambiente_en_treeview()
        main_app_instance.limpiar_campos()

        return True  # Indicar que la actualización fue exitosa

    except mysql.connector.Error as e:
        print(f"Error al actualizar el ambiente con id {id_ambiente}: {e}")
        return False  # Indicar que hubo un error durante la actualización

def actualizar_pensum(self, codigo, curso, credito, ciclo, cupos, carrera, mencion):
    try:
        # Consulta SQL para actualizar datos en la tabla "pensum"
        sql_update = """
        UPDATE pensum
        SET curso = %s, credito = %s, ciclo = %s, cupos = %s, carrera = %s, mencion = %s
        WHERE codigo = %s
        """
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (curso, credito, ciclo, cupos, carrera, mencion, codigo))
            conexion.connection.commit()
        
        print("Datos actualizados en la tabla 'pensum'.")
        self.mostrar_pensum_en_treeview()
        self.limpiar_campos()
        
        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print("Error al actualizar datos en la tabla 'pensum':", e)
        return False  # Indica que hubo un error durante la actualización

def actualizar_asignacion_hr_amb(self, id, id_hora, id_ambiente):
    try:
        # Consulta SQL para actualizar los datos en la tabla asignacion_hr_amb
        sql_update = "UPDATE asignacion_hr_amb SET id_hora = %s, id_ambiente = %s WHERE id = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (id_hora, id_ambiente, id))
            conexion.connection.commit()
        print(f"Datos actualizados en la tabla 'asignacion_hr_amb' para ID {id}.")
        
        self.mostrar_asignacion_hr_amb_en_treeview()  # Refresca el TreeView
        self.limpiar_campos()  # Limpia los campos después de actualizar

        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print(f"Error al actualizar datos en la tabla 'asignacion_hr_amb': {e}")
        return False  # Indica que hubo un error durante la actualización

def actualizar_participante(self, cedula, nombre, apellido, sexo, edad, telefono, correo, estado, municipio, parroquia, discapacidad, grupo_i, programa, sistema):
    try:
        # Actualiza los datos en la tabla "participante"
        sql_update = """
        UPDATE PARTICIPANTE 
        SET nombre = %s, apellido = %s, sexo = %s, edad = %s, telefono = %s, 
            correo = %s, estado = %s, municipio = %s, parroquia = %s, 
            discapacidad = %s, grupo_i = %s, programa = %s, sistema = %s 
        WHERE cedula = %s
        """
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (nombre, apellido, sexo, edad, telefono, 
                                                    correo, estado, municipio, parroquia, 
                                                    discapacidad, grupo_i, programa, sistema, cedula))
            conexion.connection.commit()
        print("Datos actualizados en la tabla 'participante'.")
        self.mostrar_participante_treeview()  # Actualizar Treeview después de la actualización
        self.limpiar_campos()

        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print("Error al actualizar datos en la tabla 'participante':", e)
        return False  # Indica que hubo un error durante la actualización

def actualizar_fechas_inscripcion_periodo(self, nombre, nueva_fecha_inicio, nueva_fecha_fin):
    try:
        # Consulta SQL para actualizar las fechas
        sql_update = "UPDATE inscripcion_periodo SET fecha_inicio = %s, fecha_fin = %s WHERE nombre = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (nueva_fecha_inicio, nueva_fecha_fin, nombre))
            conexion.connection.commit()
            print("Fechas actualizadas correctamente.")
            self.mostrar_periodo_academico_treeview()  # Actualizar Treeview de inscripciones
            self.limpiar_campos()

            return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print(f"Error al actualizar las fechas de la inscripción {nombre}: {e}")
        return False  # Indica que hubo un error durante la actualización

def actualizar_preseleccion(self, cedula_participante, id_preseleccion_periodo, codigo_pensum):
    try:
        # Actualiza los datos en la tabla "preseleccion_curso"
        sql_update = """
        UPDATE preseleccion_curso 
        SET id_preseleccion_periodo = %s, codigo_pensum = %s 
        WHERE cedula_participante = %s
        """
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_update, (id_preseleccion_periodo, codigo_pensum, cedula_participante))
            # Confirma la transacción
            conexion.connection.commit()
        
        print("Datos actualizados en la tabla 'preseleccion_curso'.")
        self.mostrar_preseleccion_treeview()  # Actualizar Treeview de preseleccion
        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as e:
        print("Error al actualizar datos en la tabla 'preseleccion_curso':", e)
        return False  # Indica que hubo un error durante la actualización



#                              ELIMINAR DATOS


def eliminar_facilitador(self, cedula):
    try:
        # Mensaje de advertencia para confirmar la eliminación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este facilitador?")
        if not confirmacion:
            print("Eliminación cancelada.")
            return False

        # Elimina datos de la tabla "facilitador"
        sql_delete = "DELETE FROM facilitador WHERE cedula = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (cedula,))
            conexion.connection.commit()
        
        print("Datos eliminados de la tabla 'facilitador'.")
        
        # Actualiza el TreeView de facilitadores
        self.mostrar_facilitador_treeview()  
        
        # Actualiza el Combobox de facilitadores
        cargar_datos_combobox_facilitador(self.cedulaf_cuadro)  # Asegúrate de que este método esté definido correctamente
        
        # Limpia los campos
        self.limpiar_campos()
        
        return True  # Indica que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar datos en la tabla 'facilitador':", e)
        return False  # Indica que hubo un error durante la eliminación

def eliminar_hora(self, id_hora):
    try:
        # Mensaje de advertencia para confirmar la eliminación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar esta hora?")
        if not confirmacion:
            print("Eliminación cancelada.")
            return False

        # Consulta para eliminar un registro de la tabla "horas"
        sql_delete = """ 
        DELETE FROM horas WHERE id = %s;
        """
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (id_hora,))
            conexion.connection.commit()  # Asegúrate de confirmar los cambios
            print(f"Registro con ID {id_hora} eliminado.")
        
        # Vaciar los Entry
        self.limpiar_campos()
        
        # Limpiar el Treeview y mostrar los datos actualizados
        self.mostrar_inscripcion_treeview()
        
        return True  # Indicar que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar el registro:", e)
        return False  # Indicar que hubo un error durante la eliminación


def eliminar_ambiente(main_app_instance, id_ambiente):
    try:
        # Mensaje de advertencia para confirmar la eliminación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este ambiente?")
        if not confirmacion:
            print("Eliminación cancelada.")
            return False

        # Consulta SQL para eliminar el registro de la tabla 'ambiente'
        sql_delete = """
            DELETE FROM ambiente
            WHERE id = %s
        """

        # Abre la conexión a la base de datos usando la clase ConexConexion
        with ConexConexion() as conexion:
            # Ejecutar la consulta con los parámetros
            conexion.micursor.execute(sql_delete, (id_ambiente,))
            conexion.connection.commit()  # Confirmar los cambios en la base de datos

        print(f"Ambiente con ID {id_ambiente} eliminado correctamente.")

        # Actualizar el TreeView y limpiar los campos después de la eliminación
        main_app_instance.mostrar_ambiente_en_treeview()
        main_app_instance.limpiar_campos()

        return True  # Indicar que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print(f"Error al eliminar el ambiente con id {id_ambiente}: {e}")
        return False  # Indicar que hubo un error durante la eliminación


def eliminar_pensum(self, codigo):
    try:
        # Mensaje de advertencia para confirmar la eliminación
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este registro?")
        if not confirmacion:
            print("Eliminación cancelada.")
            return False
        
        # Consulta SQL para eliminar un registro en la tabla "pensum"
        sql_delete = "DELETE FROM pensum WHERE codigo = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (codigo,))
            conexion.connection.commit()

        print("Registro eliminado de la tabla 'pensum'.")
        self.mostrar_pensum_en_treeview()
        self.limpiar_campos()
        
        return True  # Indica que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar datos de la tabla 'pensum':", e)
        return False  # Indica que hubo un error durante la eliminación

def eliminar_asignacion_facilitador_horario(self, id=None, cedula_facilitador=None, id_asignacion_hr_amb=None):
    try:
        # Confirmar la eliminación con un mensaje de advertencia
        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este registro?")
        if not confirmacion:
            print("Eliminación cancelada.")
            return False

        if id:
            # Eliminar por ID
            sql_delete = "DELETE FROM asignacion_facilitador_curso WHERE id = %s"
            parametros = (id,)
        elif cedula_facilitador:
            # Eliminar por cédula del facilitador
            sql_delete = "DELETE FROM asignacion_facilitador_curso WHERE cedula_facilitador = %s"
            parametros = (cedula_facilitador,)
        elif id_asignacion_hr_amb:
            # Eliminar por id_asignacion_hr_amb
            sql_delete = "DELETE FROM asignacion_facilitador_curso WHERE id_asignacion_hr_amb = %s"
            parametros = (id_asignacion_hr_amb,)
        else:
            print("No se proporcionó un criterio de eliminación válido.")
            return None
        
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, parametros)
            conexion.connection.commit()  # Confirmar la eliminación

            # Comprobar el número de filas afectadas
            if conexion.micursor.rowcount > 0:
                print("Registro eliminado exitosamente.")
                
                # Llamar a la función para limpiar campos
                self.limpiar_campos()
                
                # Llamar a la función para mostrar la tabla actualizada
                self.mostrar_asig_faci_hora_treeview()
                self.mostrar_facilitador_treeview()
                
        


                return True
            else:
                print("No se encontró ningún registro con los datos proporcionados.")
                return False

    except mysql.connector.Error as e:
        print("Error al eliminar datos en la tabla 'asignacion_facilitador_curso':", e)
        return False

def eliminar_asignacion_hr_amb_por_id(self, id):
    try:
        # Elimina datos de la tabla "asignacion_hr_amb" donde el id coincida
        sql_delete = "DELETE FROM asignacion_hr_amb WHERE id = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (id,))
            conexion.connection.commit()  # Confirma los cambios

        print(f"Registro con id {id} eliminado de la tabla 'asignacion_hr_amb'.")
        
        # Aquí llamas a la función que actualiza el TreeView
        self.mostrar_asignacion_hr_amb_en_treeview()

        return True  # Indica que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar datos en la tabla 'asignacion_hr_amb':", e)
        return False  # Indica que hubo un error durante la eliminación

def eliminar_participante(self, cedula):
    try:
        # Consulta SQL para eliminar un registro de la tabla "participante"
        sql_delete = "DELETE FROM participante WHERE cedula = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (cedula,))
            conexion.connection.commit()
        print(f"Participante con cédula {cedula} eliminado.")
        self.mostrar_participante_treeview()  # Actualizar Treeview después de la inserción
        self.limpiar_campos()

        cargar_datos_combobox_participante(self.cedulap_cuadro)

        return True  # Indica que la eliminación fue exitosa
    except mysql.connector.Error as e:
        print(f"Error al eliminar el participante con cédula {cedula}: {e}")
        return False  # Indica que hubo un error durante la eliminación

def eliminar_inscripcion_periodo(self, nombre):
    try:
        # Consulta SQL para eliminar un registro
        sql_delete = "DELETE FROM inscripcion_periodo WHERE nombre = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (nombre,))
            conexion.connection.commit()
            if conexion.micursor.rowcount > 0:
                print("Registro eliminado correctamente.")
                self.mostrar_periodo_academico_treeview()  # Actualizar Treeview de inscripciones
                self.limpiar_campos()

                return True  # Indica que la eliminación fue exitosa
            else:
                print("No se encontró ningún registro para eliminar.")
                return False  # Indica que no se encontró el registro

    except mysql.connector.Error as e:
        print(f"Error al eliminar la inscripción con el nombre {nombre}: {e}")
        return False  # Indica que hubo un error durante la eliminación

def eliminar_preseleccion(self, cedula_participante):
    try:
        # Elimina el registro de la tabla "preseleccion_curso" basado en la cédula
        sql_delete = "DELETE FROM preseleccion_curso WHERE cedula_participante = %s"
        with ConexConexion() as conexion:
            conexion.micursor.execute(sql_delete, (cedula_participante,))
            # Confirma la transacción
            conexion.connection.commit()
        
        print("Registro eliminado de la tabla 'preseleccion_curso'.")
        self.mostrar_preseleccion_treeview()  # Actualiza el Treeview después de la eliminación
        return True  # Indica que la eliminación fue exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar el registro en la tabla 'preseleccion_curso':", e)
        return False  # Indica que hubo un error durante la eliminación

def eliminar_inscripcion(self, cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo):
    try:
        with ConexConexion() as conexion:
            # Verificar si el registro existe antes de eliminarlo
            sql_check = "SELECT COUNT(*) FROM inscripcion WHERE cedula_participante = %s AND id_asignacion_facilitador_curso = %s AND nombre_inscripcion_periodo = %s"
            conexion.micursor.execute(sql_check, (cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo))
            count = conexion.micursor.fetchone()[0]

            if count == 0:
                print("No se encontró el registro para eliminar.")
                return False  # Registro no existe

            # Eliminar el registro de la tabla 'inscripcion'
            sql_delete = "DELETE FROM inscripcion WHERE cedula_participante = %s AND id_asignacion_facilitador_curso = %s AND nombre_inscripcion_periodo = %s"
            conexion.micursor.execute(sql_delete, (cedula_participante, id_asignacion_facilitador_curso, nombre_inscripcion_periodo))

            # Confirmar la transacción
            conexion.connection.commit()

        print("Registro eliminado de la tabla 'Inscripcion'.")
        
        # Actualizar el Treeview y limpiar campos
        self.mostrar_inscripcion_treeview()
        self.limpiar_campos()

        return True  # Eliminación exitosa

    except mysql.connector.Error as e:
        print("Error al eliminar el registro en la tabla 'Inscripcion':", e)
        return False  # Hubo un error al intentar eliminar

