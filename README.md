# Arquitetura — Morada Propriedades

Desenhos técnicos (DXF/DWG) feitos no [CADCraft](https://github.com/storytold/cadcraft) com o
Claude Code desenhando, conferindo e exportando via MCP.

## Preparar o computador (uma vez)

O Claude conversa com o CADCraft pelo programa de linha de comando **`cadcraft-cli`**, que precisa
estar no PATH.

**Windows** (instalador `.msi`): o `cadcraft-cli.exe` já vem em `C:\Program Files\CADCraft\`, mas
fora do PATH. No PowerShell:

```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\CADCraft", "User")
```

**macOS**: o `.dmg` traz só o aplicativo. Baixe também `cadcraft-cli-<versão>-macos-universal.zip`
na página de [releases](https://github.com/storytold/cadcraft/releases), descompacte e mova:

```sh
sudo mv cadcraft-cli /usr/local/bin/
```

(Se instalou pelo Homebrew ou pelo pacote Linux, o `cadcraft-cli` normalmente já está no PATH.)

Confira em um terminal novo: `cadcraft-cli --version`.

## Usar no dia a dia

1. Abra o CADCraft com o canal de controle ligado:
   - Windows: `& "C:\Program Files\CADCraft\cadcraft.exe" --control 7979`
   - macOS: `open -a CADCraft --args --control 7979`
   - Linux: `cadcraft --control 7979 &`
2. Abra o Claude Code **nesta pasta** (`claude`). Na primeira vez ele pergunta se pode usar os
   servidores do `.mcp.json` — aceite. `/mcp` mostra se `cadcraft` está conectado.
3. Peça em português, por exemplo:
   - "Abra `modelos/modelo-morada.dxf` e desenhe a planta existente do apto 301 com estas medidas…"
   - "Marque em amarelo as paredes a demolir entre cozinha e sala e desenhe a nova bancada."
   - "Exporte a planta de reforma em PDF A3, escala 1:50."
   - "Lance as divisas deste lote e os afastamentos para um estudo de massa."

Sem o app aberto, o servidor `cadcraft-headless` ainda gera e converte arquivos sem janela.

## Conteúdo

| Caminho | O quê |
|---|---|
| `.mcp.json` | Servidores MCP `cadcraft` (app aberto, porta 7979) e `cadcraft-headless` |
| `CLAUDE.md` | Convenções que o Claude segue (unidade metro, layers, NBR 6492) |
| `modelos/modelo-morada.dxf` | Modelo com layers, estilo de texto e de cota 1:50 |
| `modelos/padrao-layers.json` | Padrão de layers (fonte do modelo) |
| `scripts/gerar_modelo.py` | Regenera o modelo DXF a partir do JSON |
| `projetos/` | Um diretório por obra ou terreno |
