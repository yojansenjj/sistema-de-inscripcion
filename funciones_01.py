import tkinter as tk
from tkinter import ttk
from conexion_db_01 import*

#                    Registrar datos

def llamar_crear_horas(main_app_instance):
    try:
        id = main_app_instance.idh_cuadro_var.get()
        hora_inicial = main_app_instance.hora_i_cuadro_var.get()
        hora_final = main_app_instance.hora_f_cuadro_var.get()

        # Aquí llamas a tu función `crear_horas` que no has proporcionado
        exito = crear_horas(main_app_instance, id, hora_inicial, hora_final)

        if exito:
            messagebox.showinfo("Éxito", "Registro de horas creado con éxito.")
        else:
            messagebox.showerror("Error", "Hubo un error al crear el registro de horas.")
    except Exception as e:
        error_message = f"Hubo un error: {e}"
        print(error_message)  # Imprime el mensaje de error en la consola
        messagebox.showerror("Error", error_message)

def llamar_crear_ambiente(main_app_instance):
    id = main_app_instance.idamb_cuadro_var.get()
    ambiente = main_app_instance.ambiente_cuadro_var.get()
    seccion = main_app_instance.seccion_cuadro_var.get()
    dia= main_app_instance.dia_cuadro_var.get()
        
    exito = crear_ambiente(main_app_instance, id, ambiente,seccion, dia)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de ambiente creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de ambiente.")

def llamar_crear_asignacion_hr_amb(main_app_instance):
    id = main_app_instance.idhramb_cuadro_var.get()
    id_hora = main_app_instance.idhoras_cuadro_var.get()
    id_ambiente = main_app_instance.id_ambiente_cuadro_var.get()
        
    exito = crear_asignacion_hr_amb(main_app_instance, id, id_hora, id_ambiente)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de asignacion_hr_amb creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de asignacion_hr_amb.")

def llamar_crear_facilitador(main_app_instance):
    cedula = main_app_instance.cedulaf_cuadro_var.get()
    nombre = main_app_instance.nombresf_cuadro_var.get()
    apellido = main_app_instance.apellidosf_cuadro_var.get()
    horas_de_clase = main_app_instance.horaclasef_cuadro_var.get()        
        
    exito = crear_facilitador(main_app_instance, cedula, nombre, apellido, horas_de_clase)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de facilitador creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de facilitador.")




def llamar_crear_asignacion_facilitador_horario(main_app_instance):
    id = main_app_instance.id_asigfa_cuadro_var.get()
    ce_facilitador = main_app_instance.ced_asigfaho_cuadro_var.get()        
    id_asignacion_hr_amb = main_app_instance.id_asighramb_asigfaho_cuadro_var.get()
    codigo_pensum= main_app_instance.codigo_asig_cuadro_var.get()
      
    exito = crear_asignacion_facilitador_horario(main_app_instance, id, ce_facilitador, id_asignacion_hr_amb, codigo_pensum)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de asignacion_facilitador_horario creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de asignacion_facilitador_horario.")

def llamar_crear_pensum(main_app_instance):
    codigo = main_app_instance.codigo_cuadro_var.get()
    curso=main_app_instance.curso_cuadro_var.get()
    credito=main_app_instance.creditos_cuadro_var.get()
    ciclo=main_app_instance.ciclo_cuadro_var.get()
    cupos=main_app_instance.cupos_cuadro_var.get()
    carrera=main_app_instance.carrera_cuadro_var.get()
    mencion=main_app_instance.mencion_cuadro_var.get()
    exito = crear_pensum(main_app_instance,codigo, curso, credito, ciclo, cupos, carrera, mencion)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de asignacion_facilitador_horario creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de asignacion_facilitador_horario.")
        
