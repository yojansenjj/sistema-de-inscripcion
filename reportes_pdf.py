# Importaciones de la biblioteca estándar
import datetime
import os
import subprocess
from tkinter import messagebox

# Importaciones de terceros
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle
)

# Importaciones locales
from conexion_db_01 import *


# Asegúrate de tener las otras funciones definidas aquí.

def truncar_texto(texto, max_longitud=15):
    return (texto[:max_longitud] + '...') if len(texto) > max_longitud else texto

def generar_reporte_general_pdf(datos):
    try:
        # Definir la ruta y el nombre del archivo
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Documents")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"reporte_general_inscripciones_{timestamp}.pdf"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Cambiar a A3 para más espacio
        doc = SimpleDocTemplate(
            ruta_archivo, 
            pagesize=landscape(A3),  # Usando A3 aquí
            rightMargin=5, leftMargin=5,
            topMargin=10, bottomMargin=10
        )
        elements = []

        styles = getSampleStyleSheet()
        estilo_titulo = styles['Heading1']
        estilo_titulo.alignment = 1  # Centrar el título
        title = Paragraph("Reporte General de Inscripciones", estilo_titulo)
        elements.append(title)
        elements.append(Spacer(1, 12))

        # Encabezados abreviados
        encabezados = [
            "Alumno", "Nombre", "Apellido", "Facilitador", "Nombre", 
            "Apellido", "Incio", "Fin", "Amb", 
            "Día", "Secc", "Codigo", "Curso", "Ciclo", 
            "Periodo"
        ]

        encabezados_rotados = [
            Paragraph(f'<font size="12"><b>{text}</b></font>', styles['Normal'])  # Ajustar tamaño de fuente
            for text in encabezados
        ]

        # Construir los datos de la tabla
        tabla_datos = [encabezados_rotados]
        for registro in datos:
            fila = [
                Paragraph(f'<font size="12">{str(registro[0])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[1]))}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[2]))}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[3])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[4]))}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[5]))}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[6])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[7])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[8])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[9])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[10])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[11])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[12]))}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{str(registro[13])}</font>', styles['Normal']),
                Paragraph(f'<font size="12">{truncar_texto(str(registro[14]))}</font>', styles['Normal'])
            ]
            tabla_datos.append(fila)

        # Definir el ancho de las columnas y la altura de las filas
        ancho_columnas = [
            1.1 * inch,  # Céd.
            1.2 * inch,  # Nom.
            1.2 * inch,  # Ape.
            1.1 * inch,  # Céd. Fac.
            1.2 * inch,  # Nom. Fac.
            1.2 * inch,  # Ape. Fac.
            0.9 * inch,  # H. Init.
            0.9 * inch,  # H. Final
            0.7 * inch,  # Amb.
            0.9 * inch,  # Día
            0.7 * inch,  # Secc.
            0.8 * inch,  # Cod. Pensum
            1.3 * inch,  # Curso
            0.9 * inch,  # Ciclo
            1.1 * inch   # Nom. Periodo
        ]

        # Crear la tabla con la opción repeatRows para repetir encabezados
        #tabla = Table(tabla_datos, colWidths=ancho_columnas, repeatRows=1)
        altura_fila = 0.9 * inch  # Ajusta este valor según tus necesidades

# Crear la tabla con la altura de las celdas ajustada
        tabla = Table(tabla_datos, colWidths=ancho_columnas, repeatRows=10, rowHeights=[altura_fila] * len(tabla_datos))


        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),  # Ajustar tamaño de letra
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        # Alternar colores de fondo para filas
        for i in range(1, len(tabla_datos)):
            bg_color = colors.whitesmoke if i % 2 == 0 else colors.white
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, i), (-1, i), bg_color)
            ]))

        # Agregar la tabla al documento
        elements.append(tabla)

        # Definir un footer opcional con el número de página
        def agregar_footer(canvas, doc):
            canvas.saveState()
            footer_text = f"Pág. {doc.page}"
            canvas.setFont('Helvetica', 8)  # Tamaño de letra del footer
            canvas.drawString(10, 10, footer_text)
            canvas.restoreState()

        # Construir el documento con el footer
        doc.build(elements, onFirstPage=agregar_footer, onLaterPages=agregar_footer)
        
        return ruta_archivo
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el PDF: {e}")
        return None

    



