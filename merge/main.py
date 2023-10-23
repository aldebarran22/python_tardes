"""
Unir los 3 ficheros con la función merge
Borrar y renombrar columnas
"""

import pandas as pd


def generarPedidos():
    dfPedidos = pd.read_csv("Pedidos.txt", sep=";")
    print("Pedidos: ", dfPedidos.shape)

    dfEmpresas = pd.read_csv("Empresas.txt", sep=";")
    print("Empresas: ", dfEmpresas.shape)

    dfEmpleados = pd.read_csv("Empleados.txt", sep=";")
    print("Empleados: ", dfEmpleados.shape)

    # Merge entre pedidos y empleados:
    dfPedEmp = pd.merge(dfPedidos, dfEmpleados, left_on="idempleado", right_on="id")

    # Merge con las empresas:
    dfTotal = pd.merge(dfPedEmp, dfEmpresas, left_on="idempresa", right_on="id")
    dfTotal.rename(columns={"nombre": "empleado"}, inplace=True)
    dfTotal.drop(
        columns=["idempleado", "idempresa", "id_x", "id_y", "cargo"], inplace=True
    )
    dfTotal = dfTotal[["idpedido", "cliente", "empleado", "empresa", "importe", "pais"]]
    dfTotal.to_html("pedidos.html", index=False)


if __name__ == "__main__":
    generarPedidos()