def llamar_crear_participante(main_app_instance):
    cedula = main_app_instance.cedulap_cuadro_var.get()
    nombre = main_app_instance.nombresp_cuadro_var.get()
    apellido = main_app_instance.apellidosp_cuadro_var.get()
    sexo= main_app_instance.sexop_var.get()
    edad= main_app_instance.edadp_var.get()
    telefono= main_app_instance.telefonop_var.get()
    email= main_app_instance.emailp_var.get()
    edo= main_app_instance.edop_var.get()
    municipio= main_app_instance.municipiop_var.get()
    parroquia= main_app_instance.parroquiap_var.get()
    discapacidad= main_app_instance.discapacidadp_var.get()
    grupo= main_app_instance.grupo_in_p_var.get()
    programa= main_app_instance.programap_var.get()
    sistema= main_app_instance.sistemap_var.get()
    exito = crear_participante(main_app_instance,cedula, nombre, apellido, sexo, edad, telefono, 
    email, edo, municipio, parroquia, discapacidad, grupo, programa, sistema)

    if exito:
        messagebox.showinfo("Éxito", "Registro de participante creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de participante.")

def llamar_crear_inscripcion(main_app_instance):
    print("Llamando a crear inscripcion")  # Para depuración
    ced_par_inscri = main_app_instance.ced_par_inscri_cuadro_var.get()
    id_asi_faho_inscri = main_app_instance.id_asi_faho_inscri_cuadro_var.get()
    id_periodo_inscri = main_app_instance.id_periodo_inscri_cuadro_var.get()
        
    exito = crear_inscripcion(main_app_instance, ced_par_inscri, id_asi_faho_inscri, id_periodo_inscri)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de Inscripcion creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de Inscripcion.")


def llamar_crear_periodo_aca(main_app_instance):
    nombre_periodo = main_app_instance.nombre_periodo_cuadro_var.get()
    fechai_periodo= main_app_instance.fechai_periodo_cuadro_var.get()
    fechaf_periodo=main_app_instance.fechaf_periodo_cuadro_var.get()
        
    exito = crear_periodo_aca(main_app_instance, nombre_periodo, fechai_periodo,fechaf_periodo)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de Periodo Academico creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de Periodo Academico.")

def llamar_crear_preseleccion(main_app_instance):
    preseleccion_ced_par = main_app_instance.preseleccion_ced_par_cuadro_var.get()
    preseleccion_id_peri= main_app_instance.preseleccion_id_peri_cuadro_var.get()
    preseleccion_pensum_=main_app_instance.preseleccion_pensum_cuadro_var.get()
        
    exito = crear_preseleccion(main_app_instance, preseleccion_ced_par, preseleccion_id_peri,preseleccion_pensum_)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de Preseleccion creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de Preseleccion.")

def llamar_crear_periodo_preseleccion(main_app_instance):
    pre_fechaf_cuadro = main_app_instance.pre_fechaf_cuadro_var.get()
    pre_fechai_cuadro= main_app_instance.pre_fechai_cuadro_var.get()
        
    exito = crear_periodo_preseleccion(main_app_instance, pre_fechaf_cuadro, pre_fechai_cuadro)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de periodo_preseleccion creado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al crear el registro de periodo_preseleccion.")

# PDF
def llamar_generar_reporte_inscripciones_general():
    try:
        generar_reporte_inscripciones_general()
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte general: {e}")

def llamar_generar_reporte_inscripcion_individual(cedula_p, nombre_p):
    try:
        generar_reporte_inscripcion_individual(cedula_p, nombre_p)
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte individual: {e}")

def llamar_generar_reporte_preseleccion(self):
    try:
        # Obtén los datos antes de llamar a la función de generar el reporte
        datos = obtener_datos_preseleccion()
        nombre_archivo_base = "reporte_preseleccion.pdf"  # Define el nombre del archivo

        # Llama a la función con los argumentos requeridos
        generar_reporte_preseleccion(datos, nombre_archivo_base)
        messagebox.showinfo("Éxito", "Reporte general generado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte general: {e}")

def llamar_generar_reporte_participantes():
    try:
        generar_reporte_participantes()
        messagebox.showinfo("Éxito", "Reporte de participantes generado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el reporte de participantes: {e}")


#                           BUSCAR REGISTROS
def llamar_buscar_ambiente_por_nombre(main_app_instance):
    nombre_ambiente = main_app_instance.ambiente_cuadro_var.get()  # Obtiene el valor del cuadro de búsqueda
    
    exito = buscar_ambiente_por_nombre(main_app_instance, nombre_ambiente)
    
    if exito:
        messagebox.showinfo("Éxito", "Búsqueda de ambiente realizada con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al realizar la búsqueda de ambiente.")

