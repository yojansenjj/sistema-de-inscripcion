# import os
# print("Current working directory:", os.getcwd())
# print("Files in current directory:", os.listdir(os.getcwd()))

# import tkinter as tk
# import logging
# import mysql.connector  # o cualquier otro módulo que estés usando
# # Otras importaciones
# from conexion_db_01 import*
# # Configuración de logging para obtener más información
# logging.basicConfig(level=logging.DEBUG)

# El resto de tu código...


from tkinter import ttk
from tkinter import *
from tkinter import ttk, Button, messagebox
from funciones_01 import *
from reportes_pdf import*
from tkinter import PhotoImage
from ventana_presentacion import*
from pensum import*
from datetime import timedelta


class Ventana:
    def __init__(self, root):
        


        self.root = root
        self.root.title("SISTEMA ALTERNO PARA LA GESTION DE INSCRIPCION")
        self.root.geometry("1250x680+50+10")
        self.root.configure(bg="Azure")
        self.root.rowconfigure(0, weight=1)  # Expandir fila 0
        self.root.columnconfigure(0, weight=1)  # Expandir columna 0
        style = ttk.Style()
        style.theme_use("default")  # Usa el tema por defecto

        self.ventana_presentacion = VentanaPresentacion(self.root)

        self.conn = ConexConexion()
        self.carrera_cuadro_var= StringVar()
        self.mencion_cuadro_var= StringVar()
        self.codigo_cuadro_var= IntVar() 
        self.curso_cuadro_var= StringVar()
        self.creditos_cuadro_var= IntVar()
        self.ciclo_cuadro_var= StringVar()
        self.cupos_cuadro_var= IntVar()
        self.idh_cuadro_var= IntVar() 
        self.hora_i_cuadro_var= StringVar()
        self.hora_f_cuadro_var= StringVar()
        self.idamb_cuadro_var= StringVar()
        self.dia_cuadro_var= StringVar()
        self.ambiente_cuadro_var= StringVar()
        self.seccion_cuadro_var= StringVar()
        self.idhramb_cuadro_var= IntVar()
        self.idhoras_cuadro_var= IntVar()
        self.id_ambiente_cuadro_var= IntVar()
        self.cedulaf_cuadro_var= StringVar()
        self.nombresf_cuadro_var= StringVar()
        self.apellidosf_cuadro_var= StringVar()
        self.horaclasef_cuadro_var= StringVar()
        self.id_horario_cuadro_var= IntVar()
        self.hi_horario_cuadro_var= StringVar()
        self.hf_horario_cuadro_var= StringVar()
        self.ced_horario_cuadro_var=IntVar()
        self.id_asigfa_cuadro_var= IntVar()
        self.idho_asigfa_cuadro_var= IntVar()
        self.asig_cedulaf_cuadro_var= IntVar()
        self.ced_asigfaho_cuadro_var= IntVar()
        self.idhora_asig_asif_cuadro_var=IntVar()
        self.idfa_asigfaho_cuadro_var= IntVar()
        self.idhora_horario_cuadro_var=IntVar()
        self.id_asighramb_asigfaho_cuadro_var= IntVar()
        self.cedulap_cuadro_var= IntVar()
        self.nombresp_cuadro_var= StringVar()
        self.apellidosp_cuadro_var= StringVar()
        self.total_cre_par_cuadro_var=IntVar()
        self.total_cur_par_cuadro_var=IntVar()
        self.id_asi_faho_inscri_cuadro_var= IntVar()
        self.ced_par_inscri_cuadro_var= IntVar()
        self.id_periodo_inscri_cuadro_var=StringVar()
        self.codigo_asig_cuadro_var=IntVar()
        self.nombre_periodo_cuadro_var=StringVar()
        self.fcedula_cuadro_var=StringVar()
        self.nombre_periodof_cuadro_var=StringVar()
        self.fechai_periodo_cuadro_var=StringVar()
        self.fechaf_periodo_cuadro_var=StringVar()
        self.preseleccion_ced_par_cuadro_var=IntVar()
        self.preseleccion_id_peri_cuadro_var=IntVar()
        self.preseleccion_pensum_cuadro_var=IntVar()
        self.pre_fechaf_cuadro_var=StringVar()
        self.pre_fechai_cuadro_var=StringVar()

        self.sexop_var = StringVar()
        self.edadp_var = IntVar()
        self.telefonop_var = StringVar()
        self.emailp_var = StringVar()
        self.edop_var = StringVar()
        self.municipiop_var = StringVar()
        self.parroquiap_var = StringVar()
        self.discapacidadp_var = StringVar()
        self.grupo_in_p_var = StringVar()
        self.programap_var = StringVar()
        self.sistemap_var= StringVar()



        # Cargar la aplicación principal después de cerrar la ventana de presentación
 
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12))  # Configura el estilo para los botones

        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Arial", 12), rowheight=25)  # Configura la fuente y el tamaño
        self.style.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Configura el encabezado del Treeview

    # Crear un estilo para los frames
        style = ttk.Style()
        style.configure("TFrame", background="Red")
    
        style = ttk.Style()
        style.configure("TLabel", background="royalblue2", foreground="black", font=('Arial', 12))


        style = ttk.Style()
        style.configure("TNotebook.Tab", font=("Arial", 12))
        # #                                   FRAME PINCIPAL DE BOTONES DE NAVEGACION
        self.frame_botones_a = tk.Frame(self.root, width=1250, height=200, bg="black")
        self.frame_botones_a.pack(side=tk.TOP, fill=tk.X)
        self.frame_botones_a.place(x=0, y=0)

        self.frame_central_a = tk.Frame(self.root)
        self.frame_central_a.place(x=0, y=50, relwidth=1, relheight=1)
        self.frame_central_a.rowconfigure(0, weight=1)  # Expandir fila 0
        self.frame_central_a.columnconfigure(0, weight=1)  # Expandir columna 0

#                                   FRAMES PRINCIPALES
        self.frame_horario = tk.Frame(self.frame_central_a)
        self.frame_horario.grid(row=0, column=0, sticky="nsew")

        self.frame_facilitador = tk.Frame(self.frame_central_a, width=1250, height=500)
        self.frame_facilitador.grid(row=0, column=0, sticky="nsew")

        self.frame_participante = tk.Frame(self.frame_central_a,width=1250, height=500,background="royalblue2")
        self.frame_participante.grid(row=0, column=0, sticky="nsew")

        self.frame_asignaciones = tk.Frame(self.frame_central_a, width=1250, height=800)
        self.frame_asignaciones.grid(row=0, column=0, sticky="nsew")
      

        self.frame_pensum = tk.Frame(self.frame_central_a)
        self.frame_pensum.grid(row=0, column=0, sticky="nsew")

        self.frame_inscripcion = tk.Frame(self.frame_central_a, width=1250, height=800)
        self.frame_inscripcion.grid(row=0, column=0, sticky="nsew")
 
#                                BOTONES PARA DESPLAZAR ENTRE FRAME PRINCIPALES
             
# Configuración del tamaño de la fuente
        font_config = ('Arial', 12)  # Nombre de la fuente y tamaño

        # Crear botones con colores personalizados y tamaño de letra
        self.btn_horario = tk.Button(self.frame_botones_a, text="Horarios y Amb", command=self.mostrar_horario, width=15, bg="SteelBlue1", fg="black", font=font_config)
        self.btn_horario.pack(side=tk.LEFT, padx=10)

        self.btn_facilitador = tk.Button(self.frame_botones_a, text="Facilitador", command=self.mostrar_facilitador, width=15, bg="SteelBlue2", fg="black", font=font_config)
        self.btn_facilitador.pack(side=tk.LEFT, padx=10)

        self.btn_participante = tk.Button(self.frame_botones_a, text="Participante", command=self.mostrar_participante, width=15, bg="SteelBlue3", fg="black", font=font_config)
        self.btn_participante.pack(side=tk.LEFT, padx=10)

        self.btn_asignaciones = tk.Button(self.frame_botones_a, text="Asignaciones", command=self.mostrar_asignaciones, width=15, bg="SteelBlue4", fg="black", font=font_config)
        self.btn_asignaciones.pack(side=tk.LEFT, padx=10)

        self.btn_pensum = tk.Button(self.frame_botones_a, text="Pensum", command=self.mostrar_pensum, width=15, bg="SkyBlue1", fg="black", font=font_config)
        self.btn_pensum.pack(side=tk.LEFT, padx=10)

        self.btn_inscripcion = tk.Button(self.frame_botones_a, text="Inscripciones", command=self.mostrar_inscripcion, width=15, bg="SkyBlue2", fg="black", font=font_config)
        self.btn_inscripcion.pack(side=tk.LEFT, padx=10)

       

#                               PENSUM
        
