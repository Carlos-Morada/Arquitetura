# Arquitetura — Morada Propriedades

Repositório de desenhos técnicos da Morada Propriedades (reformas totais, house flipping e
incorporação vertical de pequeno porte em Belo Horizonte). Os desenhos são feitos no
**CADCraft** (CAD 2D open-source, compatível com DXF/DWG), que o Claude controla via MCP.

## Como falar com o CADCraft

Dois servidores MCP estão em `.mcp.json`:

- `cadcraft` — ponte para o app aberto (`cadcraft --control 7979`). Use este por padrão: o Carlos
  vê o desenho sendo feito. Se a chamada falhar dizendo que o app não responde, peça para ele
  abrir o CADCraft com `--control 7979` (ver README).
- `cadcraft-headless` — sessão sem janela, para gerar/converter/conferir arquivos em lote.

Ferramentas principais: `command_line` (digitar como no AutoCAD: `line 0,0 @3.5,0`),
`script`, `execute` (comando + parâmetros JSON; `list_commands` mostra o catálogo),
`inspect_drawing`, `query_entities`, `find_text`, `render` (PNG para conferir),
`open`, `save` (salvar em `.pdf`/`.svg`/`.png` exporta).

Depois de desenhar, **sempre** confira com `inspect_drawing` e `render` antes de dizer que terminou.

## Convenções de desenho

- **Unidade: metro**, 2 casas decimais, vírgula decimal nas cotas (padrão brasileiro).
- Comece novos desenhos abrindo `modelos/modelo-morada.dxf` e salvando com outro nome — ele já
  tem os layers, o estilo de texto `MORADA` e o estilo de cota `MORADA-1-50`.
- Se o desenho não veio do modelo, crie os layers de `modelos/padrao-layers.json` com
  `execute {"command": "layer.new", "params": {name, color, linetype, lineweight}}`.
- Reformas seguem a NBR 6492: **manter** (`ARQ-PAREDE-MANTER`, cinza), **demolir**
  (`ARQ-PAREDE-DEMOLIR`, amarelo tracejado), **construir** (`ARQ-PAREDE-CONSTRUIR`, vermelho).
- Nunca desenhe no layer `0`. Nunca altere `ARQ-ESTRUTURA` sem pedido explícito — remoção de
  pilar/viga/laje exige projeto estrutural.
- Escalas usuais: plantas e layouts 1:50, detalhes 1:20/1:25, implantação/terreno 1:100–1:200.
- Salve em DXF (CADCraft grava DXF/DWG R2000). Entidades que o CADCraft ainda não modela são
  descartadas ao salvar: ao editar DWG recebido de terceiros, salve uma cópia, nunca por cima.
- Fontes SHX não são lidas (o CADCraft usa fonte própria); prefira estilos TrueType.

## Organização

- `modelos/` — modelo DXF e padrão de layers (`scripts/gerar_modelo.py` regenera o DXF a partir
  do JSON: `pip install ezdxf && python scripts/gerar_modelo.py`).
- `projetos/<AAAA>-<codigo>-<endereco-curto>/` — um diretório por obra/terreno, por exemplo
  `projetos/2026-R014-rua-pernambuco-1200/`, com `existente.dxf`, `reforma.dxf`, `layout.dxf` e PDFs.

Responda em português.