def llamar_buscar_facilitador_por_cedula(main_app_instance):
    cedula = main_app_instance.cedulaf_cuadro_var.get()  # Obtiene el valor del cuadro de búsqueda
    
    exito = buscar_facilitador_por_cedula(main_app_instance, cedula)
    
    if exito:
        messagebox.showinfo("Éxito", "Búsqueda de facilitador realizada con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al realizar la búsqueda de facilitador.")



def llamar_buscar_hora(main_app_instance):
    id_hora = main_app_instance.idh_cuadro_var.get()  # Recupera el ID desde la interfaz

    resultado = buscar_hora(main_app_instance, id_hora)  # Llama a la función de búsqueda

    if resultado:
        id_hora, hora_inicial, hora_final = resultado
        main_app_instance.hora_i_cuadro_var.set(hora_inicial)  # Establece la hora inicial en la interfaz
        main_app_instance.hora_f_cuadro_var.set(hora_final)  # Establece la hora final en la interfaz

        messagebox.showinfo("Éxito", f"Hora encontrada: {hora_inicial} - {hora_final}")
    else:
        messagebox.showerror("Error", f"No se encontró ninguna hora con ID {id_hora}.")

def llamar_buscar_asignacion_hr_amb_por_id(main_app_instance):
    id = main_app_instance.idhramb_cuadro_var.get()  # Obtiene el id del Entry
    
    resultado = buscar_asignacion_hr_amb_por_id(main_app_instance, id)
    
    if resultado:
        # Si se encontró el registro, muestra los datos en los campos correspondientes
        main_app_instance.idhoras_cuadro_var.set(resultado[0])  # Asigna el id_hora
        main_app_instance.id_ambiente_cuadro_var.set(resultado[1])  # Asigna el id_ambiente
        messagebox.showinfo("Éxito", "Registro encontrado.")
    else:
        messagebox.showerror("Error", "No se encontró ningún registro con el id proporcionado.")

def llamar_buscar_pensum_por_codigo(main_app_instance):
    codigo = main_app_instance.codigo_cuadro_var.get()  # Obtener el código desde el Entry
    resultado = buscar_pensum_por_codigo(main_app_instance, codigo)
    
    if resultado:
        # Desplegar la información encontrada (puedes modificar este bloque según tu interfaz)
        main_app_instance.curso_cuadro_var.set(resultado[1])
        main_app_instance.creditos_cuadro_var.set(resultado[2])
        main_app_instance.ciclo_cuadro_var.set(resultado[3])
        main_app_instance.cupos_cuadro_var.set(resultado[4])
        main_app_instance.carrera_cuadro_var.set(resultado[5])
        main_app_instance.mencion_cuadro_var.set(resultado[6])
        messagebox.showinfo("Éxito", "Registro encontrado y mostrado en los campos.")
    else:
        messagebox.showerror("Error", "No se encontró ningún registro con ese código.")

def llamar_buscar_participante_por_cedula(main_app_instance):
    cedula = main_app_instance.cedulap_cuadro_var.get()
    resultado = buscar_participante_por_cedula(main_app_instance, cedula)

    if resultado:
        main_app_instance.cedulap_cuadro_var.set(resultado[0])  # Cédula
        main_app_instance.nombresp_cuadro_var.set(resultado[1])  # Nombre
        main_app_instance.apellidosp_cuadro_var.set(resultado[2])  # Apellido
        main_app_instance.sexop_var.set(resultado[3])  # Sexo
        main_app_instance.edadp_var.set(resultado[4])  # Edad
        main_app_instance.telefonop_var.set(resultado[5])  # Teléfono
        main_app_instance.emailp_var.set(resultado[6])  # Correo
        main_app_instance.edop_var.set(resultado[7])  # Estado
        main_app_instance.municipiop_var.set(resultado[8])  # Municipio
        main_app_instance.parroquiap_var.set(resultado[9])  # Parroquia
        main_app_instance.discapacidadp_var.set(resultado[10])  # Discapacidad
        main_app_instance.grupo_in_p_var.set(resultado[11])  # Grupo I
        main_app_instance.programap_var.set(resultado[12])  # Programa
        main_app_instance.sistemap_var.set(resultado[13])  # Sistema
        main_app_instance.total_cur_par_cuadro_var.set(resultado[14])  # Cursos G
        main_app_instance.total_cre_par_cuadro_var.set(resultado[15])  # Créditos G

        messagebox.showinfo("Éxito", "Registro encontrado y mostrado en los campos.")

        main_app_instance.limpiar_campos()

    else:
        messagebox.showerror("Error", "No se encontró ningún registro con esa cédula.")

