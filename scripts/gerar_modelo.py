"""Gera modelos/modelo-morada.dxf a partir de modelos/padrao-layers.json.

Uso: python scripts/gerar_modelo.py   (requer: pip install ezdxf)
"""
import json
from pathlib import Path

import ezdxf
from ezdxf import units

RAIZ = Path(__file__).resolve().parent.parent
PADRAO = RAIZ / "modelos" / "padrao-layers.json"
SAIDA = RAIZ / "modelos" / "modelo-morada.dxf"


def main():
    padrao = json.loads(PADRAO.read_text(encoding="utf-8"))
    doc = ezdxf.new("R2000", setup=True)  # setup=True traz DASHED, CENTER, PHANTOM etc.
    doc.units = units.M
    doc.header["$MEASUREMENT"] = 1  # métrico
    doc.header["$LUNITS"] = 2  # decimal
    doc.header["$LUPREC"] = 2  # 0,00 m

    for camada in padrao["layers"]:
        layer = doc.layers.add(
            camada["name"],
            color=camada["color"],
            linetype=camada["linetype"],
            lineweight=round(camada["lineweight"] * 100),
        )
        layer.description = camada["description"]
        if camada.get("plot") is False:
            layer.dxf.plot = 0

    doc.styles.add("MORADA", font="arial.ttf")
    cota = doc.dimstyles.new("MORADA-1-50")
    cota.dxf.dimtxsty = "MORADA"
    cota.dxf.dimscale = 50  # escala da prancha
    cota.dxf.dimtxt = 0.0025  # 2,5 mm impressos
    cota.dxf.dimasz = 0.002
    cota.dxf.dimexo = 0.001
    cota.dxf.dimexe = 0.001
    cota.dxf.dimdec = 2
    cota.dxf.dimdsep = ord(",")
    cota.dxf.dimtsz = 0.0015  # tique em vez de seta
    cota.dxf.dimclrd = 7
    doc.header["$DIMSTYLE"] = "MORADA-1-50"
    doc.header["$CLAYER"] = "ARQ-PAREDE-MANTER"

    doc.saveas(SAIDA)
    print(f"{SAIDA.relative_to(RAIZ)}: {len(padrao['layers'])} layers")


if __name__ == "__main__":
    main()