# La misma corrección debe aplicarse a la función generar_reporte_individual_pdf.
def truncar_texto(texto, max_longitud=15):
    return (texto[:max_longitud] + '...') if len(texto) > max_longitud else texto

def generar_reporte_individual_pdf(registros, cedula_participante):
    try:
        # Verificar que haya registros para generar el reporte
        if not registros:
            messagebox.showinfo("Información", "No hay registros para generar el reporte.")
            return None

        # Definir la ruta y el nombre del archivo
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Documents")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"reporte_individual_{cedula_participante}_{timestamp}.pdf"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Cambiar a orientación horizontal (Landscape) para mayor ancho
        doc = SimpleDocTemplate(
            ruta_archivo, 
            pagesize=landscape(letter),  # Cambiado a Landscape
            rightMargin=10, leftMargin=10,
            topMargin=20, bottomMargin=20
        )
        elements = []

        styles = getSampleStyleSheet()

        # Crear un estilo de párrafo personalizado para el membrete con tamaño de letra 12
        style_membrete = ParagraphStyle(
            'Membrete',
            parent=styles['Title'],
            fontSize=12,
            alignment=1  # Centrar el texto
        )

        # Agregar título o membrete
        membrete = [
            Paragraph("REPÚBLICA BOLIVARIANA DE VENEZUELA", style_membrete),
            Paragraph("UNIVERSIDAD NACIONAL EXPERIMENTAL SIMÓN RODRÍGUEZ", style_membrete),
            Paragraph("DIRECCIÓN DE CONTROL DE ESTUDIOS", style_membrete),
            Paragraph("NÚCLEO VALLES DEL TUY", style_membrete),
            Paragraph("PLANILLA DE RENOVACIÓN O INSCRIPCIÓN DE CURSOS", style_membrete),
            Spacer(1, 12)
        ]
        elements.extend(membrete)

        # Crear un estilo para el título del participante
        style_titulo = ParagraphStyle(
            'TituloParticipante',
            parent=styles['Heading2'],
            fontSize=10,  # Reducido a 10
            alignment=1  # Centrado
        )

        # Crear un estilo para el contenido de la tabla
        style_contenido = ParagraphStyle(
            'Contenido',
            parent=styles['Normal'],
            fontSize=9,  # Reducido a 9
            alignment=1  # Centrado
        )

        # Agregar título del participante
        cedula = registros[0][0]
        nombre = registros[0][1]
        apellido = registros[0][2]
        programa = registros[0][3]

        title_text = f"Cédula: {cedula} - Participante: {nombre} {apellido} - Programa: {programa}"
        title = Paragraph(title_text, style_titulo)
        elements.append(title)
        elements.append(Spacer(1, 12))

        # Encabezados de la tabla
        encabezados = [
            "Nom. Facilitador", "Ape. Facilitador", "Hora Inicial", 
            "Hora Final", "Amb.", "Día", "Sección", "Cod. Pensum", 
            "Curso", "Ciclo", "Nom. Periodo"
        ]

        # Crear las filas de la tabla (Encabezado + Datos)
        tabla_datos = [
            [
                Paragraph(f'<b>{encabezado}</b>', style_contenido) 
                for encabezado in encabezados
            ]
        ]

        # Agregar cada registro como una fila en la tabla
        for registro in registros:
            datos_registro = [
                Paragraph(truncar_texto(str(registro[5]), 15), style_contenido),   # Nombre Facilitador
                Paragraph(truncar_texto(str(registro[6]), 15), style_contenido),   # Apellido Facilitador
                Paragraph(str(registro[7]), style_contenido),                      # Hora Inicial
                Paragraph(str(registro[8]), style_contenido),                      # Hora Final
                Paragraph(str(registro[9]), style_contenido),                      # Ambiente
                Paragraph(str(registro[10]), style_contenido),                     # Día
                Paragraph(str(registro[11]), style_contenido),                     # Sección
                Paragraph(str(registro[12]), style_contenido),                     # Código Pensum
                Paragraph(truncar_texto(str(registro[13]), 15), style_contenido),  # Curso
                Paragraph(str(registro[14]), style_contenido),                     # Ciclo
                Paragraph(truncar_texto(str(registro[15]), 15), style_contenido)   # Nombre Periodo
            ]
            tabla_datos.append(datos_registro)

        # Definir el ancho de las columnas ajustado para Landscape
        ancho_columnas = [
            0.9 * inch,  # Nom. Facilitador
            0.9 * inch,  # Ape. Facilitador
            0.8 * inch,  # Hora Inicial
            0.8 * inch,  # Hora Final
            0.8 * inch,  # Amb.
            0.6 * inch,  # Día
            0.8 * inch,  # Sección
            0.8 * inch,  # Cod. Pensum
            1.0 * inch,  # Curso
            0.8 * inch,  # Ciclo
            0.8 * inch   # Nom. Periodo
        ]

        # Crear la tabla
        tabla = Table(tabla_datos, colWidths=ancho_columnas, repeatRows=1)

        # Establecer estilos para la tabla
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),  # Reducido a 9
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        # Alternar colores de fondo para filas
        for i in range(1, len(tabla_datos)):
            bg_color = colors.whitesmoke if i % 2 == 0 else colors.white
            tabla.setStyle(TableStyle([
                ('BACKGROUND', (0, i), (-1, i), bg_color)
            ]))

        # Agregar la tabla al documento
        elements.append(tabla)
        elements.append(Spacer(1, 12))

        # Definir un footer opcional con el número de página
        def agregar_footer(canvas, doc):
            canvas.saveState()
            footer_text = f"Pág. {doc.page}"
            canvas.setFont('Helvetica', 8)  # Tamaño de letra del footer
            width, height = landscape(letter)  # Actualizado a Landscape
            canvas.drawString(width - 50, 10, footer_text)  # Posición ajustada al Landscape
            canvas.restoreState()

        # Crear un estilo para los títulos adicionales
        style_titulo_adicional = ParagraphStyle(
            'TituloAdicional',
            parent=styles['Heading2'],  # Puedes usar Heading2 o cualquier estilo que prefieras
            fontSize=12,  # Cambia el tamaño de letra aquí
            alignment=1  # Centrado
        )

        # Agregar títulos adicionales con total de cursos y créditos
        total_cursos = registros[0][16] if len(registros) > 0 else 0  # Suponiendo que total_cursos está en la posición 16
        total_creditos = registros[0][17] if len(registros) > 0 else 0  # Suponiendo que total_creditos está en la posición 17
        
        titulo_adicional_1 = Paragraph(f"TOTAL CURSOS: {total_cursos}", style_titulo_adicional)
        titulo_adicional_2 = Paragraph(f"TOTAL CRÉDITOS: {total_creditos}", style_titulo_adicional)
        
        elements.append(Spacer(1, 24))  # Espacio antes del título adicional
        elements.append(titulo_adicional_1)
        elements.append(titulo_adicional_2)

        # Construir el documento con el footer
        doc.build(elements, onFirstPage=agregar_footer, onLaterPages=agregar_footer)

        return ruta_archivo
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un error al generar el PDF: {e}")
        return

    