def llamar_buscar_asignacion_facilitador_horario(main_app_instance):
    id = main_app_instance.id_asigfa_cuadro_var.get()  # Obtener el ID del Entry
    cedula_facilitador = main_app_instance.ced_asigfaho_cuadro_var.get()  # Obtener la cédula del Entry
    id_asignacion_hr_amb = main_app_instance.id_asighramb_asigfaho_cuadro_var.get()  # Obtener id_asignacion_hr_amb del Entry
    
    # Verificamos si alguno de los tres campos tiene un valor
    if id or cedula_facilitador or id_asignacion_hr_amb:
        resultado = buscar_asignacion_facilitador_horario(
            main_app_instance, 
            id=id if id else None, 
            cedula_facilitador=cedula_facilitador if cedula_facilitador else None, 
            id_asignacion_hr_amb=id_asignacion_hr_amb if id_asignacion_hr_amb else None
        )
        
        if resultado:
            # Actualizar los campos con los datos obtenidos
            main_app_instance.id_asigfa_cuadro_var.set(resultado[0])  # id
            main_app_instance.ced_asigfaho_cuadro_var.set(resultado[1])  # cedula_facilitador
            main_app_instance.id_asighramb_asigfaho_cuadro_var.set(resultado[2])  # id_asignacion_hr_amb
            main_app_instance.codigo_asig_cuadro_var.set(resultado[3])  # codigo_pensum
            messagebox.showinfo("Éxito", "Registro encontrado.")
        else:
            messagebox.showwarning("Advertencia", "No se encontró ningún registro con los datos proporcionados.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un ID, cédula de facilitador o ID de asignación de horario.")

def llamar_buscar_inscripcion_periodo_por_nombre(main_app_instance):
    nombre = main_app_instance.nombre_periodo_cuadro_var.get()  # Obtener el nombre desde el Entry
    resultado = buscar_inscripcion_periodo_por_nombre(main_app_instance, nombre)

    if resultado:
        # Desplegar la información encontrada en los campos correspondientes
        main_app_instance.fechai_periodo_cuadro_var.set(resultado[0])  # fecha_inicio
        main_app_instance.fechaf_periodo_cuadro_var.set(resultado[1])  # fecha_fin
        main_app_instance.nombre_periodo_cuadro_var.set(resultado[2])  # nombre

        messagebox.showinfo("Éxito", "Registro encontrado y mostrado en los campos.")
    else:
        messagebox.showerror("Error", "No se encontró ningún registro con ese nombre.")

def llamar_buscar_inscripcion(main_app_instance):
    print("Llamando a buscar inscripcion")  # Para depuración
    ced_busqueda = main_app_instance.ced_par_inscri_cuadro_var.get()  # Suponiendo que tienes un campo para la cédula
    nombre_periodo=main_app_instance.id_periodo_inscri_cuadro_var.get()
    if ced_busqueda:
        buscar_inscripcion_por_cedula(main_app_instance,ced_busqueda, nombre_periodo)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una cédula para buscar.")


#                                  ACTUALIZAR DATOS

def llamar_actualizar_asignacion_hr_amb(main_app_instance):
    # Obtener los valores de los Entry para los campos a actualizar
    id = main_app_instance.idhramb_cuadro_var.get()
    id_hora = main_app_instance.idhoras_cuadro_var.get()
    id_ambiente = main_app_instance.id_ambiente_cuadro_var.get()
    
    # Llamar a la función para actualizar los datos en la tabla asignacion_hr_amb
    exito = actualizar_asignacion_hr_amb(main_app_instance, id, id_hora, id_ambiente)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de asignacion_hr_amb actualizado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar el registro de asignacion_hr_amb.")

