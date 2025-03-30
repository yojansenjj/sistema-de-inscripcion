-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-10-2024 a las 23:41:50
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_inscripcion`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `ActualizarResumen` (IN `p_cedula_participante` INT, IN `p_nombre_inscripcion_periodo` VARCHAR(45))   BEGIN
    DECLARE total_cursos INT DEFAULT 0;
    DECLARE total_creditos DECIMAL(5,2) DEFAULT 0.00;

    -- Contar total de cursos de asignacion_facilitador_curso relacionados con la nueva inscripción
    SELECT COUNT(DISTINCT afc.codigo_pensum) INTO total_cursos
    FROM inscripcion i
    JOIN asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
    WHERE i.cedula_participante = p_cedula_participante
    AND i.nombre_inscripcion_periodo = p_nombre_inscripcion_periodo;

    -- Sumar total de créditos de pensum para los cursos
    SELECT COALESCE(SUM(p.credito), 0) INTO total_creditos
    FROM inscripcion i
    JOIN asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
    JOIN pensum p ON afc.codigo_pensum = p.codigo
    WHERE i.cedula_participante = p_cedula_participante
    AND i.nombre_inscripcion_periodo = p_nombre_inscripcion_periodo;

    -- Insertar o actualizar en resumen_participante_periodo
    INSERT INTO resumen_participante_periodo (cedula_participante, nombre_inscripcion_periodo, total_cursos, total_creditos)
    VALUES (p_cedula_participante, p_nombre_inscripcion_periodo, total_cursos, total_creditos)
    ON DUPLICATE KEY UPDATE
        total_cursos = VALUES(total_cursos),
        total_creditos = VALUES(total_creditos);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `ActualizarResumenAlEliminar` (IN `p_cedula_participante` INT, IN `p_nombre_inscripcion_periodo` VARCHAR(45))   BEGIN
    DECLARE total_cursos INT DEFAULT 0;
    DECLARE total_creditos DECIMAL(5,2) DEFAULT 0.00;

    -- Contar total de cursos de asignacion_facilitador_curso relacionados con la inscripción después de la eliminación
    SELECT COUNT(DISTINCT afc.codigo_pensum) INTO total_cursos
    FROM inscripcion i
    JOIN asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
    WHERE i.cedula_participante = p_cedula_participante
    AND i.nombre_inscripcion_periodo = p_nombre_inscripcion_periodo;

    -- Sumar total de créditos de pensum para los cursos después de la eliminación
    SELECT COALESCE(SUM(p.credito), 0) INTO total_creditos
    FROM inscripcion i
    JOIN asignacion_facilitador_curso afc ON i.id_asignacion_facilitador_curso = afc.id
    JOIN pensum p ON afc.codigo_pensum = p.codigo
    WHERE i.cedula_participante = p_cedula_participante
    AND i.nombre_inscripcion_periodo = p_nombre_inscripcion_periodo;

    -- Actualizar en resumen_participante_periodo restando los valores obtenidos
    UPDATE resumen_participante_periodo
    SET total_cursos = total_cursos,
        total_creditos = total_creditos
    WHERE cedula_participante = p_cedula_participante
    AND nombre_inscripcion_periodo = p_nombre_inscripcion_periodo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `asignar_cupos_para_periodo` (IN `nuevo_periodo` VARCHAR(45))   BEGIN
    -- Verificar si el período de inscripción existe
    IF NOT EXISTS (SELECT 1 FROM inscripcion_periodo WHERE nombre = nuevo_periodo) THEN
        SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'El período de inscripción no existe en inscripcion_periodo.';
    ELSE
        -- Insertar cupos asignados para cada pensum en el nuevo período, evitando duplicados
        INSERT INTO cupos_pensum_periodo (codigo_pensum, nombre_inscripcion_periodo, cupos_asignados)
        SELECT p.codigo, nuevo_periodo, p.cupos
        FROM pensum p
        WHERE NOT EXISTS (
            SELECT 1 
            FROM cupos_pensum_periodo cpp
            WHERE cpp.codigo_pensum = p.codigo
              AND cpp.nombre_inscripcion_periodo = nuevo_periodo
        );
    END IF;
END$$

--
-- Funciones
--
CREATE DEFINER=`root`@`localhost` FUNCTION `calcular_diferencia_horas` (`inicio` TIME, `fin` TIME) RETURNS DECIMAL(5,2)  BEGIN
    DECLARE diferencia DECIMAL(5,2);
    SET diferencia = TIME_TO_SEC(fin) - TIME_TO_SEC(inicio);
    IF diferencia < 0 THEN
        SET diferencia = diferencia + 86400; -- Añadir 24 horas en segundos
    END IF;
    RETURN diferencia / 3600; -- Convertir a horas
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ambiente`
--