def abrir_pdf(ruta_archivo):
    try:
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_archivo)
        elif os.name == 'posix':  # Para macOS y Linux
            subprocess.call(('open', ruta_archivo) if sys.platform == 'darwin' else ('xdg-open', ruta_archivo))
    except Exception as e:
        print(f"Error al abrir el archivo PDF: {e}")




def generar_reporte_preseleccion_pdf(datos, nombre_archivo_base, tamaño_fuente=6, tamaño_fuente_encabezado=8):
    try:
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Documents")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{nombre_archivo_base}_{timestamp}.pdf"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Cambiar la orientación a landscape
        doc = SimpleDocTemplate(ruta_archivo, pagesize=landscape(letter),
                                rightMargin=10, leftMargin=10,
                                topMargin=20, bottomMargin=20)
        elements = []

        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title = Paragraph("Reporte de Preselección", title_style)
        elements.append(title)

        encabezados = [
            "Cédula", "Fecha de Inicio", "Fecha de Fin", "Código Pensum", "Curso"
        ]

        # Crear una fila de encabezados rotados
        encabezados_rotados = [Paragraph(f'<font size="{tamaño_fuente_encabezado}"><b>{text}</b></font>', 
                                         styles['Normal']) for text in encabezados]

        tabla_datos = [encabezados_rotados]
        for registro in datos:
            fila = [
                Paragraph(f'<font size="{tamaño_fuente}">{str(registro[0])}</font>', styles['Normal']), 
                Paragraph(f'<font size="{tamaño_fuente}">{str(registro[1])}</font>', styles['Normal']), 
                Paragraph(f'<font size="{tamaño_fuente}">{str(registro[2])}</font>', styles['Normal']), 
                Paragraph(f'<font size="{tamaño_fuente}">{str(registro[3])}</font>', styles['Normal']), 
                Paragraph(f'<font size="{tamaño_fuente}">{str(registro[4])}</font>', styles['Normal'])
            ]
            tabla_datos.append(fila)

        # Ajustar los anchos de las columnas
        ancho_columnas = [0.9 * inch, 1.0 * inch, 1.0 * inch, 0.9 * inch, 1.0 * inch]

        # Crear la tabla con anchos de columnas específicos
        tabla = Table(tabla_datos, colWidths=ancho_columnas)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), tamaño_fuente_encabezado),
            ('FONTSIZE', (0, 1), (-1, -1), tamaño_fuente),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(tabla)

        doc.build(elements)
        print(f"Reporte generado: {ruta_archivo}")
        return ruta_archivo

    except Exception as e:
        print(f"Error al generar el reporte PDF: {e}")
        return None