def llamar_actualizar_facilitador(main_app_instance):
    cedula = main_app_instance.cedulaf_cuadro_var.get()
    nombre = main_app_instance.nombresf_cuadro_var.get()
    apellido = main_app_instance.apellidosf_cuadro_var.get()
    horas_de_clase = main_app_instance.horaclasef_cuadro_var.get()        
        
    exito = actualizar_facilitador(main_app_instance, cedula, nombre, apellido, horas_de_clase)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de facilitador actualizado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar el registro de facilitador.")

def llamar_actualizar_hora(main_app_instance):
    id_hora = main_app_instance.idh_cuadro_var.get()  # Recupera el ID de la interfaz
    hora_inicial = main_app_instance.hora_i_cuadro_var.get()  # Recupera la hora inicial de la interfaz
    hora_final = main_app_instance.hora_f_cuadro_var.get()  # Recupera la hora final de la interfaz

    # Llama a la función para actualizar la hora
    exito = actualizar_hora(main_app_instance, id_hora, hora_inicial, hora_final)

    if exito:
        messagebox.showinfo("Éxito", f"Hora con ID {id_hora} actualizada correctamente.")
    else:
        messagebox.showerror("Error", f"No se pudo actualizar la hora con ID {id_hora}.")

def llamar_actualizar_ambiente(main_app_instance):
    # Recupera los valores de la interfaz
    id_ambiente = main_app_instance.idamb_cuadro_var.get()
    ambiente = main_app_instance.ambiente_cuadro_var.get()
    seccion = main_app_instance.seccion_cuadro_var.get()
    dia = main_app_instance.dia_cuadro_var.get()

    # Llama a la función para actualizar el ambiente
    exito = actualizar_ambiente(main_app_instance, id_ambiente, ambiente, seccion, dia)

    if exito:
        messagebox.showinfo("Éxito", f"Ambiente con ID {id_ambiente} actualizado correctamente.")
    else:
        messagebox.showerror("Error", f"No se pudo actualizar el ambiente con ID {id_ambiente}.")

def llamar_actualizar_pensum(main_app_instance):
    codigo = main_app_instance.codigo_cuadro_var.get()  # Obtener el código desde el Entry
    curso = main_app_instance.curso_cuadro_var.get()
    credito = main_app_instance.creditos_cuadro_var.get()
    ciclo = main_app_instance.ciclo_cuadro_var.get()
    cupos = main_app_instance.cupos_cuadro_var.get()
    carrera = main_app_instance.carrera_cuadro_var.get()
    mencion = main_app_instance.mencion_cuadro_var.get()
    
    exito = actualizar_pensum(main_app_instance, codigo, curso, credito, ciclo, cupos, carrera, mencion)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro actualizado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar el registro.")

def llamar_actualizar_participante(main_app_instance):
    cedula = main_app_instance.cedulap_cuadro_var.get()  # Asumimos que la cédula es el identificador
    nombre = main_app_instance.nombresp_cuadro_var.get()
    apellido = main_app_instance.apellidosp_cuadro_var.get()
    sexo = main_app_instance.sexop_var.get()
    edad = main_app_instance.edadp_var.get()
    telefono = main_app_instance.telefonop_var.get()
    email = main_app_instance.emailp_var.get()
    edo = main_app_instance.edop_var.get()
    municipio = main_app_instance.municipiop_var.get()
    parroquia = main_app_instance.parroquiap_var.get()
    discapacidad = main_app_instance.discapacidadp_var.get()
    grupo = main_app_instance.grupo_in_p_var.get()
    programa = main_app_instance.programap_var.get()
    sistema = main_app_instance.sistemap_var.get()
    
    exito = actualizar_participante(cedula, nombre, apellido, sexo, edad, telefono, 
                                                      email, edo, municipio, parroquia, discapacidad, 
                                                      grupo, programa, sistema)

    if exito:
        messagebox.showinfo("Éxito", "Registro de participante actualizado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar el registro de participante.")

