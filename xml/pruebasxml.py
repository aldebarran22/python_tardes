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


if __name__ == "__main__":
    cargaDOM("Pedidos.xml")