def abrir_pdf(ruta_archivo):
    try:
        if os.name == 'nt':  # Para Windows
            os.startfile(ruta_archivo)
        elif os.name == 'posix':  # Para macOS y Linux
            subprocess.call(('open', ruta_archivo) if sys.platform == 'darwin' else ('xdg-open', ruta_archivo))
    except Exception as e:
        print(f"Error al abrir el archivo PDF: {e}")

def generar_reporte_participante_pdf(datos, nombre_archivo_base, tamaño_fuente=14, tamaño_fuente_encabezado=14):
    try:
        # Definir la ruta y el nombre del archivo
        ruta_carpeta = os.path.join(os.path.expanduser("~"), "Documents")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{nombre_archivo_base}_{timestamp}.pdf"
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)

        # Crear el documento PDF
        doc = SimpleDocTemplate(ruta_archivo, pagesize=landscape(letter),
                                rightMargin=10, leftMargin=10,
                                topMargin=20, bottomMargin=20)
        elements = []

        # Título del reporte
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']

        # Encabezados de la tabla
        encabezados = [
            "Cédula", "Nombre", "Apellido", "Sexo", "Edad", 
            "Teléfono", "Correo", "Estado", "Municipio", 
            "Parroquia", "Discapacidad", "Grupo Indigena", "Programa", 
            "Total Cursos", "Total Créditos", "Sistema"
        ]

        # Validar que los datos tengan la misma cantidad de columnas que los encabezados
        if datos and len(datos[0]) != len(encabezados):
            raise ValueError(f"El número de columnas en los datos ({len(datos[0])}) no coincide con el número de encabezados ({len(encabezados)})")

        # Procesar cada registro de los datos
        for registro in datos:
            # Título para cada página con el número de cédula
            title = Paragraph(f"Reporte de Participante - Cédula: {registro[0]}", title_style)  # Aquí se usa el número de cédula
            elements.append(title)

            # Crear la tabla de datos para el participante
            tabla_datos = []

            for i in range(len(encabezados)):
                # Crear fila con el encabezado y su información
                encabezado_paragraph = Paragraph(f'<font size="{tamaño_fuente_encabezado}"><b>{encabezados[i]}</b></font>', styles['Normal'])
                info_paragraph = Paragraph(f'<font size="{tamaño_fuente}">{registro[i]}</font>', styles['Normal'])
                
                # Agregar a la tabla
                tabla_datos.append([encabezado_paragraph, info_paragraph])  # Cada fila tiene el encabezado y su dato

            # Crear la tabla con un tamaño un poco mayor
            tabla = Table(tabla_datos, colWidths=[2.5 * inch, 4 * inch])  # Ajustar el ancho de las columnas

            # Estilos de la tabla
            tabla.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), tamaño_fuente_encabezado),  # Tamaño de letra para encabezados
                ('FONTSIZE', (0, 1), (-1, -1), tamaño_fuente),  # Tamaño de letra para datos
                ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Rejilla en toda la tabla
                ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Sin color de fondo para encabezados
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Color de texto para encabezados
            ]))

            elements.append(tabla)
            elements.append(PageBreak())  # Agregar un salto de página después de cada participante

        # Generar el documento PDF
        doc.build(elements)
        print(f"Reporte generado: {ruta_archivo}")
        return ruta_archivo

    except Exception as e:
        print(f"Error al generar el reporte PDF: {e}")
        return None