from abc import ABC, abstractmethod


class ServicioAcademicoCompleto(ABC):
    @abstractmethod
    def matricular_curso(self, estudiante, curso):
        pass
    @abstractmethod
    def calificar_estudiante(self, estudiante, curso, nota):
        pass
    @abstractmethod
    def generar_horarios(self, semestre):
        pass
    @abstractmethod
    def gestionar_aulas(self,aula, operacion):
        pass
    @abstractmethod
    def procesar_pagos(self, estudiante, monto):
        pass

class ServicioMatriculas(ServicioAcademicoCompleto):
    def matricular_curso(self, estudiante, curso):
        return f"Matriculando {estudiante} en {curso}"
    def calificar_estudiante(self, estudiante, curso, nota):
        raise NotImplementedError("No es responsabilidad de matriculas")
    def generar_horarios(self, semestre):
        raise NotImplementedError("No es responsabilidad de matriculas")
    def gestionar_aulas(self,aula, operacion):
        raise NotImplementedError("No es responsabilidad de matriculas")
    def procesar_pagos(self, estudiante, monto):
        raise NotImplementedError("No es responsabilidad de matriculas")
