

preguntas_basicas = {
    'pregunta_1': {
        'enunciado': ['¿En qué año se firmó la Declaración de Independencia de Estados Unidos?'],
        'alternativas': [
            ['1776', 1],
            ['1789', 0],
            ['1804', 0],
            ['1754', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Cuántos planetas tiene el sistema solar?'],
        'alternativas': [
            ['7', 0],
            ['8', 1],
            ['9', 0],
            ['10', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Qué instrumento musical tiene teclas blancas y negras?'],
        'alternativas': [
            ['Guitarra', 0],
            ['Violín', 0],
            ['Piano', 1],
            ['Flauta', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': ['¿En qué año cayó el Muro de Berlín?'],
        'alternativas': [
            ['1987', 0],
            ['1989', 1],
            ['1991', 0],
            ['1993', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Quién escribió *Cien años de soledad*?'],
        'alternativas': [
            ['Mario Vargas Llosa', 0],
            ['Gabriel García Márquez', 1],
            ['Pablo Neruda', 0],
            ['Jorge Luis Borges', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Qué tipo de energía se obtiene del Sol?'],
        'alternativas': [
            ['Eólica', 0],
            ['Geotérmica', 0],
            ['Hidráulica', 0],
            ['Solar', 1]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': ['¿En qué conflicto histórico se utilizó por primera vez el gas mostaza?'],
        'alternativas': [
            ['Primera Guerra Mundial', 1],
            ['Segunda Guerra Mundial', 0],
            ['Guerra de Vietnam', 0],
            ['Guerra de Corea', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': ['¿Qué país tiene más premios Nobel de la Paz?'],
        'alternativas': [
            ['Noruega', 0],
            ['Alemania', 0],
            ['Estados Unidos', 1],
            ['Suiza', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': ['¿Cuál fue el primer satélite artificial lanzado al espacio?'],
        'alternativas': [
            ['Apollo 11', 0],
            ['Sputnik 1', 1],
            ['Voyager 1', 0],
            ['Hubble', 0]
        ]
    }
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}