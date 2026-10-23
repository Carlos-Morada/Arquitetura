# Como usar — CADCraft + Claude (app do Windows)

## Toda vez que for trabalhar
1. Clique duas vezes em **"CADCraft (Claude)"** na área de trabalho.
2. Abra o **app Claude** e vá na aba **Code**.
3. Escolha a pasta **Documentos\arquitetura**.
4. Confira se o modelo está no **Opus** (seletor perto da caixa de mensagem).
5. Peça em português.

## Projeto atual: Léo e Samuel
Pasta: `projetos/2026-leo-e-samuel/`
- `00-levantamento-original-2026-10-20.dwg`: original, nunca salvar por cima.

Primeira mensagem para continuar:
> Abra `projetos/2026-leo-e-samuel/00-levantamento-original-2026-10-20.dwg` no CADCraft,
> me diga o que tem no desenho (layers, ambientes, medidas gerais) e salve uma cópia de
> trabalho como `01-existente.dxf` na mesma pasta.

## Se algo não funcionar
- **"o app não responde"**: o CADCraft foi aberto pelo ícone errado. Feche e abra pelo "CADCraft (Claude)".
- **cadcraft não conecta**: no PowerShell, `cadcraft-cli --version` precisa mostrar a versão.
- **Arquivos desatualizados**: no PowerShell, `cd ~\Documents\arquitetura` e depois `git pull`.

## Só se o atalho sumir (recriar, uma vez)
```powershell
$s=(New-Object -ComObject WScript.Shell).CreateShortcut("$([Environment]::GetFolderPath('Desktop'))\CADCraft (Claude).lnk"); $s.TargetPath="C:\Program Files\CADCraft\cadcraft.exe"; $s.Arguments="--control 7979"; $s.Save()
```