#                                    Frame para contener los Label y Entry
       
        self.notebook_pensum = ttk.Notebook(self.frame_pensum,)
        self.notebook_pensum.pack(fill=tk.BOTH, expand=True)
        # Pestaña 1
        self.tab_pensum = ttk.Frame(self.notebook_pensum)
        self.notebook_pensum.add(self.tab_pensum, text="Pensum")
        self.label_entry_frame_pensum = ttk.Frame(self.tab_pensum)
        self.label_entry_frame_pensum.grid(row=0, column=0, padx=15, pady=15)

        self.pensum_label_entry_frame = ttk.Frame(self.label_entry_frame_pensum)
        self.pensum_label_entry_frame.grid(row=8, column=0, padx=15, pady=15, sticky="nsew")

        self.carrera_label=ttk.Label(self.pensum_label_entry_frame, text="Carrera")
        self.carrera_label.grid(row=0, column=0, padx=15, pady=15,ipady=5)
        self.carrera_label.config(font="Arial 10")
        self.carrera_cuadro = ttk.Combobox(self.pensum_label_entry_frame, textvariable=self.carrera_cuadro_var,values=["Administarcion", "Educacion"])
        self.carrera_cuadro.grid(row=0, column=1, padx=15, pady=15,ipady=5)
        self.carrera_cuadro.config(font="Arial 10")
        self.carrera_cuadro.bind("<<ComboboxSelected>>", self.carrera_cuadro_var)



        self.mencion_label=ttk.Label(self.pensum_label_entry_frame, text="Mencion")
        self.mencion_label.grid(row=0, column=2, padx=15, pady=15,ipady=5)
        self.mencion_label.config(font="Arial 10")
        self.mencion_cuadro = ttk.Combobox(self.pensum_label_entry_frame, textvariable=self.mencion_cuadro_var)
        self.mencion_cuadro.grid(row=0, column=3, padx=15, pady=15,ipady=5)
        self.mencion_cuadro.config(font="Arial 10")
        self.mencion_cuadro.bind("<<ComboboxSelected>>", self.actualizar_codigos)

        menciones = list(mencion_dict.keys())
        self.mencion_cuadro['values'] = menciones



        self.codigo_label=ttk.Label(self.pensum_label_entry_frame, text="Codigo")
        self.codigo_label.grid(row=0, column=4, padx=15, pady=15,ipady=5)
        self.codigo_label.config(font="Arial 10")
        self.codigo_cuadro = ttk.Combobox(self.pensum_label_entry_frame, textvariable=self.codigo_cuadro_var)
        self.codigo_cuadro.grid(row=0, column=5, padx=15, pady=15,ipady=5)
        self.codigo_cuadro.config(font="Arial 10")

        self.codigo_cuadro['values'] = list(administracion.keys())
        self.codigo_cuadro.bind("<<ComboboxSelected>>", self.mostrar_curso)
       

        self.curso_label=ttk.Label(self.pensum_label_entry_frame, text="Curso")
        self.curso_label.grid(row=0, column=6, padx=15, pady=15,ipady=5)
        self.curso_label.config(font="Arial 10")
        self.curso_cuadro = ttk.Entry(self.pensum_label_entry_frame, textvariable=self. curso_cuadro_var)
        self.curso_cuadro.grid(row=0, column=7, padx=15, pady=15,ipady=5)
        self.curso_cuadro.config(font="Arial 10")

        self.creditos_label=ttk.Label(self.pensum_label_entry_frame, text="Creditos")
        self.creditos_label.grid(row=1, column=0, padx=15, pady=15,ipady=5)
        self.creditos_label.config(font="Arial 10")
        self.creditos_cuadro = ttk.Entry(self.pensum_label_entry_frame, textvariable=self.creditos_cuadro_var)
        self.creditos_cuadro.grid(row=1, column=1, padx=15, pady=15,ipady=5)
        self.creditos_cuadro.config(font="Arial 10")

        self.ciclo_label=ttk.Label(self.pensum_label_entry_frame, text="Ciclo")
        self.ciclo_label.grid(row=1, column=2, padx=15, pady=15,ipady=5)
        self.ciclo_label.config(font="Arial 10")
        self.ciclo_cuadro = ttk.Entry(self.pensum_label_entry_frame, textvariable=self.ciclo_cuadro_var)
        self.ciclo_cuadro.grid(row=1, column=3, padx=15, pady=15,ipady=5)
        self.ciclo_cuadro.config(font="Arial 10")



        #                            PRESELECCION

        self.tab_pre = ttk.Frame(self.notebook_pensum)
        self.notebook_pensum.add(self.tab_pre, text="Preseleccion")
        self.label_entry_frame_pre = ttk.Frame(self.tab_pre)
        self.label_entry_frame_pre.grid(row=1, column=0, padx=15, pady=15)

        self.pre_label_entry_frame = ttk.Frame(self.label_entry_frame_pre)
        self.pre_label_entry_frame.grid(row=8, column=0, padx=15, pady=15, sticky="nsew")

        self.preseleccion_id_par_label=ttk.Label(self.pre_label_entry_frame, text="Cedula")
        self.preseleccion_id_par_label.grid(row=0, column=0, padx=15, pady=15)
        self.preseleccion_id_par_label.config(font="Arial 10")
        self.preseleccion_id_par_cuadro = ttk.Entry(self.pre_label_entry_frame, textvariable=self.preseleccion_ced_par_cuadro_var)
        self.preseleccion_id_par_cuadro.grid(row=0, column=1, padx=15, pady=15)
        self.preseleccion_id_par_cuadro.config(font="Arial 10")

        self.preseleccion_id_peri_label=ttk.Label(self.pre_label_entry_frame, text="Id Periodo")
        self.preseleccion_id_peri_label.grid(row=0, column=2, padx=15, pady=15)
        self.preseleccion_id_peri_label.config(font="Arial 10")
        self.preseleccion_id_peri_cuadro = ttk.Entry(self.pre_label_entry_frame, textvariable=self.preseleccion_id_peri_cuadro_var)
        self.preseleccion_id_peri_cuadro.grid(row=0, column=3, padx=15, pady=15)
        self.preseleccion_id_peri_cuadro.config(font="Arial 10")

        self.preseleccion_pensum_label=ttk.Label(self.pre_label_entry_frame, text="Codigo Pensum")
        self.preseleccion_pensum_label.grid(row=0, column=4, padx=15, pady=15)
        self.preseleccion_pensum_label.config(font="Arial 10")
        self.preseleccion_pensum_cuadro = ttk.Entry(self.pre_label_entry_frame, textvariable=self.preseleccion_pensum_cuadro_var)
        self.preseleccion_pensum_cuadro.grid(row=0, column=5, padx=15, pady=15)
        self.preseleccion_pensum_cuadro.config(font="Arial 10")
    
        
        #                               PERIDO DE PRESELECCION
        self.tab_periodo_pre = ttk.Frame(self.notebook_pensum)
        self.notebook_pensum.add(self.tab_periodo_pre, text="Perido de Preseleccion")
        self.label_entry_frame_perido_pre = ttk.Frame(self.tab_periodo_pre)
        self.label_entry_frame_perido_pre.grid(row=1, column=0, padx=15, pady=15)

        self.pre_fechai_label=ttk.Label(self.label_entry_frame_perido_pre, text="Fecha Final")
        self.pre_fechai_label.grid(row=0, column=2, padx=15, pady=15)
        self.pre_fechai_label.config(font="Arial 10")
        self.pre_fechai_cuadro = ttk.Entry(self.label_entry_frame_perido_pre, textvariable=self.pre_fechai_cuadro_var)
        self.pre_fechai_cuadro.grid(row=0, column=3, padx=15, pady=15)
        self.pre_fechai_cuadro.config(font="Arial 10")

        self.pre_fechaf_label=ttk.Label(self.label_entry_frame_perido_pre, text="Fecha Inicio")
        self.pre_fechaf_label.grid(row=0, column=0, padx=15, pady=15)
        self.pre_fechaf_label.config(font="Arial 10")
        self.pre_fechaf_cuadro = ttk.Entry(self.label_entry_frame_perido_pre, textvariable=self.pre_fechaf_cuadro_var)
        self.pre_fechaf_cuadro.grid(row=0, column=1, padx=15, pady=15)
        self.pre_fechaf_cuadro.config(font="Arial 10")


        #                              HORARIO
        self.notebook = ttk.Notebook(self.frame_horario)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        # Pestaña 1
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Horas")
        self.label_entry_frame_1 = ttk.Frame(self.tab1)
        self.label_entry_frame_1.grid(row=0, column=0, padx=15, pady=15)  
        
        # Pestaña 2
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Ambiente")
        self.label_entry_frame_2 = ttk.Frame(self.tab2)
        self.label_entry_frame_2.grid(row=0, column=0, padx=15, pady=15)
        #Pestaña 3
        self.notebook_asig = ttk.Notebook(self.frame_asignaciones)
        self.notebook_asig.pack(fill=tk.BOTH, expand=True)
        
        self.tab3 = ttk.Frame(self.notebook_asig)
        self.tab3.rowconfigure(0, weight=0)
        self.tab3.columnconfigure(0, weight=1)
        self.notebook_asig.add(self.tab3, text="Asignacion horas ambiente")
        
    

        #Contenedores de horas y ambiente
        self.frame_ambiente = ttk.Label(self.label_entry_frame_2)
        self.frame_ambiente.grid(row=2, column=0, padx=15, pady=15, sticky="nsew")
        
        self.frame_asig_hr_amb = ttk.Frame(self.tab3)
        self.frame_asig_hr_amb.grid(row=8, column=0, padx=15, pady=15)

        # Elevar el ttk.Label del título a la capa superior

        #Pestaña horas
        self.frame_asig_hr=ttk.Frame(self.tab1)
        self.frame_asig_hr.grid(row=5, column=3)
        self.idh_label=ttk.Label(self.frame_asig_hr, text="Id")
        self.idh_label.grid(row=0, column=0, padx=5, pady=5)
        self.idh_label.config(font="Arial 10")
        self.idh_cuadro = ttk.Combobox(self.frame_asig_hr, textvariable=self.idh_cuadro_var)
        self.idh_cuadro.grid(row=0, column=1, padx=5, pady=5)
        self.idh_cuadro.config(font="Arial 10")
        self.idh_cuadro.bind("<<ComboboxSelected>>", lambda event: actualizar_campos_horas(event, self.idh_cuadro, self.hora_i_cuadro, self.hora_f_cuadro))
        cargar_datos_combobox_horas(self.idh_cuadro)


        self.hora_i_label=ttk.Label(self.frame_asig_hr, text="Hora Inicial")
        self.hora_i_label.grid(row=0, column=2, padx=5, pady=5)
        self.hora_i_label.config(font="Arial 10")
        self.hora_i_cuadro = ttk.Entry(self.frame_asig_hr, textvariable=self.hora_i_cuadro_var)
        self.hora_i_cuadro.grid(row=0, column=3, padx=5, pady=5)
        self.hora_i_cuadro.config(font="Arial 10")

        self.hora_f_label=ttk.Label(self.frame_asig_hr, text="Hora Final")
        self.hora_f_label.grid(row=0, column=4, padx=5, pady=5)
        self.hora_f_label.config(font="Arial 10")
        self.hora_f_cuadro = ttk.Entry(self.frame_asig_hr, textvariable=self.hora_f_cuadro_var)
        self.hora_f_cuadro.grid(row=0, column=5, padx=5, pady=5)
        self.hora_f_cuadro.config(font="Arial 10")
        # Pestaña ambiente
        self.ambiente_labels_entrys=ttk.Frame(self.frame_ambiente)
        self.ambiente_labels_entrys.grid(row=2, column=0)

        self.idamb_label=ttk.Label(self.ambiente_labels_entrys, text="Id")
        self.idamb_label.grid(row=0, column=0,padx=5, pady=5)
        self.idamb_label.config(font="Arial 10")
        self.idamb_cuadro = ttk.Combobox(self.ambiente_labels_entrys, textvariable=self.idamb_cuadro_var)
        self.idamb_cuadro.grid(row=0, column=1,padx=5, pady=5)
        self.idamb_cuadro.config(font="Arial 10")
        self.idamb_cuadro.bind("<<ComboboxSelected>>", lambda event: actualizar_campos_amb(event, self.idamb_cuadro, 
                                self.ambiente_cuadro, self.seccion_cuadro, self.dia_cuadro))
            # Cargar datos en el Combobox
        cargar_datos_combobox_amb(self.idamb_cuadro)


        self.ambiente_label=ttk.Label(self.ambiente_labels_entrys, text="Ambiente")
        self.ambiente_label.grid(row=1, column=0, padx=5, pady=5)
        self.ambiente_label.config(font="Arial 10")
        self.ambiente_cuadro = ttk.Entry(self.ambiente_labels_entrys, textvariable=self.ambiente_cuadro_var)
        self.ambiente_cuadro.grid(row=1, column=1,padx=5, pady=5)
        self.ambiente_cuadro.config(font="Arial 10")

        self.seccion_label=ttk.Label(self.ambiente_labels_entrys, text="Seccion")
        self.seccion_label.grid(row=2, column=0,padx=5, pady=5)
        self.seccion_label.config(font="Arial 10")
        self.seccion_cuadro = ttk.Entry(self.ambiente_labels_entrys, textvariable=self.seccion_cuadro_var)
        self.seccion_cuadro.grid(row=2, column=1,padx=5, pady=5)
        self.seccion_cuadro.config(font="Arial 10")

        self.dia_label=ttk.Label(self.ambiente_labels_entrys, text="Dia")
        self.dia_label.grid(row=3, column=0, padx=5, pady=5)
        self.dia_label.config(font="Arial 10")
        self.dia_cuadro = ttk.Entry(self.ambiente_labels_entrys, textvariable=self.dia_cuadro_var)
        self.dia_cuadro.grid(row=3, column=1,padx=5, pady=5)
        self.dia_cuadro.config(font="Arial 10")

        #Pestaña asignacion hora ambiente
        self.idhramb_label=ttk.Label(self.frame_asig_hr_amb, text="Id")
        self.idhramb_label.grid(row=0, column=0, padx=5, pady=5)
        self.idhramb_label.config(font="Arial 10")
        self.idhramb_cuadro = ttk.Entry(self.frame_asig_hr_amb, textvariable=self.idhramb_cuadro_var)
        self.idhramb_cuadro.grid(row=0, column=1, padx=5, pady=5)
        self.idhramb_cuadro.config(font="Arial 10")

        self.idhoras_label=ttk.Label(self.frame_asig_hr_amb, text="Id Horas")
        self.idhoras_label.grid(row=0, column=2, padx=5)
        self.idhoras_label.config(font="Arial 10")
        self.idhoras_cuadro = ttk.Combobox(self.frame_asig_hr_amb, textvariable=self.idhoras_cuadro_var)
        self.idhoras_cuadro.grid(row=0, column=3, padx=3, pady=5)
        self.idhoras_cuadro.config(font="Arial 10")

        self.id_ambiente_label=ttk.Label(self.frame_asig_hr_amb, text="Id Amb")
        self.id_ambiente_label.grid(row=0, column=4, padx=5, pady=5)
        self.id_ambiente_label.config(font="Arial 10")
        self.id_ambiente_cuadro = ttk.Combobox(self.frame_asig_hr_amb, textvariable=self.id_ambiente_cuadro_var)
        self.id_ambiente_cuadro.grid(row=0, column=5, padx=5, pady=5)
        self.id_ambiente_cuadro.config(font="Arial 10")
        # Llamar al método llenar_combobox() en la instancia de ConexConexion

        # No olvides cerrar la conexión cuando hayas terminado de usarla
        self.conn.connection.close()
