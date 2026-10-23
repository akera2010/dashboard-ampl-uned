import pandas as pd
import matplotlib.pyplot as plt
import os

def generar_grafico(ruta_csv, nombre_imagen, titulo, ylabel, color='#2ca02c'):
    if not os.path.exists(ruta_csv):
        print(f"⚠️ Omitiendo {ruta_csv} (No se ha generado en AMPL)")
        return

    df = pd.read_csv(ruta_csv)
    fig, ax = plt.subplots(figsize=(8, 5))
    colores = [color if val > 0.001 else '#d3d3d3' for val in df.iloc[:, 1]]
    
    barras = ax.bar(df.iloc[:, 0], df.iloc[:, 1], color=colores, width=0.5)
    ax.bar_label(barras, padding=3, fontsize=11, fontweight='bold', fmt='%.2f')
    
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.text(0.98, 0.05, 'Sandra Blanco | UNED 2026', transform=ax.transAxes, 
            ha='right', va='bottom', fontsize=9, color='gray', alpha=0.7, fontstyle='italic')
    
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(nombre_imagen, dpi=300)
    plt.close()
    print(f"✅ Generado: {nombre_imagen}")

# --- GENERACIÓN DE GRÁFICOS ---
print("Iniciando generación...")
generar_grafico('Ejemplo_Guia/resultados1.csv', 'Grafico_Ejercicio1.png', 'Ej. 1: Max Beneficio', 'Unidades a Fabricar')
generar_grafico('Ejercicio_2/resultados2.csv', 'Grafico_Ejercicio2.png', 'Ej. 2: Producto D', 'Unidades a Fabricar')
generar_grafico('Ejercicio_3/resultados3.csv', 'Grafico_Ejercicio3.png', 'Ej. 3: Min Coste', 'Unidades a Comprar')
generar_grafico('Ejercicio_4/resultados4.csv', 'Grafico_Ejercicio4.png', 'Ej. 4: Min Coste Cap.', 'Unidades a Comprar')
generar_grafico('Ejercicio_5/resultados5.csv', 'Grafico_Ejercicio5.png', 'Ej. 5: Múltiples Recursos', 'Unidades a Fabricar')
generar_grafico('Ejercicio_6/resultados6.csv', 'Grafico_Ejercicio6.png', 'Ej. 6: Embalaje Limitado', 'Unidades a Fabricar')

# El Ejercicio 7 es especial
ruta_csv_7 = 'Ejercicio_7/resultados7.csv'
if os.path.exists(ruta_csv_7):
    df7 = pd.read_csv(ruta_csv_7)
    df7['Ruta'] = df7['Almacen'] + ' → ' + df7['Tienda']
    fig, ax = plt.subplots(figsize=(10, 5))
    barras = ax.bar(df7['Ruta'], df7['Unidades'], color='#1f77b4', width=0.5)
    ax.bar_label(barras, padding=3, fontsize=10, fontweight='bold', fmt='%.0f')
    ax.set_title('Ej. 7: Rutas de Transporte', fontsize=14, fontweight='bold', pad=15)
    ax.set_ylabel('Unidades Enviadas', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    ax.text(0.98, 0.05, 'Sandra Blanco | UNED 2026', transform=ax.transAxes, 
            ha='right', va='bottom', fontsize=9, color='gray', alpha=0.7, fontstyle='italic')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('Grafico_Ejercicio6.png', dpi=300)
    plt.close()
    print("✅ Generado: Grafico_Ejercicio6.png")
else:
    print(f"⚠️ Omitiendo {ruta_csv_6} (Falta ejecutar en AMPL)")

print("--- Proceso finalizado ---")