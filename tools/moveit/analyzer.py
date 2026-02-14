import pandas as pd

class AgileProjectAnalyzer:
    """
    Herramienta de automatización de métricas para Project Managers.
    Inspirada en la gestión de brecha de tareas críticas (<12%) realizada en Ternium.
    """
    def __init__(self, file_path):
        # Simulación de proceso ETL: Carga y limpieza de datos
        self.data = pd.read_csv(file_path)
    
    def get_critical_gap(self):
        """Calcula el porcentaje de tareas de alta prioridad no finalizadas."""
        critical = self.data[self.data['priority'] == 'High']
        pending = critical[critical['status'] != 'Done']
        
        gap = (len(pending) / len(critical)) * 100
        return round(gap, 2)

    def run_report(self):
        gap = self.get_critical_gap()
        print(f"--- REPORTE DE ESTADO ÁGIL ---")
        print(f"Brecha Crítica Actual: {gap}%")
        
        # Lógica de negocio basada en objetivos de cumplimiento (SLA)
        if gap <= 12:
            print("Estado: SALUDABLE. Cumple con el objetivo de eficiencia.")
        else:
            print("Estado: ALERTA. Requiere gestión de riesgos inmediata.")

if __name__ == "__main__":
    analyzer = AgileProjectAnalyzer('sprint_data.csv')
    analyzer.run_report()