#                                          FACILITADOR
        self.notebook = ttk.Notebook(self.frame_facilitador)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        # Pestaña 1
        self.tab1f = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1f, text="Registro Facilitador")
        self.label_entry_frame_f = ttk.Frame(self.tab1f)
        self.label_entry_frame_f.grid(row=0, column=0, padx=15, pady=15)
        # Pestaña 2
        self.tab2f = ttk.Frame(self.notebook)
         # #Pestaña 3
        # 
        #Pestaña 4
 
        self.tab4f = ttk.Frame(self.notebook_asig)
        self.tab4f.rowconfigure(0, weight=0)
        self.tab4f.columnconfigure(0, weight=1)
        self.notebook_asig.add(self.tab4f, text="Asignacion Facilitador Curso")

        self.label_entry_frame_4f = ttk.Frame(self.tab2f)
        self.label_entry_frame_4f.grid(row=0, column=0, padx=15, pady=15)
        #Pestaña facilitador
        self.faci_labels_entrys=ttk.Frame(self.label_entry_frame_f)
        self.faci_labels_entrys.grid(row=4, column=0)

        self.cedulaf_label=ttk.Label(self.faci_labels_entrys , text="Cedula")
        self.cedulaf_label.grid(row=0, column=0, padx=5, pady=5,ipady=5)
        self.cedulaf_label.config(font="Arial 10")
        self.cedulaf_cuadro = ttk.Combobox(self.faci_labels_entrys, textvariable=self.cedulaf_cuadro_var )
        self.cedulaf_cuadro.grid(row=0, column=1, padx=5, pady=5,ipady=5)
        self.cedulaf_cuadro.config(font="Arial 10")
        self.cedulaf_cuadro.bind("<<ComboboxSelected>>", lambda event: actualizar_campos_facilitador(event, 
        self.cedulaf_cuadro, self.nombresf_cuadro, self.apellidosf_cuadro, self.horaclasef_cuadro))
        cargar_datos_combobox_facilitador(self.cedulaf_cuadro)


        self.nombresf_label=ttk.Label(self.faci_labels_entrys , text="Nombres")
        self.nombresf_label.grid(row=0, column=2, padx=5, pady=5,ipady=5)
        self.nombresf_label.config(font="Arial 10")
        self.nombresf_cuadro = ttk.Entry(self.faci_labels_entrys,textvariable=self.nombresf_cuadro_var )
        self.nombresf_cuadro.grid(row=0, column=3, padx=5, pady=5,ipady=5)
        self.nombresf_cuadro.config(font="Arial 10")

        self.apellidosf_label=ttk.Label(self.faci_labels_entrys , text="Apellido")
        self.apellidosf_label.grid(row=0, column=4, padx=5, pady=5,ipady=5)
        self.apellidosf_label.config(font="Arial 10")
        self.apellidosf_cuadro = ttk.Entry(self.faci_labels_entrys, textvariable=self.apellidosf_cuadro_var )
        self.apellidosf_cuadro.grid(row=0, column=5, padx=15, pady=15,ipady=5)
        self.apellidosf_cuadro.config(font="Arial 10")




        #Pestaña Asignacion facilitador horario
        self.asig_fa_hora_labels_entrys=ttk.Frame(self.tab4f)
        self.asig_fa_hora_labels_entrys.grid(row=1, column=0)

        self.id_asigfaho_label=ttk.Label(self.asig_fa_hora_labels_entrys , text="Id")
        self.id_asigfaho_label.grid(row=0, column=2, padx=5, pady=5,ipady=5)
        self.id_asigfaho_label.config(font="Arial 10")
        self.id_asigfaho_cuadro = ttk.Entry( self.asig_fa_hora_labels_entrys, textvariable=self.id_asigfa_cuadro_var)
        self.id_asigfaho_cuadro.grid(row=0, column=1, padx=5, pady=5,ipady=5)
        self.id_asigfaho_cuadro.config(font="Arial 10")

        self.idfa_asigfaho_label=ttk.Label(self.asig_fa_hora_labels_entrys , text="Cedula F")
        self.idfa_asigfaho_label.grid(row=0, column=2, padx=5, pady=5,ipady=5)
        self.idfa_asigfaho_label.config(font="Arial 10")
        self.idfa_asigfaho_cuadro = ttk.Entry( self.asig_fa_hora_labels_entrys, textvariable=self.ced_asigfaho_cuadro_var)
        self.idfa_asigfaho_cuadro.grid(row=0, column=3, padx=5, pady=5,ipady=5)
        self.idfa_asigfaho_cuadro.config(font="Arial 10")

        self.codigo_asig_label=ttk.Label(self.asig_fa_hora_labels_entrys, text="Codigo Pensum")
        self.codigo_asig_label.grid(row=0, column=4, padx=15, pady=15,ipady=5)
        self.codigo_asig_label.config(font="Arial 10")
        self.codigo_asig_cuadro = ttk.Entry(self.asig_fa_hora_labels_entrys, textvariable=self.codigo_asig_cuadro_var)
        self.codigo_asig_cuadro.grid(row=0, column=5, padx=15, pady=15,ipady=5)
        self.codigo_asig_cuadro.config(font="Arial 10")

        self.id_asighramb_asigfaho_label=ttk.Label(self.asig_fa_hora_labels_entrys , text="Id Asig Hora/Amb")
        self.id_asighramb_asigfaho_label.grid(row=0, column=6, padx=5, pady=5,ipady=5)
        self.id_asighramb_asigfaho_label.config(font="Arial 10")
        self.id_asighramb_asigfaho_cuadro = ttk.Entry( self.asig_fa_hora_labels_entrys, textvariable=self.id_asighramb_asigfaho_cuadro_var)
        self.id_asighramb_asigfaho_cuadro.grid(row=0, column=7, padx=5, pady=5,ipady=5)
        self.id_asighramb_asigfaho_cuadro.config(font="Arial 10")
#                               Entrys y label participante   
        
        self.label_entry_frame_4 = ttk.Frame(self.frame_participante)
        self.label_entry_frame_4.grid(row=1, column=0, padx=15, pady=15)

        self.cedulap_label=ttk.Label(self.label_entry_frame_4, text="Cedula")
        self.cedulap_label.grid(row=0, column=0, padx=15, pady=15)
        self.cedulap_label.config(font="Arial 10")
        self.cedulap_cuadro = ttk.Combobox(self.label_entry_frame_4, textvariable=self.cedulap_cuadro_var)
        self.cedulap_cuadro.grid(row=0, column=1, padx=15, pady=15)
        
        self.cedulap_cuadro.bind("<<ComboboxSelected>>", lambda event: actualizar_campos_participante(
            event, self.cedulap_cuadro_var, self.nombresp_cuadro_var, self.apellidosp_cuadro_var, 
            self.total_cre_par_cuadro_var, self.total_cur_par_cuadro_var, self.sexop_var, self.edadp_var,
            self.telefonop_var, self.emailp_var, self.edop_var, self.municipiop_var, self.parroquiap_var,
            self.grupo_in_p_var, self.programap_var, self.sistemap_var, self.discapacidadp_var))

        cargar_datos_combobox_participante(self.cedulap_cuadro)


        self.nombresp_label=ttk.Label(self.label_entry_frame_4, text="Nombres")
        self.nombresp_label.grid(row=0, column=2, padx=15, pady=15)
        self.nombresp_label.config(font="Arial 10")
        self.nombresp_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.nombresp_cuadro_var)
        self.nombresp_cuadro.grid(row=0, column=3, padx=15, pady=15)
        self.nombresp_cuadro.config(font="Arial 10")

        self.apellidosp_label=ttk.Label(self.label_entry_frame_4, text="Apellidos")
        self.apellidosp_label.grid(row=0, column=4, padx=15, pady=15)
        self.apellidosp_label.config(font="Arial 10")
        self.apellidosp_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.apellidosp_cuadro_var)
        self.apellidosp_cuadro.grid(row=0, column=5, padx=15, pady=15)
        self.apellidosp_cuadro.config(font="Arial 10")

        self.sexop_label=ttk.Label(self.label_entry_frame_4, text="Sexo")
        self.sexop_label.grid(row=0, column=6, padx=15, pady=15)
        self.sexop_label.config(font="Arial 10")
        # Configuración del Combobox para mostrar opciones de "M" y "F"
        self.sexop_cuadro = ttk.Combobox(self.label_entry_frame_4, values=["M", "F"], textvariable=self.sexop_var)
        self.sexop_cuadro.grid(row=0, column=7, padx=15, pady=15)
        self.sexop_cuadro.config(font="Arial 10")


        self.edadp_label=ttk.Label(self.label_entry_frame_4, text="Edad")
        self.edadp_label.grid(row=1, column=0, padx=15, pady=15)
        self.edadp_label.config(font="Arial 10")
        self.edadp_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.edadp_var)
        self.edadp_cuadro.grid(row=1, column=1, padx=15, pady=15)
        self.edadp_cuadro.config(font="Arial 10")

        self.telefonop_label=ttk.Label(self.label_entry_frame_4, text="Telefono")
        self.telefonop_label.grid(row=1, column=2, padx=15, pady=15)
        self.telefonop_label.config(font="Arial 10")
        self.telefonop_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.telefonop_var)
        self.telefonop_cuadro.grid(row=1, column=3, padx=15, pady=15)
        self.telefonop_cuadro.config(font="Arial 10")

        self.emailp_label=ttk.Label(self.label_entry_frame_4, text="E-mail")
        self.emailp_label.grid(row=1, column=4, padx=15, pady=15)
        self.emailp_label.config(font="Arial 10")
        self.emailp_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.emailp_var)
        self.emailp_cuadro.grid(row=1, column=5, padx=15, pady=15)
        self.emailp_cuadro.config(font="Arial 10")

        self.edop_label=ttk.Label(self.label_entry_frame_4, text="Estado")
        self.edop_label.grid(row=1, column=6, padx=15, pady=15)
        self.edop_label.config(font="Arial 10")
        self.edop_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.edop_var)
        self.edop_cuadro.grid(row=1, column=7, padx=15, pady=15)
        self.edop_cuadro.config(font="Arial 10")

        self.municipiop_label=ttk.Label(self.label_entry_frame_4, text="Municipio")
        self.municipiop_label.grid(row=2, column=0, padx=15, pady=15)
        self.municipiop_label.config(font="Arial 10")
        self.municipiop_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.municipiop_var)
        self.municipiop_cuadro.grid(row=2, column=1, padx=15, pady=15)
        self.municipiop_cuadro.config(font="Arial 10")

        self.parroquiap_label=ttk.Label(self.label_entry_frame_4, text="Parroquia")
        self.parroquiap_label.grid(row=2, column=2, padx=15, pady=15)
        self.parroquiap_label.config(font="Arial 10")
        self.parroquiap_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.parroquiap_var)
        self.parroquiap_cuadro.grid(row=2, column=3, padx=15, pady=15)
        self.parroquiap_cuadro.config(font="Arial 10")

        self.discapacidadp_label=ttk.Label(self.label_entry_frame_4, text="Discapacidad")
        self.discapacidadp_label.grid(row=2, column=4, padx=15, pady=15)
        self.discapacidadp_label.config(font="Arial 10")
        self.discapacidadp_cuadro = ttk.Combobox(self.label_entry_frame_4, textvariable=self.discapacidadp_var,values=["Si", "No"])
        self.discapacidadp_cuadro.grid(row=2, column=5, padx=15, pady=15)
        self.discapacidadp_cuadro.config(font="Arial 10")

        self.grupo_in_p_label=ttk.Label(self.label_entry_frame_4, text="Grupo Indigena")
        self.grupo_in_p_label.grid(row=2, column=6, padx=15, pady=15)
        self.grupo_in_p_label.config(font="Arial 10")
        self.grupo_in_p_cuadro = ttk.Combobox(self.label_entry_frame_4, textvariable= self.grupo_in_p_var,values=["Si", "No"])
        self.grupo_in_p_cuadro.grid(row=2, column=7, padx=15, pady=15)
        self.grupo_in_p_cuadro.config(font="Arial 10")

        self.programap_label=ttk.Label(self.label_entry_frame_4, text="Programa o Carrera")
        self.programap_label.grid(row=3, column=0, padx=15, pady=15)
        self.programap_label.config(font="Arial 10")
        self.programap_cuadro = ttk.Entry(self.label_entry_frame_4, textvariable=self.programap_var)
        self.programap_cuadro.grid(row=3, column=1, padx=15, pady=15)
        self.programap_cuadro.config(font="Arial 10")

        self.sistemap_label=ttk.Label(self.label_entry_frame_4, text="Sistema")
        self.sistemap_label.grid(row=3, column=2, padx=15, pady=15)
        self.sistemap_label.config(font="Arial 10")
        self.sistemap_cuadro = ttk.Combobox(self.label_entry_frame_4, textvariable=self.sistemap_var,values=["SIACE", "SGA"])
        self.sistemap_cuadro.grid(row=3, column=3, padx=15, pady=15)
        self.sistemap_cuadro.config(font="Arial 10")

        