def llamar_actualizar_fechas_inscripcion_periodo(main_app_instance):
    nombre = main_app_instance.nombre_periodo_cuadro_var.get()  # Obtener el nombre desde el Entry
    nueva_fecha_inicio = main_app_instance.fechai_periodo_cuadro_var.get()  # Obtener la nueva fecha de inicio
    nueva_fecha_fin = main_app_instance.fechaf_periodo_cuadro_var.get()  # Obtener la nueva fecha de fin

    # Validación del rango de fechas
    if nueva_fecha_inicio >= nueva_fecha_fin:
        messagebox.showerror("Error", "La fecha de inicio debe ser anterior a la fecha de fin.")
        return

    exito = actualizar_fechas_inscripcion_periodo(main_app_instance, nombre, nueva_fecha_inicio, nueva_fecha_fin)

    if exito:
        messagebox.showinfo("Éxito", "Fechas actualizadas con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar las fechas.")

def llamar_actualizar_preseleccion(main_app_instance):
    preseleccion_ced_par = main_app_instance.preseleccion_ced_par_cuadro_var.get()
    preseleccion_id_peri = main_app_instance.preseleccion_id_peri_cuadro_var.get()
    preseleccion_pensum_ = main_app_instance.preseleccion_pensum_cuadro_var.get()

    exito = actualizar_preseleccion(main_app_instance, preseleccion_ced_par, preseleccion_id_peri, preseleccion_pensum_)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de Preseleccion actualizado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al actualizar el registro de Preseleccion.")



#                         ELIMINAR DATOS

def llamar_eliminar_facilitador(main_app_instance):
    cedula = main_app_instance.cedulaf_cuadro_var.get()
        
    exito = eliminar_facilitador(main_app_instance, cedula)
    
    if exito:
        messagebox.showinfo("Éxito", "Registro de facilitador eliminado con éxito.")
    else:
        messagebox.showerror("Error", "Hubo un error al eliminar el registro de facilitador.")

def llamar_eliminar_hora(main_app_instance):
    id_hora = main_app_instance.idh_cuadro_var.get()  # Obtener el ID desde la interfaz

    # Llamar a la función para eliminar el registro
    exito = eliminar_hora(main_app_instance, id_hora)

    if exito:
        messagebox.showinfo("Éxito", f"Registro con ID={id_hora} eliminado correctamente.")
    else:
        messagebox.showerror("Error", f"No se pudo eliminar el registro con ID={id_hora}.")

def llamar_eliminar_ambiente(main_app_instance):
    # Recupera el ID del ambiente a eliminar desde la interfaz
    id_ambiente = main_app_instance.idamb_cuadro_var.get()

    # Verificación adicional (opcional) para asegurar que no se eliminen registros sin un ID válido
    if not id_ambiente:
        messagebox.showerror("Error", "Por favor ingresa un ID válido para eliminar.")
        return

    # Confirmar con el usuario antes de proceder con la eliminación
    confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Seguro que deseas eliminar el ambiente con ID {id_ambiente}?")
    
    if confirmacion:
        exito = eliminar_ambiente(main_app_instance, id_ambiente)
        
        if exito:
            messagebox.showinfo("Éxito", f"Ambiente con ID {id_ambiente} eliminado correctamente.")
        else:
            messagebox.showerror("Error", f"No se pudo eliminar el ambiente con ID {id_ambiente}.")

def llamar_eliminar_pensum(main_app_instance):
    codigo = main_app_instance.codigo_cuadro_var.get()  # Obtener el código desde el Entry
    
    if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de eliminar el registro con código {codigo}?"):
        exito = eliminar_pensum(main_app_instance, codigo)
        
        if exito:
            messagebox.showinfo("Éxito", "Registro eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro.")