CREATE TABLE `ambiente` (
  `id` int(11) NOT NULL,
  `ambiente` varchar(50) DEFAULT NULL,
  `seccion` varchar(50) DEFAULT NULL,
  `dia` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ambiente`
--

INSERT INTO `ambiente` (`id`, `ambiente`, `seccion`, `dia`) VALUES
(1, '1-A', 'A', 'MARTES'),
(2, '2-A', 'B', 'LUNES');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_facilitador_curso`
--

CREATE TABLE `asignacion_facilitador_curso` (
  `id` int(11) NOT NULL,
  `cedula_facilitador` int(11) DEFAULT NULL,
  `codigo_pensum` int(11) DEFAULT NULL,
  `id_asignacion_hr_amb` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `asignacion_facilitador_curso`
--
DELIMITER $$
CREATE TRIGGER `actualizar_horas_facilitador` AFTER INSERT ON `asignacion_facilitador_curso` FOR EACH ROW BEGIN
    DECLARE hora_inicio TIME;
    DECLARE hora_fin TIME;
    DECLARE total_horas DECIMAL(5,2);

    -- Obtener las horas de la tabla horas a través de la asignación de horario y ambiente
    SELECT h.hora_inicial, h.hora_final 
    INTO hora_inicio, hora_fin
    FROM asignacion_hr_amb ahr
    JOIN horas h ON ahr.id_hora = h.id
    WHERE ahr.id = NEW.id_asignacion_hr_amb;

    -- Verificar que las horas sean válidas
    IF hora_inicio IS NOT NULL AND hora_fin IS NOT NULL THEN
        -- Calcular la diferencia en horas entre la hora inicial y la hora final, redondear a múltiplos de 0.5
        SET total_horas = ROUND(TIME_TO_SEC(TIMEDIFF(hora_fin, hora_inicio)) / 3600 * 2, 0) / 2;

        -- Asegurarse de que total_horas no sea negativo
        IF total_horas > 0 THEN
            -- Actualizar las horas de clase del facilitador sumando las horas calculadas
            UPDATE facilitador
            SET horas_de_clase = horas_de_clase + total_horas
            WHERE cedula = NEW.cedula_facilitador;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: El tiempo total calculado no es válido (debe ser positivo).';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: No se pudieron obtener las horas inicial y final.';
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `restar_horas_clase` AFTER DELETE ON `asignacion_facilitador_curso` FOR EACH ROW BEGIN
    DECLARE hora_inicio TIME;
    DECLARE hora_fin TIME;
    DECLARE total_horas DECIMAL(5,2);

    -- Obtener las horas de la tabla horas a través de la asignación de horario y ambiente
    SELECT h.hora_inicial, h.hora_final 
    INTO hora_inicio, hora_fin
    FROM asignacion_hr_amb ahr
    JOIN horas h ON ahr.id_hora = h.id
    WHERE ahr.id = OLD.id_asignacion_hr_amb;

    -- Verificar que las horas sean válidas
    IF hora_inicio IS NOT NULL AND hora_fin IS NOT NULL THEN
        -- Calcular la diferencia en horas entre la hora inicial y la hora final, redondear a múltiplos de 0.5
        SET total_horas = ROUND(TIME_TO_SEC(TIMEDIFF(hora_fin, hora_inicio)) / 3600 * 2, 0) / 2;

        -- Asegurarse de que total_horas no sea negativo
        IF total_horas > 0 THEN
            -- Actualizar las horas de clase del facilitador restando las horas calculadas
            UPDATE facilitador
            SET horas_de_clase = horas_de_clase - total_horas
            WHERE cedula = OLD.cedula_facilitador;
        ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Error: El tiempo total calculado no es válido (debe ser positivo).';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: No se pudieron obtener las horas inicial y final.';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacion_hr_amb`
--

CREATE TABLE `asignacion_hr_amb` (
  `id` int(11) NOT NULL,
  `id_hora` int(11) DEFAULT NULL,
  `id_ambiente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facilitador`
--

CREATE TABLE `facilitador` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `horas_de_clase` decimal(5,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horas`
--

CREATE TABLE `horas` (
  `id` int(11) NOT NULL,
  `hora_inicial` time DEFAULT NULL,
  `hora_final` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `horas`
--
DELIMITER $$
CREATE TRIGGER `before_insert_horas` BEFORE INSERT ON `horas` FOR EACH ROW BEGIN
    DECLARE v_count INT;

    -- Verificar si el rango de horas ya existe
    SELECT COUNT(*)
    INTO v_count
    FROM horas
    WHERE hora_inicial = NEW.hora_inicial
      AND hora_final = NEW.hora_final;

    -- Si el rango de horas ya existe, lanzar un error
    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El rango de horas ya existe en la tabla horas.';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion`
--

CREATE TABLE `inscripcion` (
  `id` int(11) NOT NULL,
  `cedula_participante` int(11) NOT NULL,
  `id_asignacion_facilitador_curso` int(11) DEFAULT NULL,
  `nombre_inscripcion_periodo` varchar(45) NOT NULL,
  `validada` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Disparadores `inscripcion`
--
DELIMITER $$
CREATE TRIGGER `AfterInscripcionInsert` AFTER INSERT ON `inscripcion` FOR EACH ROW BEGIN
    CALL ActualizarResumen(NEW.cedula_participante, NEW.nombre_inscripcion_periodo);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trg_update_participante_after_delete_inscripcion` AFTER DELETE ON `inscripcion` FOR EACH ROW BEGIN
   DECLARE v_creditos INT;
   
   -- Obtener los créditos del curso del código pensum
   SELECT p.credito INTO v_creditos
   FROM pensum p
   INNER JOIN asignacion_facilitador_curso afc ON afc.codigo_pensum = p.codigo
   WHERE afc.id = OLD.id_asignacion_facilitador_curso;

   -- Actualizar el conteo de cursos y créditos del participante
   UPDATE participante
   SET cursos_g = cursos_g - 1,
       creditos_g = creditos_g - v_creditos
   WHERE cedula = OLD.cedula_participante;

END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trg_update_participante_after_inscripcion` AFTER INSERT ON `inscripcion` FOR EACH ROW BEGIN
   DECLARE v_creditos INT;
   
   -- Obtener los créditos del curso del código pensum
   SELECT p.credito INTO v_creditos
   FROM pensum p
   INNER JOIN asignacion_facilitador_curso afc ON afc.codigo_pensum = p.codigo
   WHERE afc.id = NEW.id_asignacion_facilitador_curso;
   
   -- Actualizar el conteo de cursos y créditos del participante
   UPDATE participante
   SET cursos_g = cursos_g + 1,
       creditos_g = creditos_g + v_creditos
   WHERE cedula = NEW.cedula_participante;
   
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trg_update_resumen_after_delete` AFTER DELETE ON `inscripcion` FOR EACH ROW BEGIN
    CALL ActualizarResumenAlEliminar(OLD.cedula_participante, OLD.nombre_inscripcion_periodo);
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `validar_fecha_inscripcion` BEFORE INSERT ON `inscripcion` FOR EACH ROW BEGIN
    DECLARE v_fecha_inicio DATE;
    DECLARE v_fecha_fin DATE;

    -- Obtener las fechas de inicio y fin del período de inscripción
    SELECT fecha_inicio, fecha_fin
    INTO v_fecha_inicio, v_fecha_fin
    FROM inscripcion_periodo
    WHERE nombre = NEW.nombre_inscripcion_periodo;

    -- Verificar si la fecha actual está dentro del período válido
    IF CURDATE() < v_fecha_inicio OR CURDATE() > v_fecha_fin THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La inscripción no puede realizarse fuera del período válido.';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripcion_periodo`
--

CREATE TABLE `inscripcion_periodo` (
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `nombre` varchar(45) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participante`
--

CREATE TABLE `participante` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `sexo` enum('M','F') NOT NULL,
  `edad` tinyint(3) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `municipio` varchar(45) NOT NULL,
  `parroquia` varchar(45) NOT NULL,
  `discapacidad` enum('sí','no') NOT NULL,
  `grupo_i` enum('sí','no') NOT NULL,
  `programa` varchar(45) NOT NULL,
  `sistema` varchar(5) NOT NULL,
  `cursos_g` smallint(5) UNSIGNED DEFAULT 0,
  `creditos_g` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pensum`
--

CREATE TABLE `pensum` (
  `codigo` int(11) NOT NULL,
  `curso` varchar(45) NOT NULL,
  `credito` int(11) NOT NULL,
  `ciclo` varchar(45) NOT NULL,
  `carrera` varchar(45) NOT NULL,
  `mencion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pensum`
--

INSERT INTO `pensum` (`codigo`, `curso`, `credito`, `ciclo`, `carrera`, `mencion`) VALUES
(31011, 'INICIACION UNIVERSITARIA', 2, 'INICIAL', 'Administarcion', 'Administración Introductorio'),
(31012, 'LENGUAJE Y COMUNICACION', 3, 'INICIAL', 'ADMINISTRACION', 'Introductorio');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preseleccion_curso`
--

CREATE TABLE `preseleccion_curso` (
  `id` int(11) NOT NULL,
  `cedula_participante` int(11) NOT NULL,
  `id_preseleccion_periodo` int(11) NOT NULL,
  `codigo_pensum` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preseleccion_periodo`
--

CREATE TABLE `preseleccion_periodo` (
  `id` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resumen_participante_periodo`
--

CREATE TABLE `resumen_participante_periodo` (
  `cedula_participante` int(11) NOT NULL,
  `nombre_inscripcion_periodo` varchar(50) NOT NULL,
  `total_cursos` int(11) DEFAULT 0,
  `total_creditos` decimal(5,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_ambiente` (`ambiente`);

--
-- Indices de la tabla `asignacion_facilitador_curso`
--
ALTER TABLE `asignacion_facilitador_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedula_facilitador` (`cedula_facilitador`),
  ADD KEY `codigo_pensum` (`codigo_pensum`),
  ADD KEY `id_asignacion_hr_amb` (`id_asignacion_hr_amb`);

--
-- Indices de la tabla `asignacion_hr_amb`
--
ALTER TABLE `asignacion_hr_amb`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_id_hora_id_ambiente` (`id_hora`,`id_ambiente`),
  ADD KEY `id_hora` (`id_hora`),
  ADD KEY `id_ambiente` (`id_ambiente`);

--
-- Indices de la tabla `facilitador`
--
ALTER TABLE `facilitador`
  ADD PRIMARY KEY (`cedula`);

--
-- Indices de la tabla `horas`
--
ALTER TABLE `horas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_rango_horas` (`hora_inicial`,`hora_final`);

--
-- Indices de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedula_participante` (`cedula_participante`),
  ADD KEY `fk_afh_inscripcion` (`id_asignacion_facilitador_curso`),
  ADD KEY `fk_inscripcion_periodo_nombre` (`nombre_inscripcion_periodo`);

--
-- Indices de la tabla `inscripcion_periodo`
--
ALTER TABLE `inscripcion_periodo`
  ADD PRIMARY KEY (`nombre`);

--
-- Indices de la tabla `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`cedula`),
  ADD UNIQUE KEY `unique_cedula` (`cedula`);

--
-- Indices de la tabla `pensum`
--
ALTER TABLE `pensum`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `preseleccion_curso`
--
ALTER TABLE `preseleccion_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedula_participante` (`cedula_participante`),
  ADD KEY `id_preseleccion_periodo` (`id_preseleccion_periodo`),
  ADD KEY `codigo_pensum` (`codigo_pensum`);

--
-- Indices de la tabla `preseleccion_periodo`
--
ALTER TABLE `preseleccion_periodo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `resumen_participante_periodo`
--
ALTER TABLE `resumen_participante_periodo`
  ADD PRIMARY KEY (`cedula_participante`,`nombre_inscripcion_periodo`),
  ADD UNIQUE KEY `unique_participante_periodo` (`cedula_participante`,`nombre_inscripcion_periodo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ambiente`
--
ALTER TABLE `ambiente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `asignacion_facilitador_curso`
--
ALTER TABLE `asignacion_facilitador_curso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asignacion_hr_amb`
--
ALTER TABLE `asignacion_hr_amb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `horas`
--
ALTER TABLE `horas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `preseleccion_curso`
--
ALTER TABLE `preseleccion_curso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `preseleccion_periodo`
--
ALTER TABLE `preseleccion_periodo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignacion_facilitador_curso`
--
ALTER TABLE `asignacion_facilitador_curso`
  ADD CONSTRAINT `asignacion_facilitador_curso_ibfk_1` FOREIGN KEY (`cedula_facilitador`) REFERENCES `facilitador` (`cedula`),
  ADD CONSTRAINT `asignacion_facilitador_curso_ibfk_3` FOREIGN KEY (`codigo_pensum`) REFERENCES `pensum` (`codigo`),
  ADD CONSTRAINT `asignacion_facilitador_curso_ibfk_6` FOREIGN KEY (`id_asignacion_hr_amb`) REFERENCES `asignacion_hr_amb` (`id`);

--
-- Filtros para la tabla `asignacion_hr_amb`
--
ALTER TABLE `asignacion_hr_amb`
  ADD CONSTRAINT `asignacion_hr_amb_ibfk_1` FOREIGN KEY (`id_hora`) REFERENCES `horas` (`id`),
  ADD CONSTRAINT `asignacion_hr_amb_ibfk_2` FOREIGN KEY (`id_ambiente`) REFERENCES `ambiente` (`id`);

--
-- Filtros para la tabla `inscripcion`
--
ALTER TABLE `inscripcion`
  ADD CONSTRAINT `fk_afh_inscripcion` FOREIGN KEY (`id_asignacion_facilitador_curso`) REFERENCES `asignacion_facilitador_curso` (`id`),
  ADD CONSTRAINT `fk_inscripcion_periodo_nombre` FOREIGN KEY (`nombre_inscripcion_periodo`) REFERENCES `inscripcion_periodo` (`nombre`),
  ADD CONSTRAINT `fk_participante_inscripcion` FOREIGN KEY (`cedula_participante`) REFERENCES `participante` (`cedula`) ON DELETE CASCADE;

--
-- Filtros para la tabla `preseleccion_curso`
--
ALTER TABLE `preseleccion_curso`
  ADD CONSTRAINT `fk_participante_preseleccion_curso` FOREIGN KEY (`cedula_participante`) REFERENCES `participante` (`cedula`),
  ADD CONSTRAINT `fk_pensum_preseleccion` FOREIGN KEY (`codigo_pensum`) REFERENCES `pensum` (`codigo`),
  ADD CONSTRAINT `fk_preseleccion_periodo` FOREIGN KEY (`id_preseleccion_periodo`) REFERENCES `preseleccion_periodo` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