#                                               Insricripcion
        self.notebook_inscripcion = ttk.Notebook(self.frame_inscripcion)
        self.notebook_inscripcion.pack(fill=tk.BOTH, expand=True)
        # Pestaña 1
        self.tab_inscripcion = ttk.Frame(self.notebook_inscripcion)
        self.notebook_inscripcion.add(self.tab_inscripcion, text="Incripcion")

        self.inscripcion_labels_entrys=ttk.Frame(self.tab_inscripcion)
        self.inscripcion_labels_entrys.grid(row=3, column=0, pady=20)


        
        self.id_par_inscri_label=ttk.Label(self.inscripcion_labels_entrys, text="Cedula Participante")
        self.id_par_inscri_label.grid(row=0, column=0, padx=5, pady=5,ipady=5)
        self.id_par_inscri_label.config(font="Arial 10")
        self.id_par_inscri_cuadro = ttk.Entry(self.inscripcion_labels_entrys, textvariable=self.ced_par_inscri_cuadro_var)
        self.id_par_inscri_cuadro.grid(row=0, column=1, padx=5, pady=5,ipady=5)
        self.id_par_inscri_cuadro.config(font="Arial 10")

        self.id_asi_faho_inscri_label=ttk.Label(self.inscripcion_labels_entrys , text="Id asignacion facilitador Curso")
        self.id_asi_faho_inscri_label.grid(row=0, column=2, padx=5, pady=5,ipady=5)
        self.id_asi_faho_inscri_label.config(font="Arial 10")
        self.id_asi_faho_inscri_cuadro = ttk.Entry(self.inscripcion_labels_entrys, textvariable=self.id_asi_faho_inscri_cuadro_var)
        self.id_asi_faho_inscri_cuadro.grid(row=0, column=3, padx=5, pady=5,ipady=5)
        self.id_asi_faho_inscri_cuadro.config(font="Arial 10")

        self.id_periodo_inscri_label=ttk.Label(self.inscripcion_labels_entrys , text="Id Periodo")
        self.id_periodo_inscri_label.grid(row=0, column=4, padx=5, pady=5,ipady=5)
        self.id_periodo_inscri_label.config(font="Arial 10")
        self.id_periodo_inscri_cuadro = ttk.Entry(self.inscripcion_labels_entrys, textvariable=self.id_periodo_inscri_cuadro_var)
        self.id_periodo_inscri_cuadro.grid(row=0, column=5, padx=5, pady=5,ipady=5)
        self.id_periodo_inscri_cuadro.config(font="Arial 10")




        #                                   PERIODO ACADEMICO
        self.tab_periodo = ttk.Frame(self.notebook_inscripcion)
        self.notebook_inscripcion.add(self.tab_periodo, text="Perido Academico")

        self.periodo_label_entry_frame = ttk.Frame(self.tab_periodo)
        self.periodo_label_entry_frame.grid(row=3, column=0, padx=15, pady=15, sticky="nsew")

        self.nombre_periodo_label=ttk.Label(self.periodo_label_entry_frame, text="Nombre")
        self.nombre_periodo_label.grid(row=0, column=0, padx=15, pady=15)
        self.nombre_periodo_label.config(font="Arial 10")
        self.nombre_periodo_cuadro = ttk.Entry(self.periodo_label_entry_frame, textvariable=self.nombre_periodo_cuadro_var)
        self.nombre_periodo_cuadro.grid(row=0, column=1, padx=15, pady=15)
        self.nombre_periodo_cuadro.config(font="Arial 10")

        self.fechai_periodo_label=ttk.Label(self.periodo_label_entry_frame, text="Fecha Inicio")
        self.fechai_periodo_label.grid(row=0, column=2, padx=15, pady=15)
        self.fechai_periodo_label.config(font="Arial 10")
        self.fechai_periodo_cuadro = ttk.Entry(self.periodo_label_entry_frame, textvariable=self.fechai_periodo_cuadro_var)
        self.fechai_periodo_cuadro.grid(row=0, column=3, padx=15, pady=15)
        self.fechai_periodo_cuadro.config(font="Arial 10")

        self.fechaf_periodo_label=ttk.Label(self.periodo_label_entry_frame, text="Fecha Fin")
        self.fechaf_periodo_label.grid(row=0, column=4, padx=15, pady=15)
        self.fechaf_periodo_label.config(font="Arial 10")
        self.fechaf_periodo_cuadro = ttk.Entry(self.periodo_label_entry_frame, textvariable=self.fechaf_periodo_cuadro_var)
        self.fechaf_periodo_cuadro.grid(row=0, column=5, padx=15, pady=15)
        self.fechaf_periodo_cuadro.config(font="Arial 10")

    
     

#                                           REPORTES
        self.tab_reporte = ttk.Frame(self.notebook_inscripcion)
        self.notebook_inscripcion.add(self.tab_reporte, text="Reportes")

        self.label_reporte_i=ttk.Frame(self.tab_reporte)
        self.label_reporte_i.grid(row=0, column=0)

        self.cedula_label_pdf=ttk.Label(self.label_reporte_i, text="Cedula")
        self.cedula_label_pdf.grid(row=0, column=1)
        self.cedula_label_pdf.config(font="Arial 10")
        self.cedula_cuadro_pdf = ttk.Entry(self.label_reporte_i, textvariable=self.cedulap_cuadro_var)
        self.cedula_cuadro_pdf.grid(row=0, column=2)
        self.cedula_cuadro_pdf.config(font="Arial 10")

        self.reportep_label_pdf=ttk.Label(self.label_reporte_i, text="Periodo")
        self.reportep_label_pdf.grid(row=0, column=3)
        self.reportep_label_pdf.config(font="Arial 10")
        self.reportep_cuadro_pdf = ttk.Entry(self.label_reporte_i, textvariable=self.nombre_periodo_cuadro_var)
        self.reportep_cuadro_pdf.grid(row=0, column=4)
        self.reportep_cuadro_pdf.config(font="Arial 10")

        self.cedulaf_label_pdf=ttk.Label(self.label_reporte_i, text="Cedula")
        self.cedulaf_label_pdf.grid(row=2, column=1)
        self.cedulaf_label_pdf.config(font="Arial 10")
        self.cedulaf_cuadro_pdf = ttk.Entry(self.label_reporte_i, textvariable=self.fcedula_cuadro_var)
        self.cedulaf_cuadro_pdf.grid(row=2, column=2)
        self.cedulaf_cuadro_pdf.config(font="Arial 10")

        self.reportef_label_pdf=ttk.Label(self.label_reporte_i, text="Periodo")
        self.reportef_label_pdf.grid(row=2, column=3)
        self.reportef_label_pdf.config(font="Arial 10")
        self.reportef_cuadro_pdf = ttk.Entry(self.label_reporte_i, textvariable=self.nombre_periodof_cuadro_var)
        self.reportef_cuadro_pdf.grid(row=2, column=4)
        self.reportef_cuadro_pdf.config(font="Arial 10")