def llamar_eliminar_asignacion_facilitador_horario(main_app_instance):
    id = main_app_instance.id_asigfa_cuadro_var.get()  # Obtener el ID del Entry
    cedula_facilitador = main_app_instance.ced_asigfaho_cuadro_var.get()  # Obtener la cédula del Entry
    id_asignacion_hr_amb = main_app_instance.id_asighramb_asigfaho_cuadro_var.get()  # Obtener id_asignacion_hr_amb del Entry
    
    # Verificamos si alguno de los tres campos tiene un valor
    if id or cedula_facilitador or id_asignacion_hr_amb:
        if eliminar_asignacion_facilitador_horario(
            main_app_instance, 
            id=id if id else None, 
            cedula_facilitador=cedula_facilitador if cedula_facilitador else None, 
            id_asignacion_hr_amb=id_asignacion_hr_amb if id_asignacion_hr_amb else None
        ):
            messagebox.showinfo("Éxito", "Registro eliminado exitosamente.")
        else:
            messagebox.showwarning("Advertencia", "No se encontró ningún registro para eliminar.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un ID, cédula de facilitador o ID de asignación de horario para eliminar un registro.")

def llamar_eliminar_asignacion_hr_amb_por_id(main_app_instance):
    id = main_app_instance.idhramb_cuadro_var.get()  # Obtiene el id del Entry

    # Pregunta al usuario si realmente desea eliminar el registro
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este registro?")
    
    if confirmacion:
        exito = eliminar_asignacion_hr_amb_por_id(main_app_instance, id)  # Llama a la función de eliminación
        
        if exito:
            messagebox.showinfo("Éxito", "Registro eliminado con éxito.")
            main_app_instance.limpiar_campos()  # Limpia los campos después de la eliminación
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro.")

def llamar_eliminar_participante(main_app_instance):
    cedula = main_app_instance.cedulap_cuadro_var.get()  # Obtener la cédula desde el Entry

    if not cedula:  # Verifica si se ha introducido una cédula
        messagebox.showerror("Error", "Por favor, introduzca una cédula válida.")
        return

    # Mensaje de advertencia
    respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro que desea eliminar el participante con cédula {cedula}? Esta acción no se puede deshacer.")
    
    if respuesta:  # Si el usuario confirma la eliminación
        exito = eliminar_participante(main_app_instance, cedula)
        if exito:
            main_app_instance.mostrar_participante_treeview()  # Actualizar Treeview después de la eliminación
            main_app_instance.limpiar_campos()  # Limpiar los campos
            messagebox.showinfo("Éxito", f"Participante con cédula {cedula} eliminado exitosamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro de participante.")
    else:
        messagebox.showinfo("Cancelado", "La eliminación ha sido cancelada.")

def llamar_eliminar_inscripcion_periodo(main_app_instance):
    nombre = main_app_instance.nombre_periodo_cuadro_var.get()  # Obtener el nombre desde el Entry

    if not nombre:
        messagebox.showerror("Error", "Por favor, ingrese el nombre para eliminar el registro.")
        return

    # Mensaje de confirmación antes de eliminar
    confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro de que desea eliminar la inscripción con el nombre '{nombre}'?")
    if confirmacion:
        exito = eliminar_inscripcion_periodo(main_app_instance, nombre)

        if exito:
            messagebox.showinfo("Éxito", "Registro eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro.")

def llamar_eliminar_preseleccion(main_app_instance):
    preseleccion_ced_par = main_app_instance.preseleccion_ced_par_cuadro_var.get()

    # Confirmación antes de eliminar
    confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar este registro?")
    if confirmacion:
        exito = eliminar_preseleccion(main_app_instance, preseleccion_ced_par)

        if exito:
            messagebox.showinfo("Éxito", "Registro de Preseleccion eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro de Preseleccion.")



def llamar_eliminar_inscripcion(main_app_instance):
    # Obtener los valores de los campos
    ced_par_inscri = main_app_instance.ced_par_inscri_cuadro_var.get()
    id_asi_faho_inscri = main_app_instance.id_asi_faho_inscri_cuadro_var.get()
    id_periodo_inscri = main_app_instance.id_periodo_inscri_cuadro_var.get()
    
    # Mensaje de advertencia para confirmar la eliminación
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar esta inscripción?")
    
    if confirmacion:
        exito = eliminar_inscripcion(main_app_instance,ced_par_inscri, id_asi_faho_inscri, id_periodo_inscri)
        
        if exito:
            messagebox.showinfo("Éxito", "Registro de Inscripción eliminado con éxito.")
        else:
            messagebox.showerror("Error", "Hubo un error al eliminar el registro de Inscripción.")

