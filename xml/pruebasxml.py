"""
Pruebas con el dom/sax en python
"""

from xml.etree import ElementTree


def cargaDOM(path):
    with open(path, "rt") as f:
        tree = ElementTree.parse(f)

    # Obtener los países donde hay pedidos:
    paises = set()
    for nodo in tree.iter():
        if nodo.tag == "pais":
            paises.add(nodo.text)
    print("paises:", sorted(paises))

    # Sumar los pedidos de Brasil:
    total = 0
    for nodo in tree.iter():
        if nodo.tag == "importe":
            importe = float(nodo.text.strip())

        if nodo.tag == "pais":
            pais = nodo.text.strip()
            if pais == "Brasil":
                print("pais:", pais, " importe: ", importe)
                total += importe

    print(f"El total de Brasil es: {total}")


if __name__ == "__main__":
    cargaDOM("Pedidos.xml")