#                                       Inicializar Treeview para Pensum
        self.frame_treeview_pensum = ttk.Frame(self.label_entry_frame_pensum, width=800, height=250)
        self.frame_treeview_pensum.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_pensum.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir el Treeview para Pensum
        self.treeview_pensum = ttk.Treeview(self.frame_treeview_pensum)
        self.treeview_pensum["columns"] = ("Codigo", "Curso", "U/C", "Ciclo", "Carrera", "Mencion")

        # Configurar columnas y encabezados
        column_widths = {"Codigo": 100, "Curso": 300, "U/C": 80, "Ciclo": 130,  "Carrera": 200, "Mencion": 200}

        self.treeview_pensum.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col, width in column_widths.items():
            self.treeview_pensum.column(col, anchor=tk.CENTER, width=width)
            self.treeview_pensum.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_pensum = ttk.Scrollbar(self.frame_treeview_pensum, orient=tk.VERTICAL, command=self.treeview_pensum.yview)
        scrollbar_horizontal_pensum = ttk.Scrollbar(self.frame_treeview_pensum, orient=tk.HORIZONTAL, command=self.treeview_pensum.xview)
        self.treeview_pensum.configure(yscroll=scrollbar_vertical_pensum.set, xscroll=scrollbar_horizontal_pensum.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_pensum.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_pensum.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_pensum.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_pensum.grid_rowconfigure(0, weight=1)
        self.frame_treeview_pensum.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_pensum_en_treeview()

#                                        Inicializar Treeview para Preseleccion

        self.treeview_preseleccion = ttk.Treeview(self.label_entry_frame_pre, height=10)
        self.treeview_preseleccion["columns"] = ("Id", "Cedula", "Id_periodo", "Inicio", "Fin", "Codigo", "Curso")
        
        # Configurar columnas
        self.treeview_preseleccion.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        column_widths = {
            "Id": 50,
            "Cedula": 100,
            "Id_periodo": 100,
            "Inicio": 100,
            "Fin": 100,
            "Codigo": 100,
            "Curso": 300
        }
        for col, width in column_widths.items():
            self.treeview_preseleccion.column(col, anchor=tk.CENTER, width=width)
            self.treeview_preseleccion.heading(col, text=col, anchor=tk.CENTER)
        
        # Añadir Treeview a la ventana
        self.treeview_preseleccion.grid(row=0, column=0, padx=15, pady=15, rowspan=7)
        self.mostrar_preseleccion_treeview()

#                                        Inicializar Treeview para ambiente

        self.label_entry_frame_ambiente = ttk.Frame(self.label_entry_frame_2, width=600, height=300)
        self.label_entry_frame_ambiente.grid(row=0, column=1, padx=15, pady=15, rowspan=7, sticky="nsew")
        self.label_entry_frame_ambiente.grid_propagate(False)  # Evitar que el frame se expanda automáticamente

        # Definir el Treeview para Ambiente
        self.treeview_ambiente = ttk.Treeview(self.label_entry_frame_ambiente)
        self.treeview_ambiente["columns"] = ("Id", "Ambiente", "Seccion", "Dia")

        # Configurar columnas y encabezados
        col_widths_ambiente = {
            "Id": 50, "Ambiente": 150, "Seccion": 100, "Dia": 100
        }

        self.treeview_ambiente.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_ambiente["columns"]:
            self.treeview_ambiente.column(col, anchor=tk.CENTER, width=col_widths_ambiente.get(col, 100))
            self.treeview_ambiente.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_ambiente = ttk.Scrollbar(self.label_entry_frame_ambiente, orient=tk.VERTICAL, command=self.treeview_ambiente.yview)
        scrollbar_horizontal_ambiente = ttk.Scrollbar(self.label_entry_frame_ambiente, orient=tk.HORIZONTAL, command=self.treeview_ambiente.xview)
        self.treeview_ambiente.configure(yscroll=scrollbar_vertical_ambiente.set, xscroll=scrollbar_horizontal_ambiente.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_ambiente.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_ambiente.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_ambiente.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.label_entry_frame_ambiente.grid_rowconfigure(0, weight=1)
        self.label_entry_frame_ambiente.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_ambiente_en_treeview()


        #                                        Inicializar Treeview para Horas
        self.frame_treeview_horas = ttk.Frame(self.tab1, width=400, height=250)
        self.frame_treeview_horas.grid(row=0, column=3, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_horas.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir el Treeview para Horas
        self.treeview_horas = ttk.Treeview(self.frame_treeview_horas)
        self.treeview_horas["columns"] = ("Id", "Hora Inicio", "Hora Final")

        # Configurar columnas y encabezados
        col_widths_horas = {
            "Id": 50, "Hora Inicio": 120, "Hora Final": 120
        }

        self.treeview_horas.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_horas["columns"]:
            self.treeview_horas.column(col, anchor=tk.CENTER, width=col_widths_horas.get(col, 100))
            self.treeview_horas.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_horas = ttk.Scrollbar(self.frame_treeview_horas, orient=tk.VERTICAL, command=self.treeview_horas.yview)
        scrollbar_horizontal_horas = ttk.Scrollbar(self.frame_treeview_horas, orient=tk.HORIZONTAL, command=self.treeview_horas.xview)
        self.treeview_horas.configure(yscroll=scrollbar_vertical_horas.set, xscroll=scrollbar_horizontal_horas.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_horas.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_horas.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_horas.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_horas.grid_rowconfigure(0, weight=1)
        self.frame_treeview_horas.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_horas_en_treeview()


        
        #                                        Inicializar Treeview para asignacion Horas y ambiente

        self.frame_treeview_hr_amb = ttk.Frame(self.tab3, width=800, height=300)
        self.frame_treeview_hr_amb.grid(row=0, column=0, padx=15, pady=15, rowspan=7, sticky="nsew")
        self.frame_treeview_hr_amb.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir el Treeview para Horas-Ambiente
        self.treeview_hr_amb = ttk.Treeview(self.frame_treeview_hr_amb)
        self.treeview_hr_amb["columns"] = ("Id", "Id Hora", "Id Ambiente", "Hora Inicial", "Hora Final", "Ambiente", "Seccion", "Dia")

        # Configurar columnas y encabezados
        col_widths_hr_amb = {
            "Id": 50, "Id Hora": 100, "Id Ambiente": 100, "Hora Inicial": 120, "Hora Final": 120,
            "Ambiente": 150, "Seccion": 100, "Dia": 100
        }

        self.treeview_hr_amb.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_hr_amb["columns"]:
            self.treeview_hr_amb.column(col, anchor=tk.CENTER, width=col_widths_hr_amb.get(col, 100))
            self.treeview_hr_amb.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_hr_amb = ttk.Scrollbar(self.frame_treeview_hr_amb, orient=tk.VERTICAL, command=self.treeview_hr_amb.yview)
        scrollbar_horizontal_hr_amb = ttk.Scrollbar(self.frame_treeview_hr_amb, orient=tk.HORIZONTAL, command=self.treeview_hr_amb.xview)
        self.treeview_hr_amb.configure(yscroll=scrollbar_vertical_hr_amb.set, xscroll=scrollbar_horizontal_hr_amb.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_hr_amb.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_hr_amb.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_hr_amb.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_hr_amb.grid_rowconfigure(0, weight=1)
        self.frame_treeview_hr_amb.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_asignacion_hr_amb_en_treeview()

        #                                        
       #                                        Inicializar Treeview para asignacion facilitador CURSO

    # Frame contenedor para Treeview de Asignación Facilitador-Curso
        self.frame_treeview_asig_faci_hora = ttk.Frame(self.tab4f, width=900, height=350)
        self.frame_treeview_asig_faci_hora.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_asig_faci_hora.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir el Treeview para Facilitador-Curso
        self.treeview_asig_faci_hora = ttk.Treeview(self.frame_treeview_asig_faci_hora)
        self.treeview_asig_faci_hora["columns"] = (
            "Id", "Cedula", "Nombre", "Apellido", "Id_hr_amb", "Hora Inicial", "Hora Final", "Amb",
            "Secc", "Dia", "Codigo", "Curso", "Ciclo"
        )

        # Configurar columnas y encabezados
        col_widths_faci_hora = {
            "Id": 30, "Cedula": 100, "Nombre": 200, "Apellido": 200, "Id_hr_amb": 140, "Hora Inicial": 110,
            "Hora Final": 100, "Amb": 80, "Secc": 60, "Dia": 80, "Codigo": 80, "Curso": 250, "Ciclo": 100
        }

        self.treeview_asig_faci_hora.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_asig_faci_hora["columns"]:
            self.treeview_asig_faci_hora.column(col, anchor=tk.CENTER, width=col_widths_faci_hora.get(col, 70))
            self.treeview_asig_faci_hora.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_faci_hora = ttk.Scrollbar(self.frame_treeview_asig_faci_hora, orient=tk.VERTICAL, command=self.treeview_asig_faci_hora.yview)
        scrollbar_horizontal_faci_hora = ttk.Scrollbar(self.frame_treeview_asig_faci_hora, orient=tk.HORIZONTAL, command=self.treeview_asig_faci_hora.xview)
        self.treeview_asig_faci_hora.configure(yscroll=scrollbar_vertical_faci_hora.set, xscroll=scrollbar_horizontal_faci_hora.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_asig_faci_hora.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_faci_hora.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_faci_hora.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_asig_faci_hora.grid_rowconfigure(0, weight=1)
        self.frame_treeview_asig_faci_hora.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_asig_faci_hora_treeview()


#                                             Inicializar Treeview para Facilitador

        self.label_entry_frame_f = ttk.Frame(self.label_entry_frame_f, width=1000, height=350)  # Ajustar el tamaño del contenedor
        self.label_entry_frame_f.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.label_entry_frame_f.grid_propagate(False)  # Evitar que el frame se expanda

        # Inicializar el Treeview para Facilitador
        self.treeview_facilitador = ttk.Treeview(self.label_entry_frame_f)
        self.treeview_facilitador["columns"] = ("Cedula", "Nombres", "Apellido", "Hora Clase")

        # Configurar el ancho de cada columna usando un diccionario
        col_widths_facilitador = {
            "Cedula": 100,
            "Nombres": 300,
            "Apellido": 300,
            "Hora Clase": 100,
        }

        # Configurar columnas
        self.treeview_facilitador.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_facilitador["columns"]:
            self.treeview_facilitador.column(col, anchor=tk.CENTER, width=col_widths_facilitador.get(col, 80))
            self.treeview_facilitador.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_facilitador = ttk.Scrollbar(self.label_entry_frame_f, orient=tk.VERTICAL, command=self.treeview_facilitador.yview)
        scrollbar_horizontal_facilitador = ttk.Scrollbar(self.label_entry_frame_f, orient=tk.HORIZONTAL, command=self.treeview_facilitador.xview)
        self.treeview_facilitador.configure(yscroll=scrollbar_vertical_facilitador.set, xscroll=scrollbar_horizontal_facilitador.set)

        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_facilitador.grid(row=0, column=0, sticky="nsew", rowspan=7)  # Ajusta la posición y el rowspan según tus necesidades
        scrollbar_vertical_facilitador.grid(row=0, column=1, sticky="ns")  # Colocar barra vertical
        scrollbar_horizontal_facilitador.grid(row=1, column=0, sticky="ew")  # Colocar barra horizontal

        # Ajustar el tamaño del Treeview dentro del frame
        self.label_entry_frame_f.grid_rowconfigure(0, weight=1)
        self.label_entry_frame_f.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_facilitador_treeview()

        #                                   Treeview Participante
         # Establecer un ancho máximo para el contenedor del Treeview
        self.label_entry_frame_5 = ttk.Frame(self.frame_participante, width=1000, height=300)
        self.label_entry_frame_5.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.label_entry_frame_5.grid_propagate(False)  # Evitar que el frame se expanda
        
        # Definir el Treeview
        self.treeview_participante = ttk.Treeview(self.label_entry_frame_5)
        self.treeview_participante["columns"] = (
                    "Cedula", "Nombres", "Apellido", "Sexo", "Edad", 
                    "Telefono", "E-mail", "Estado", "Municipio", "Parroquia", 
                    "Discapacidad", "Grupo Indigena", "Carrera", "Creditos", 
                    "Cursos","Sistema"
                )

        
        # Configurar el ancho de cada columna usando un diccionario
        col_widths = {
            "Cedula": 100,"Nombres": 300,"Apellido": 300,"Sexo": 70,
            "Edad": 50,"Telefono": 200,"E-mail": 300,"Estado": 150,
            "Municipio": 150,"Parroquia": 150,"Discapacidad": 130,"Grupo Indigena": 140,
            "Carrera": 400,"Sistema":80,"Creditos": 100,"Curso": 100,
        }
        
        # Configurar columnas y encabezados
        self.treeview_participante.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_participante["columns"]:
            self.treeview_participante.column(col, anchor=tk.CENTER, width=col_widths.get(col, 100))
            self.treeview_participante.heading(col, text=col, anchor=tk.CENTER)

        
        # Añadir barras de desplazamiento
        scrollbar_vertical = ttk.Scrollbar(self.label_entry_frame_5, orient=tk.VERTICAL, command=self.treeview_participante.yview)
        scrollbar_horizontal = ttk.Scrollbar(self.label_entry_frame_5, orient=tk.HORIZONTAL, command=self.treeview_participante.xview)
        self.treeview_participante.configure(yscroll=scrollbar_vertical.set, xscroll=scrollbar_horizontal.set)
        
        # Posicionar el Treeview y las barras de desplazamiento
        self.treeview_participante.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal.grid(row=1, column=0, sticky="ew")
        
        # Ajustar el tamaño del Treeview dentro del frame
        self.label_entry_frame_5.grid_rowconfigure(0, weight=1)
        self.label_entry_frame_5.grid_columnconfigure(0, weight=1)
        
        # Llamar a la función para mostrar los datos
        self.mostrar_participante_treeview()
                                                       
            #                                       TREEVIEW DE INSCRIPCION
                                                       # Frame principal
        # Establecer un ancho máximo para el contenedor del Treeview
        self.frame_treeview_inscripcion = ttk.Frame(self.tab_inscripcion, width=1000, height=300)
        self.frame_treeview_inscripcion.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_inscripcion.grid_propagate(False)  # Evitar que el frame se expanda

        self.frame_treeview_inscripcion.columnconfigure(0, weight=1)
        self.frame_treeview_inscripcion.rowconfigure(0, weight=1)

        # Configurar Treeview
        self.treeview_inscripcion = ttk.Treeview(self.frame_treeview_inscripcion, height=15, show="headings")
        self.treeview_inscripcion["columns"] = (
            "Cedula_p", "Nombre_p", "Apellido_p","ID AFC", 
            "Cedula_f", "Nombre_f", "Apellido_f", 
            "Inico", "Fin", "Ambiente", "Dia", "Secc", 
            "Codigo", "Curso", "Ciclo", "Periodo", "Cursos", "Creditos", "Validado"  
        )

        # Aplicar el ancho definido en col_widths
        col_widths = {
            "Cedula_p": 120, "Nombre_p": 250, "Apellido_p": 150,"ID AFC":100, 
            "Cedula_f": 100, "Nombre_f": 300, 
            "Apellido_fac": 300, "Inico": 80, 
            "Fin": 80, "Ambiente": 100, "Dia": 100, "Secc": 80, 
            "Codigo": 100, "Curso": 200, "Ciclo": 100, "Periodo": 100,
            "Cursos": 80, "Creditos": 80, "Validado": 90
        }

        for col in self.treeview_inscripcion["columns"]:
            self.treeview_inscripcion.column(col, anchor=tk.W, width=col_widths.get(col, 100))
            self.treeview_inscripcion.heading(col, text=col, anchor=tk.W)

        # Agregar Treeview al frame_treeview_inscripcion
        self.treeview_inscripcion.grid(row=0, column=0, sticky="nsew")


        # Configurar barra de desplazamiento horizontal
        scrollbar_i = ttk.Scrollbar(self.frame_treeview_inscripcion, orient=tk.HORIZONTAL, command=self.treeview_inscripcion.xview)
        scrollbar_i.grid(row=1, column=0, sticky="ew")
        self.treeview_inscripcion.configure(xscrollcommand=scrollbar_i.set)

        # Configurar barra de desplazamiento vertical
        scrollbar_v = ttk.Scrollbar(self.frame_treeview_inscripcion, orient=tk.VERTICAL, command=self.treeview_inscripcion.yview)
        scrollbar_v.grid(row=0, column=1, sticky="ns")
        self.treeview_inscripcion.configure(yscrollcommand=scrollbar_v.set)

        # Ajuste del tamaño del Treeview dentro del frame
        self.frame_treeview_inscripcion.grid_rowconfigure(0, weight=1)
        self.frame_treeview_inscripcion.grid_columnconfigure(0, weight=1)

        # Mostrar datos en el Treeview
        self.mostrar_inscripcion_treeview()

                #                                        Inicializar Treeview para prediodo de preseleccion
        self.frame_treeview_pre_periodo = ttk.Frame(self.tab_periodo_pre, width=500, height=200)
        self.frame_treeview_pre_periodo.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_pre_periodo.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir Treeview para período de preselección
        self.treeview_pre_periodo = ttk.Treeview(self.frame_treeview_pre_periodo)
        self.treeview_pre_periodo["columns"] = ("Id", "Fecha Inicio", "Fecha Final")

        # Configurar columnas
        self.treeview_pre_periodo.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_pre_periodo["columns"]:
            self.treeview_pre_periodo.column(col, anchor=tk.CENTER, width=120)
            self.treeview_pre_periodo.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_pre_periodo = ttk.Scrollbar(self.frame_treeview_pre_periodo, orient=tk.VERTICAL, command=self.treeview_pre_periodo.yview)
        scrollbar_horizontal_pre_periodo = ttk.Scrollbar(self.frame_treeview_pre_periodo, orient=tk.HORIZONTAL, command=self.treeview_pre_periodo.xview)
        self.treeview_pre_periodo.configure(yscroll=scrollbar_vertical_pre_periodo.set, xscroll=scrollbar_horizontal_pre_periodo.set)

        # Posicionar Treeview y barras de desplazamiento
        self.treeview_pre_periodo.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_pre_periodo.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_pre_periodo.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_pre_periodo.grid_rowconfigure(0, weight=1)
        self.frame_treeview_pre_periodo.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_periodo_pre_treeview()


    #                                        Inicializar Treeview para prediodo academico

  # Frame contenedor para Treeview del período académico
        self.frame_treeview_periodo_academico = ttk.Frame(self.tab_periodo, width=500, height=200)
        self.frame_treeview_periodo_academico.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        self.frame_treeview_periodo_academico.grid_propagate(False)  # Evitar expansión automática del frame

        # Definir Treeview para período académico
        self.treeview_periodo_academico = ttk.Treeview(self.frame_treeview_periodo_academico)
        self.treeview_periodo_academico["columns"] = ("Nombre", "Fecha Inicio", "Fecha Final")

        # Configurar columnas
        self.treeview_periodo_academico.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        for col in self.treeview_periodo_academico["columns"]:
            self.treeview_periodo_academico.column(col, anchor=tk.CENTER, width=120)
            self.treeview_periodo_academico.heading(col, text=col, anchor=tk.CENTER)

        # Añadir barras de desplazamiento
        scrollbar_vertical_periodo_academico = ttk.Scrollbar(self.frame_treeview_periodo_academico, orient=tk.VERTICAL, command=self.treeview_periodo_academico.yview)
        scrollbar_horizontal_periodo_academico = ttk.Scrollbar(self.frame_treeview_periodo_academico, orient=tk.HORIZONTAL, command=self.treeview_periodo_academico.xview)
        self.treeview_periodo_academico.configure(yscroll=scrollbar_vertical_periodo_academico.set, xscroll=scrollbar_horizontal_periodo_academico.set)

        # Posicionar Treeview y barras de desplazamiento
        self.treeview_periodo_academico.grid(row=0, column=0, sticky="nsew")
        scrollbar_vertical_periodo_academico.grid(row=0, column=1, sticky="ns")
        scrollbar_horizontal_periodo_academico.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño del Treeview dentro del frame
        self.frame_treeview_periodo_academico.grid_rowconfigure(0, weight=1)
        self.frame_treeview_periodo_academico.grid_columnconfigure(0, weight=1)

        # Llamar a la función para mostrar los datos
        self.mostrar_periodo_academico_treeview()
#                                           BOTONES CRUD PENSUM            

        self.btns_pensum = ttk.Frame(self.label_entry_frame_pensum)
        self.btns_pensum.grid(row=10, column=0, padx=15, pady=15)
        self.btn_crear_p = ttk.Button(self.btns_pensum, text="Crear", command=self.llamar_crear_pensum)
        self.btn_crear_p.grid(row=0, column=0, padx=5)
        self.btn_buscar_p = ttk.Button(self.btns_pensum, text="Buscar",command=self.llamar_buscar_pensum_por_codigo)
        self.btn_buscar_p.grid(row=0, column=1,padx=5)
        self.btn_actualizar_p = ttk.Button(self.btns_pensum, text="Actualizar", command=self.llamar_actualizar_pensum)
        self.btn_actualizar_p.grid(row=0, column=2, padx=5)
        self.btn_eliminar_p = ttk.Button(self.btns_pensum, text="Eliminar", command=self.llamar_eliminar_pensum)
        self.btn_eliminar_p.grid(row=0, column=3, padx=5)

        self.btn_limpiarc_p = ttk.Button(self.btns_pensum, text="Limpiar Campos", command=self.limpiar_campos_pensum)
        self.btn_limpiarc_p.grid(row=0, column=4, padx=5)

# #                                          BOTONES CRUD HORAS
    
        self.btns_horas = ttk.Frame(self.tab1)
        self.btns_horas.grid(row=9, column=3, padx=20, pady=20, sticky="nsew")
        self.btn_crear_h = ttk.Button(self.btns_horas, text="Crear", command=self.llamar_crear_horas)
        self.btn_crear_h.grid(row=0, column=0, padx=5)
        self.btn_buscar_h = ttk.Button(self.btns_horas, text="Buscar", command=self.llamar_buscar_hora)
        self.btn_buscar_h.grid(row=0, column=1, padx=5)
        self.btn_actualizar_h = ttk.Button(self.btns_horas, text="Actualizar", command=self.llamar_actualizar_hora)
        self.btn_actualizar_h.grid(row=0, column=2, padx=5)
        self.btn_eliminar_h = ttk.Button(self.btns_horas, text="Eliminar", command=self.llamar_eliminar_hora)
        self.btn_eliminar_h.grid(row=0, column=3, padx=5)

        self.btn_limpiarc_h = ttk.Button(self.btns_horas, text="Limpiar Campos", command=self.limpiar_campos_horas)
        self.btn_limpiarc_h.grid(row=0, column=4, padx=5)

                                        # BOTONES CRUD AMBIENTE
        self.btns_ambiente = ttk.Frame(self.label_entry_frame_2)
        self.btns_ambiente.grid(row=3, column=0, padx=15, pady=15, sticky="nsew")
        self.btn_crear_amb = ttk.Button(self.btns_ambiente, text="Crear", command=self.llamar_crear_ambiente)
        self.btn_crear_amb.grid(row=0, column=0, padx=5)
        self.btn_buscar_amb = ttk.Button(self.btns_ambiente, text="Buscar", command=self.llamar_buscar_ambiente_por_nombre)
        self.btn_buscar_amb.grid(row=0, column=1, padx=5)
        self.btn_actualizar_amb = ttk.Button(self.btns_ambiente, text="Actualizar", command=self.llamar_actualizar_ambiente)
        self.btn_actualizar_amb.grid(row=0, column=2, padx=5)
        self.btn_eliminar_amb = ttk.Button(self.btns_ambiente, text="Eliminar", command=self.llamar_eliminar_ambiente)
        self.btn_eliminar_amb.grid(row=0, column=4, padx=5)

        self.btn_limpiarc_amb = ttk.Button(self.btns_ambiente, text="Limpiar Campos", command=self.limpiar_campos_ambiente)
        self.btn_limpiarc_amb.grid(row=0, column=5, padx=5)


        # BOTONES CRUD ASIGNACION HORA AMBIENTE
        self.btns_asignacion_hr_amb = ttk.Frame(self.tab3)
        self.btns_asignacion_hr_amb.grid(row=10, column=0, padx=15, pady=15, sticky="nsew")
        self.btn_crear_asig_hr_amb = ttk.Button(self.btns_asignacion_hr_amb, text="Crear", command=self.llamar_crear_asignacion_hr_amb)
        self.btn_crear_asig_hr_amb.grid(row=0, column=0, padx=5)
        self.btn_buscar_asig_hr_amb = ttk.Button(self.btns_asignacion_hr_amb, text="Buscar", command=self.llamar_buscar_asignacion_hr_amb_por_id)
        self.btn_buscar_asig_hr_amb.grid(row=0, column=1, padx=5)
        self.btn_actualizar_asig_hr_amb = ttk.Button(self.btns_asignacion_hr_amb, text="Actualizar", command=self.llamar_actualizar_asignacion_hr_amb)
        self.btn_actualizar_asig_hr_amb.grid(row=0, column=2, padx=5)
        self.btn_eliminar_asig_hr_amb = ttk.Button(self.btns_asignacion_hr_amb, text="Eliminar", command=self.llamar_eliminar_asignacion_hr_amb)
        self.btn_eliminar_asig_hr_amb.grid(row=0, column=3, padx=5)

        self.btn_limpiar_asig_hr_amb = ttk.Button(self.btns_asignacion_hr_amb, text="Limpiar Campos", command=self.limpiar_campos_asignacion_horas_ambiente)
        self.btn_limpiar_asig_hr_amb.grid(row=0, column=4, padx=5)
        # BOTONES CRUD ASIGNACION FACILITADOR HORARIO(CURSO)
        self.btns_asig_fh = ttk.Frame(self.tab4f)
        self.btns_asig_fh.grid(row=4, column=0, padx=15, pady=15, sticky="nsew")
        self.btn_crear_asig_fh = ttk.Button(self.btns_asig_fh, text="Crear", command=self.llamar_crear_asignacion_facilitador_horario)
        self.btn_crear_asig_fh.grid(row=0, column=0, padx=5)
        self.btn_buscar_asig_fh = ttk.Button(self.btns_asig_fh, text="Buscar", command= self.llamar_buscar_asignacion_facilitador_horario)
        self.btn_buscar_asig_fh.grid(row=0, column=1, padx=5)

        self.btn_eliminar_asig_fh = ttk.Button(self.btns_asig_fh, text="Eliminar", command=self.llamar_eliminar_asignacion_facilitador_horario)
        self.btn_eliminar_asig_fh.grid(row=0, column=2, padx=5)

        self.btn_limpiar_asig_fh = ttk.Button(self.btns_asig_fh, text="Limpiar Campos", command=self.limpiar_campos_asignacion_fa_curso)
        self.btn_limpiar_asig_fh.grid(row=0, column=3, padx=5)
# #                                            BOTONTES CRUD FACILITADOR
        self.btns_facilitador = ttk.Frame(self.label_entry_frame_f)
        self.btns_facilitador.grid(row=15, column=0)
        self.btn_crar_f = ttk.Button(self.btns_facilitador, text="Crear", command=self.llamar_crear_facilitador)
        self.btn_crar_f.grid(row=0, column=0) 
        self.btn_buscar_f = ttk.Button(self.btns_facilitador, text="Buscar", command=self.llamar_buscar_facilitador_por_cedula)
        self.btn_buscar_f.grid(row=0, column=1, padx=5)
        self.btn_actualizar_f = ttk.Button(self.btns_facilitador, text="Actualizar", command=self.llamar_actualizar_facilitador)
        self.btn_actualizar_f.grid(row=0, column=2, padx=5)
        self.btn_eliminar_f = ttk.Button(self.btns_facilitador, text="Eliminar",command=self.llamar_eliminar_facilitador)
        self.btn_eliminar_f.grid(row=0, column=3, padx=5)

        self.btn_limpiar_f = ttk.Button(self.btns_facilitador, text="Limpiar Campos",command=self.limpiar_campos_facilitador)
        self.btn_limpiar_f.grid(row=0, column=4, padx=5)


#                                           BOTONES CRUD PARTICIPANTE
        self.btns_participante=ttk.Frame(self.frame_participante)
        self.btns_participante.grid(row=7, column=0)
        self.btn_crear_pa= ttk.Button(self.btns_participante, text="Crear", command=self.llamar_crear_participante)
        self.btn_crear_pa.grid(row=0, column=0)
        self.btn_buscar_pa = ttk.Button(self.btns_participante, text="Buscar", command=self.llamar_buscar_participante_por_cedula)
        self.btn_buscar_pa.grid(row=0, column=1, padx=5)
        self.btn_actualizar_pa= ttk.Button(self.btns_participante, text="Actualizar", command=self.llamar_actualizar_participante)
        self.btn_actualizar_pa.grid(row=0, column=2, padx=5)
        self.btn_eliminar_pa= ttk.Button(self.btns_participante, text="Eliminar", command=self.llamar_eliminar_participante)
        self.btn_eliminar_pa.grid(row=0, column=5, padx=5)

        self.btn_limpiarc_pa= ttk.Button(self.btns_participante, text="Limpiar Campos", command=self.limpiar_campos_participante)
        self.btn_limpiarc_pa.grid(row=0, column=3, padx=5)

        self.btn_actualizarc_pa= ttk.Button(self.btns_participante, text="Actualizar", command=self.recargar_registro_participante)
        self.btn_actualizarc_pa.grid(row=0, column=4, padx=5)

        
        
#                                       BOTONES CRUD INSCRIPCION
        self.btns_incripcion=ttk.Frame(self.tab_inscripcion)
        self.btns_incripcion.grid(row=4, column=0)
        self.btn_crear_inscri= ttk.Button(self.btns_incripcion, text="Crear", command=self.llamar_crear_inscripcion)
        self.btn_crear_inscri.grid(row=0, column=0)
        self.btn_buscar_inscri = ttk.Button(self.btns_incripcion, text="Buscar", command=self.llamar_buscar_inscripcion)
        self.btn_buscar_inscri.grid(row=0, column=1, padx=5)


        self.btn_limpiarc_inscri= ttk.Button(self.btns_incripcion, text="Limpiar Campos", command=self.limpiar_campos_inscripcion)
        self.btn_limpiarc_inscri.grid(row=0, column=2, padx=5)

        self.btn_recargar_inscri= ttk.Button(self.btns_incripcion, text="Recargar", command=self.recarga_registros_inscripcion)
        self.btn_recargar_inscri.grid(row=0, column=3, padx=5)

        self.btn_validar = ttk.Button(self.tab_inscripcion, text="Validar/Desvalidar", command=self.cambiar_estado_validacion)
        self.btn_validar.grid(row=1, column=3, padx=5, pady=5)

        self.btn_eliminar_inscri= ttk.Button(self.btns_incripcion, text="Eliminar", command=self.llamar_eliminar_inscripcion)
        self.btn_eliminar_inscri.grid(row=7, column=7, padx=5)

        #                   BOTONES CRUD PERIODO ACADEMICO
        self.btns_incripcion=ttk.Frame(self.periodo_label_entry_frame)
        self.btns_incripcion.grid(row=6, column=2)
        self.btn_crear_periodo_aca= ttk.Button(self.btns_incripcion, text="Crear", command=self.llamar_crear_periodo_aca)
        self.btn_crear_periodo_aca.grid(row=0, column=0)
        self.btn_buscar_periodo_aca = ttk.Button(self.btns_incripcion, text="Buscar", command=self.llamar_buscar_inscripcion_periodo_por_nombre)
        self.btn_buscar_periodo_aca.grid(row=0, column=1, padx=5)
        self.btn_actualizar_periodo_aca= ttk.Button(self.btns_incripcion, text="Actualizar", command=self.llamar_actualizar_inscripcion_periodo)
        self.btn_actualizar_periodo_aca.grid(row=0, column=2, padx=5)
        self.btn_eliminar_periodo_aca= ttk.Button(self.btns_incripcion, text="Eliminar", command=self.llamar_eliminar_inscripcion_periodo)
        self.btn_eliminar_periodo_aca.grid(row=0, column=3, padx=5)

        self.btn_limpiarc_periodo_aca= ttk.Button(self.btns_incripcion, text="Limpiar Campos", command=self.limpiar_campos_periodo)
        self.btn_limpiarc_periodo_aca.grid(row=0, column=4, padx=5)
        #               CRUD PRESELECCION
        self.btns_incripcion=ttk.Frame(self.label_entry_frame_pre)
        self.btns_incripcion.grid(row=7, column=0)
        self.btn_crear_preelccion= ttk.Button(self.btns_incripcion, text="Crear", command=self.llamar_crear_preseleccion)
        self.btn_crear_preelccion.grid(row=0, column=0)
        self.btn_buscar_preelccion = ttk.Button(self.btns_incripcion, text="Buscar", command=self.llamar_buscar_preesleccion_curso_por_cedula)
        self.btn_buscar_preelccion.grid(row=0, column=1, padx=5)
        self.btn_actualizar_preelccion= ttk.Button(self.btns_incripcion, text="Actualizar", command=self.llamar_actualizar_preseleccion)
        self.btn_actualizar_preelccion.grid(row=0, column=2, padx=5)
        self.btn_eliminar_preelccion= ttk.Button(self.btns_incripcion, text="Eliminar", command=self.llamar_eliminar_preseleccion)
        self.btn_eliminar_preelccion.grid(row=0, column=3, padx=5)

        self.btn_limpiarc_preelccion= ttk.Button(self.btns_incripcion, text="Limpiar Campos", command=self.limpiar_campos_preseleccion)
        self.btn_limpiarc_preelccion.grid(row=0, column=4, padx=5)

        #               CRUD PERIODO DE PRESELECCION
        self.btns_incripcion=ttk.Frame(self.tab_periodo_pre)
        self.btns_incripcion.grid(row=5, column=2)
        self.btn_crear_preelccion= ttk.Button(self.btns_incripcion, text="Crear", command=self.llamar_crear_periodo_preseleccion)
        self.btn_crear_preelccion.grid(row=0, column=0)
      

        self.btn_limpiarc_preelccion= ttk.Button(self.btns_incripcion, text="Limpiar Campos", command=self.limpiar_campos_periodo_preseleccion)
        self.btn_limpiarc_preelccion.grid(row=0, column=1, padx=5)

#               REPORTES

        self.btn_reporte_general= ttk.Button(self.label_reporte_i,text="Reportes Total", command=self.llamar_generar_reporte_inscripciones_general)
        self.btn_reporte_general.grid(row=2, column=0)
        self.btn_reporte_individual= ttk.Button(self.label_reporte_i, text="Participante Individual", command=self.llamar_generar_reporte_inscripcion_individual)
        self.btn_reporte_individual.grid(row=0, column=0, padx=5)

        self.btn_reporte_preseleccion = ttk.Button(self.label_reporte_i, text="Reportes Preselección", command=self.llamar_generar_reporte_preseleccion)
        self.btn_reporte_preseleccion.grid(row=5, column=0, padx=5)
        self.btn_reporte_participantes = ttk.Button(self.label_reporte_i, text="Ficha de Participantes", command=self.llamar_generar_reporte_participantes)
        self.btn_reporte_participantes.grid(row=1, column=0, padx=5)
        self.btn_reporte_participantes = ttk.Button(self.label_reporte_i, text="Facilitador Individual")
        self.btn_reporte_participantes.grid(row=3, column=0, padx=5)
        self.btn_reporte_participantes = ttk.Button(self.label_reporte_i, text="Facilitador Total")
        self.btn_reporte_participantes.grid(row=4, column=0, padx=5)



    
#                       CARGAR DATOS EN TREEVIEW
    def mostrar_horas_en_treeview(self):
        mostrar_horas_en_treeview(self)

    def mostrar_ambiente_en_treeview(self):
        mostrar_ambiente_en_treeview(self)

    def mostrar_asignacion_hr_amb_en_treeview(self):
        mostrar_asignacion_hr_amb_en_treeview(self)



    def mostrar_asig_faci_hora_treeview(self):
        mostrar_asig_faci_hora_treeview(self)
    
    def mostrar_facilitador_treeview(self):
        mostrar_facilitador_treeview(self)

    def mostrar_pensum_en_treeview(self):
        mostrar_pensum_en_treeview(self)

    def mostrar_participante_treeview(self):
        mostrar_participante_treeview(self)    
    
    def mostrar_inscripcion_treeview(self):
        mostrar_inscripcion_treeview(self)

    def mostrar_preseleccion_treeview(self):
        mostrar_preseleccion_treeview(self)

    def mostrar_periodo_pre_treeview(self):
        mostrar_periodo_pre_treeview(self)

    def mostrar_periodo_academico_treeview(self):
        mostrar_periodo_academico_treeview(self)
    
#                       LLAMAR FUNCIONES CREAR REGISTRO

    def llamar_crear_horas(self):
        llamar_crear_horas(self)

    def llamar_crear_ambiente(self):
        llamar_crear_ambiente(self)

    def llamar_crear_asignacion_hr_amb(self):
        llamar_crear_asignacion_hr_amb(self)

    def llamar_crear_facilitador(self):
        llamar_crear_facilitador(self)

    def llamar_crear_asignacion_facilitador_horario(self):
        llamar_crear_asignacion_facilitador_horario(self)

    def llamar_crear_pensum(self):
        llamar_crear_pensum(self)

    def llamar_crear_participante(self):
        llamar_crear_participante(self)

    def llamar_crear_inscripcion(self):
        llamar_crear_inscripcion(self)

    def llamar_crear_periodo_aca(self):
        llamar_crear_periodo_aca(self)

    def llamar_crear_preseleccion(self):
        llamar_crear_preseleccion(self)

    def llamar_crear_periodo_preseleccion(self):
        llamar_crear_periodo_preseleccion(self)

        # REPORTES  DE PDF
    
    
    def llamar_generar_reporte_inscripciones_general(self):
        try:
            generar_reporte_inscripciones_general()
            messagebox.showinfo("Éxito", "Reporte general generado con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al generar el reporte general: {e}")


    def llamar_generar_reporte_inscripcion_individual(self):
        try:
            cedula_participante = self.cedulap_cuadro_var.get()  # Obtiene la cédula como texto
            nombre_inscripcion_periodo = self.nombre_periodo_cuadro_var.get()  # Obtiene el nombre del periodo como texto

            if cedula_participante and nombre_inscripcion_periodo:
                generar_reporte_inscripcion_individual(cedula_participante, nombre_inscripcion_periodo)
            else:
                messagebox.showwarning("Advertencia", "Por favor, introduce una cédula válida y un nombre de periodo.")
        except ValueError:
            messagebox.showwarning("Advertencia", "La cédula debe ser un número entero.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al generar el reporte individual: {e}")

    def llamar_generar_reporte_preseleccion(self):
        try:
            # Obtén los datos antes de llamar a la función de generar el reporte
            datos = obtener_datos_preseleccion()
            nombre_archivo_base = "reporte_preseleccion"  # Define el nombre del archivo (sin .pdf aquí)

            # Llama a la función con los argumentos requeridos
            ruta_archivo = generar_reporte_preseleccion_pdf(datos, nombre_archivo_base)
            if ruta_archivo:
                messagebox.showinfo("Éxito", "Reporte general generado con éxito.")
                abrir_pdf(ruta_archivo)  # Opcional: abrir el PDF después de generarlo
            else:
                messagebox.showerror("Error", "No se pudo generar el reporte PDF.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al generar el reporte general: {e}")

    def llamar_generar_reporte_participantes(self):
        try:
            generar_reporte_participantes()
            messagebox.showinfo("Éxito", "Reporte de participantes generado con éxito.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al generar el reporte de participantes: {e}")



   
#               BUSCAR REGISTROS
    def llamar_buscar_ambiente_por_nombre(self):
        llamar_buscar_ambiente_por_nombre(self)

    def llamar_buscar_facilitador_por_cedula(self):
        llamar_buscar_facilitador_por_cedula(self)

    def llamar_buscar_participante_por_cedula(self):
        llamar_buscar_participante_por_cedula(self)

    def llamar_buscar_hora(self):
        llamar_buscar_hora(self)

    def llamar_buscar_ambiente(self):
        llamar_crear_ambiente(self)

    def llamar_buscar_asignacion_hr_amb_por_id(self):
        llamar_buscar_asignacion_hr_amb_por_id(self)


    def llamar_buscar_pensum_por_codigo(self):
        llamar_buscar_pensum_por_codigo(self)

    def llamar_buscar_asignacion_facilitador_horario(self):
        llamar_buscar_asignacion_facilitador_horario(self)

    def llamar_buscar_participante_por_cedula(self):
        llamar_buscar_participante_por_cedula(self)

    def llamar_buscar_inscripcion_periodo_por_nombre(self):
        llamar_buscar_inscripcion_periodo_por_nombre(self)

    def llamar_buscar_preesleccion_curso_por_cedula(self):
        llamar_buscar_preesleccion_curso_por_cedula(self)  # Llamar a la función de búsqueda

    def llamar_buscar_inscripcion(self):
        llamar_buscar_inscripcion(self)

    #                       VALIDACION DE INSCRIPCION
    def cambiar_estado_validacion(self):
        selected_item = self.treeview_inscripcion.selection()
        if selected_item:
            values = self.treeview_inscripcion.item(selected_item, "values")
            validado = int(values[-1])  # Último valor (Validado)
            
            # Cambiar el estado de validación
            nuevo_estado = 1 if validado == 0 else 0
            new_values = values[:-1] + (nuevo_estado,)
            
            # Actualizar el registro en el Treeview
            self.treeview_inscripcion.item(selected_item, values=new_values)

            # Actualizar en la base de datos
            id_inscripcion = values[0]  # Asegúrate de que este sea el ID correcto
            actualizar_validacion_en_bd(id_inscripcion, nuevo_estado)
#               PARA NAVEGAR ENTRE BOTONES PENSUM, HORARIO, FACILITADOR

    def inicializar_grid(self):
        self.frame_pensum.grid(row=0, column=0, sticky="nsew")
        self.frame_horario.grid(row=0, column=0, sticky="nsew")
        self.frame_facilitador.grid(row=0, column=0, sticky="nsew")
        self.frame_participante.grid(row=0, column=0, sticky="nsew")
        self.frame_inscripcion.grid(row=0, column=0, sticky="nsew")
        self.frame_asignaciones.grid(row=0, column=0, sticky="nsew")

    def ocultar_frames(self):
        self.frame_pensum.grid_remove()
        self.frame_horario.grid_remove()
        self.frame_facilitador.grid_remove()
        self.frame_participante.grid_remove()
        self.frame_inscripcion.grid_remove()
        self.frame_asignaciones.grid_remove()

    def mostrar_pensum(self):
        self.ocultar_frames()
        self.frame_pensum.grid()

    def mostrar_horario(self):
        self.ocultar_frames()
        self.frame_horario.grid()

    def mostrar_facilitador(self):
        self.ocultar_frames()
        self.frame_facilitador.grid()

    def mostrar_participante(self):
        self.ocultar_frames()
        self.frame_participante.grid()

    def mostrar_inscripcion(self):
        self.ocultar_frames()
        self.frame_inscripcion.grid()

    def mostrar_asignaciones(self):
        self.ocultar_frames()
        self.frame_asignaciones.grid()

    def actualizar_codigos(self, event):
        """Actualiza los códigos disponibles según la mención seleccionada."""
        # Obtener la mención seleccionada
        mencion_seleccionada = self.mencion_cuadro.get()
        
        # Obtener el diccionario de códigos correspondiente a la mención seleccionada
        diccionario = mencion_dict.get(mencion_seleccionada, {})
        
        # Limpiar los valores del Combobox de códigos
        self.codigo_cuadro.set("")  # Limpia la selección actual
        self.codigo_cuadro['values'] = []  # Limpia los valores previos
        
        # Actualiza el Combobox de códigos con los valores del diccionario seleccionado
        self.codigo_cuadro['values'] = list(diccionario.keys())


    def mostrar_curso(self, event):
        """Muestra el curso, créditos y ciclo cuando se selecciona un código."""
        try:
            codigo = int(self.codigo_cuadro_var.get())
        except ValueError:
            # Maneja el caso en el que el valor no es un número
            self.curso_cuadro_var.set("")
            self.creditos_cuadro_var.set("")
            self.ciclo_cuadro_var.set("")
            return

        # Obtener el diccionario correcto según la mención seleccionada
        mencion_seleccionada = self.mencion_cuadro.get()
        diccionario = mencion_dict.get(mencion_seleccionada, {})

        if codigo in diccionario:
            valores = diccionario[codigo]
            # Verificar y asignar los valores según su cantidad
            curso = valores[0] if len(valores) > 0 else ""
            creditos = valores[1] if len(valores) > 1 else ""
            ciclo = valores[2] if len(valores) > 2 else ""

            self.curso_cuadro_var.set(curso)
            self.creditos_cuadro_var.set(creditos)
            self.ciclo_cuadro_var.set(ciclo)
        else:
            # Limpia los campos si no se encuentra el código
            self.curso_cuadro_var.set("")
            self.creditos_cuadro_var.set("")
            self.ciclo_cuadro_var.set("")



    def limpiar_campos(self):
        self.hora_i_cuadro_var.set("")
        self.hora_f_cuadro_var.set("")

        self.carrera_cuadro_var.set("")
        self.mencion_cuadro_var.set("")
        self.codigo_cuadro_var.set(0)  # IntVar
        self.curso_cuadro_var.set("")
        self.creditos_cuadro_var.set(0)  # IntVar
        self.ciclo_cuadro_var.set("")
        self.cupos_cuadro_var.set(0)  # IntVar

        self.dia_cuadro_var.set("")
        self.ambiente_cuadro_var.set("")
        self.seccion_cuadro_var.set("")
        self.idhoras_cuadro_var.set(0)  # IntVar
        self.id_ambiente_cuadro_var.set(0)  # IntVar
        self.cedulaf_cuadro_var.set("")
        self.nombresf_cuadro_var.set("")
        self.apellidosf_cuadro_var.set("")
        self.horaclasef_cuadro_var.set("")
        self.id_horario_cuadro_var.set(0)  # IntVar
        self.hi_horario_cuadro_var.set("")
        self.hf_horario_cuadro_var.set("")
        self.ced_horario_cuadro_var.set(0)  # IntVar
        self.idho_asigfa_cuadro_var.set(0)  # IntVar
        self.asig_cedulaf_cuadro_var.set(0)  # IntVar
        self.ced_asigfaho_cuadro_var.set(0)  # IntVar
        self.idhora_asig_asif_cuadro_var.set(0)  # IntVar
        self.idfa_asigfaho_cuadro_var.set(0)  # IntVar
        self.idhora_horario_cuadro_var.set(0)  # IntVar
        self.id_asighramb_asigfaho_cuadro_var.set(0)  # IntVar
        self.cedulap_cuadro_var.set(0)  # IntVar
        self.nombresp_cuadro_var.set("")
        self.apellidosp_cuadro_var.set("")
        self.total_cre_par_cuadro_var.set(0)  # IntVar
        self.total_cur_par_cuadro_var.set(0)  # IntVar
        self.id_asi_faho_inscri_cuadro_var.set(0)  # IntVar
        self.ced_par_inscri_cuadro_var.set(0)  # IntVar
        self.id_periodo_inscri_cuadro_var.set("")
        self.codigo_asig_cuadro_var.set(0)  # IntVar
        self.nombre_periodo_cuadro_var.set("")
        self.fechai_periodo_cuadro_var.set("")
        self.fechaf_periodo_cuadro_var.set("")
        self.preseleccion_ced_par_cuadro_var.set(0)  # IntVar
        self.preseleccion_id_peri_cuadro_var.set(0)  # IntVar
        self.preseleccion_pensum_cuadro_var.set(0)  # IntVar
        self.pre_fechaf_cuadro_var.set("")
        self.pre_fechai_cuadro_var.set("")

        self.sexop_var.set("")
        self.edadp_var.set(0)  # IntVar
        self.telefonop_var.set("")
        self.emailp_var.set("")
        self.edop_var.set("")
        self.municipiop_var.set("")
        self.parroquiap_var.set("")
        self.discapacidadp_var.set("")
        self.grupo_in_p_var.set("")
        self.programap_var.set("")
        self.sistemap_var.set("")



    def limpiar_campos_pensum(self):
        # Limpiar campos relacionados con Pensum
        self.carrera_cuadro_var.set("")  # StringVar
        self.mencion_cuadro_var.set("")  # StringVar
        self.codigo_cuadro_var.set(0)  # IntVar
        self.curso_cuadro_var.set("")  # StringVar
        self.creditos_cuadro_var.set(0)  # IntVar
        self.ciclo_cuadro_var.set("")  # StringVar
        self.cupos_cuadro_var.set(0)  # IntVar

    def limpiar_campos_preseleccion(self):
        # Limpiar campos relacionados con Preselección
        self.preseleccion_ced_par_cuadro_var.set(0)  # IntVar
        self.preseleccion_id_peri_cuadro_var.set(0)  # IntVar
        self.preseleccion_pensum_cuadro_var.set("")  # StringVar
        
    def limpiar_campos_periodo_preseleccion(self):
    # Limpiar campos relacionados con Periodo de Preselección
        self.pre_fechai_cuadro_var.set("")
        self.pre_fechaf_cuadro_var.set("")

    def limpiar_campos_horas(self):
        # Limpiar campos relacionados con Horas
        self.idh_cuadro_var.set(0)  # IntVar
        self.hora_i_cuadro_var.set("")  # StringVar
        self.hora_f_cuadro_var.set("")  # StringVar

    def limpiar_campos_ambiente(self):
        # Limpiar campos relacionados con Ambiente
        self.idamb_cuadro_var.set(0)  # IntVar
        self.ambiente_cuadro_var.set("")  # StringVar
        self.seccion_cuadro_var.set("")  # StringVar
        self.dia_cuadro_var.set("")  # StringVar

    def limpiar_campos_asignacion_horas_ambiente(self):
        # Limpiar campos relacionados con Asignación Horas Ambiente
        self.idhramb_cuadro_var.set(0)  # IntVar
        self.idhoras_cuadro_var.set(0)  # IntVar
        self.id_ambiente_cuadro_var.set(0)  # IntVar

    def limpiar_campos_facilitador(self):
        # Limpiar campos relacionados con Facilitador
        self.cedulaf_cuadro_var.set("")  # StringVar
        self.nombresf_cuadro_var.set("")  # StringVar
        self.apellidosf_cuadro_var.set("")  # StringVar
        self.horaclasef_cuadro_var.set("")  # StringVar

    def limpiar_campos_asignacion_fa_curso(self):
        # Limpiar campos relacionados con Asignación Facilitador Curso
        self.id_asigfa_cuadro_var.set(0)  # IntVar
        self.ced_asigfaho_cuadro_var.set(0)  # IntVar
        self.codigo_asig_cuadro_var.set(0)  # IntVar
        self.id_asighramb_asigfaho_cuadro_var.set(0)  # IntVar

    def limpiar_campos_participante(self):
        # Limpiar campos relacionados con Participante
        self.cedulap_cuadro_var.set(0)  # IntVar
        self.nombresp_cuadro_var.set("")  # StringVar
        self.apellidosp_cuadro_var.set("")  # StringVar
        self.sexop_var.set("")  # StringVar
        self.edadp_var.set(0)  # IntVar
        self.telefonop_var.set("")  # StringVar
        self.emailp_var.set("")  # StringVar
        self.edop_var.set("")  # StringVar
        self.municipiop_var.set("")  # StringVar
        self.parroquiap_var.set("")  # StringVar
        self.discapacidadp_var.set("")  # StringVar
        self.grupo_in_p_var.set("")  # StringVar
        self.programap_var.set("")  # StringVar
        self.sistemap_var.set("")  # StringVar

    def limpiar_campos_inscripcion(self):
        # Limpiar campos relacionados con Inscripción
        self.ced_par_inscri_cuadro_var.set(0)  # IntVar
        self.id_asi_faho_inscri_cuadro_var.set(0)  # IntVar
        self.id_periodo_inscri_cuadro_var.set("")  # StringVar

    def limpiar_campos_periodo(self):
        # Limpiar campos relacionados con Periodo Académico
        self.nombre_periodo_cuadro_var.set("")  # StringVar
        self.fechai_periodo_cuadro_var.set("")  # StringVar
        self.fechaf_periodo_cuadro_var.set("")  # StringVar



#                       ACTUALIZAR DATOS
    def llamar_actualizar_facilitador(self):
        llamar_actualizar_facilitador(self)

    def llamar_actualizar_hora(self):
        llamar_actualizar_hora(self)

    def llamar_actualizar_ambiente(self):
        llamar_actualizar_ambiente(self)

    def llamar_actualizar_pensum(self):
        llamar_actualizar_pensum(self)

    def llamar_actualizar_asignacion_hr_amb(self):
        llamar_actualizar_asignacion_hr_amb(self)

    def llamar_actualizar_participante(self):
        llamar_actualizar_participante(self)  # Llama a la función para actualizar el participante

    def llamar_actualizar_inscripcion_periodo(self):
        llamar_actualizar_fechas_inscripcion_periodo(self)  # Llamar a la función de actualización

    def llamar_actualizar_preseleccion(self):
        llamar_actualizar_preseleccion(self)

#                     ELIMINAR DATOS

    def llamar_eliminar_facilitador(self):
        llamar_eliminar_facilitador(self)

    def llamar_eliminar_hora(self):
        llamar_eliminar_hora(self)

    def llamar_eliminar_ambiente(self):
        llamar_eliminar_ambiente(self)

    def llamar_eliminar_pensum(self):
        llamar_eliminar_pensum(self)

    def llamar_eliminar_asignacion_facilitador_horario(self):
        llamar_eliminar_asignacion_facilitador_horario(self)

    def llamar_eliminar_asignacion_hr_amb(self):
        llamar_eliminar_asignacion_hr_amb_por_id(self)

    def llamar_eliminar_participante(self):
        llamar_eliminar_participante(self)

    def llamar_eliminar_inscripcion_periodo(self):
        llamar_eliminar_inscripcion_periodo(self)  # Llamar a la función de eliminación

    def llamar_eliminar_preseleccion(self):
        llamar_eliminar_preseleccion(self)


    def llamar_eliminar_inscripcion(self):
        llamar_eliminar_inscripcion(self)


    #LIMPIAR DATOS

    def limpiar_inscripcion_treeview(self):
        # Limpiar el Treeview antes de insertar nuevos datos
        for item in self.treeview_inscripcion.get_children():
            self.treeview_inscripcion.delete(item)

    def limpiar_participante_treeview(self):
        # Limpiar el Treeview antes de insertar nuevos datos
        for item in self.treeview_participante.get_children():
            self.treeview_participante.delete(item)


    def recarga_registros_inscripcion(self):
        # Limpiar el Treeview
        self.limpiar_inscripcion_treeview()
        
        # Volver a mostrar todos los registros
        self.mostrar_inscripcion_treeview()

    def recargar_registro_participante(self):
        
        self.mostrar_participante_treeview()


def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal al principio
    VentanaPresentacion(root)  # Crea la ventana de presentación
    app = Ventana(root)  # Inicializa la ventana principal
    root.mainloop()  # Inicia el bucle de eventos

if __name__ == "__main__":
    main()

    
